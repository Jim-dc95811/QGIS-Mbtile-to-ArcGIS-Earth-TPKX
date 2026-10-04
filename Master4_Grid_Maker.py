import math
import re
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont, TiffImagePlugin
except ImportError:
    raise SystemExit(
        "Pillow is required. Install it with: py -3 -m pip install Pillow"
    )

EPSG = 3857
EARTH_RADIUS = 6378137.0
OUTPUT_DIR = Path(r"C:\downloads")
IMAGE_SIZE = 5000
WEB_MERCATOR_MAX_LAT = 85.05112878


def parse_coord(token, longitude):
    match = re.fullmatch(r"\s*(\d+(?:\.\d+)?)\s*([NSEWnsew])\s*", token)
    if not match:
        raise ValueError(f"Invalid coordinate: {token.strip()}")

    value = float(match.group(1))
    direction = match.group(2).upper()

    if longitude and direction not in ("E", "W"):
        raise ValueError(f"Longitude must end in E or W: {token.strip()}")
    if not longitude and direction not in ("N", "S"):
        raise ValueError(f"Latitude must end in N or S: {token.strip()}")

    if longitude and value > 180:
        raise ValueError(f"Longitude must be 180 degrees or less: {token.strip()}")
    if not longitude and value > 90:
        raise ValueError(f"Latitude must be 90 degrees or less: {token.strip()}")

    if direction in ("W", "S"):
        value = -value
    return value, direction


def parse_master4(text):
    parts = [p.strip() for p in text.split(",")]
    if len(parts) != 4:
        raise ValueError("Enter exactly four coordinates separated by commas.")

    west, west_dir = parse_coord(parts[0], True)
    east, east_dir = parse_coord(parts[1], True)
    south, south_dir = parse_coord(parts[2], False)
    north, north_dir = parse_coord(parts[3], False)

    if west >= east:
        raise ValueError("The first longitude must be the west edge and the second the east edge.")
    if south >= north:
        raise ValueError("The third latitude must be the south edge and the fourth the north edge.")
    if not math.isclose(east - west, 1.0, abs_tol=1e-9):
        raise ValueError("The longitude edges must be exactly 1 degree apart.")
    if not math.isclose(north - south, 1.0, abs_tol=1e-9):
        raise ValueError("The latitude edges must be exactly 1 degree apart.")

    for value, name in (
        (west, "west longitude"),
        (east, "east longitude"),
        (south, "south latitude"),
        (north, "north latitude"),
    ):
        if not math.isclose(value, round(value), abs_tol=1e-9):
            raise ValueError(f"Master 4 edges must be whole degrees. Invalid {name}: {value}")

    if south <= -WEB_MERCATOR_MAX_LAT or north >= WEB_MERCATOR_MAX_LAT:
        raise ValueError("Latitude is outside the usable EPSG:3857 Web Mercator range.")

    label = "_".join(p.upper().replace(" ", "") for p in parts)
    return west, east, south, north, label


def mercator_x(lon_deg):
    return EARTH_RADIUS * math.radians(lon_deg)


def mercator_y(lat_deg):
    lat = math.radians(lat_deg)
    return EARTH_RADIUS * math.log(math.tan(math.pi / 4.0 + lat / 2.0))


def cell_records(west, east, south, north):
    """
    Cell numbering follows the first decimal digit of absolute latitude/longitude.

    Examples:
      30.56N, 81.34W -> cell 54
      30.56N, 10.34E -> cell 54
      30.56S, 81.34W -> cell 54
      30.56S, 10.34E -> cell 54

    This makes the 01-100 address pattern work in all four hemispheres.
    """
    records = []

    west_side = east <= 0.0
    south_side = north <= 0.0

    lon_base = abs(east) if west_side else abs(west)
    lat_base = abs(north) if south_side else abs(south)

    for cell_id in range(1, 101):
        row_digit = (cell_id - 1) // 10
        col_digit = (cell_id - 1) % 10

        if west_side:
            lon_w = -(lon_base + (col_digit + 1) / 10.0)
            lon_e = -(lon_base + col_digit / 10.0)
        else:
            lon_w = lon_base + col_digit / 10.0
            lon_e = lon_base + (col_digit + 1) / 10.0

        if south_side:
            lat_s = -(lat_base + (row_digit + 1) / 10.0)
            lat_n = -(lat_base + row_digit / 10.0)
        else:
            lat_s = lat_base + row_digit / 10.0
            lat_n = lat_base + (row_digit + 1) / 10.0

        xmin = mercator_x(lon_w)
        xmax = mercator_x(lon_e)
        ymin = mercator_y(lat_s)
        ymax = mercator_y(lat_n)
        records.append((cell_id, xmin, xmax, ymin, ymax))

    return records


def find_font(size):
    candidates = [
        Path(r"C:\Windows\Fonts\arialbd.ttf"),
        Path(r"C:\Windows\Fonts\Arialbd.ttf"),
        Path(r"C:\Windows\Fonts\calibrib.ttf"),
    ]
    for path in candidates:
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def make_grid_tif(path, west, east, south, north, records):
    width = IMAGE_SIZE
    height = IMAGE_SIZE

    master_xmin = mercator_x(west)
    master_xmax = mercator_x(east)
    master_ymin = mercator_y(south)
    master_ymax = mercator_y(north)

    image = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(image)
    font = find_font(92)

    def x_to_px(x):
        return (x - master_xmin) / (master_xmax - master_xmin) * (width - 1)

    def y_to_px(y):
        return (master_ymax - y) / (master_ymax - master_ymin) * (height - 1)

    for i in range(11):
        lon = west + i / 10.0
        x = round(x_to_px(mercator_x(lon)))
        draw.line([(x, 0), (x, height - 1)], fill=255, width=12 if i in (0, 10) else 8)

        lat = south + i / 10.0
        y = round(y_to_px(mercator_y(lat)))
        draw.line([(0, y), (width - 1, y)], fill=255, width=12 if i in (0, 10) else 8)

    for cell_id, xmin, xmax, ymin, ymax in records:
        x_center = x_to_px((xmin + xmax) / 2.0)
        y_center = y_to_px((ymin + ymax) / 2.0)
        label = f"{cell_id:02d}" if cell_id < 100 else "100"
        bbox = draw.textbbox((0, 0), label, font=font, stroke_width=8)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
        draw.text(
            (x_center - text_w / 2.0, y_center - text_h / 2.0),
            label,
            font=font,
            fill=255,
            stroke_width=8,
            stroke_fill=64,
        )

    pixel_x = (master_xmax - master_xmin) / width
    pixel_y = (master_ymax - master_ymin) / height

    tiffinfo = TiffImagePlugin.ImageFileDirectory_v2()
    tiffinfo[33550] = (pixel_x, pixel_y, 0.0)  # ModelPixelScaleTag
    tiffinfo[33922] = (0.0, 0.0, 0.0, master_xmin, master_ymax, 0.0)  # ModelTiepointTag
    tiffinfo[34735] = (
        1, 1, 0, 3,
        1024, 0, 1, 1,      # GTModelTypeGeoKey = Projected
        1025, 0, 1, 1,      # GTRasterTypeGeoKey = PixelIsArea
        3072, 0, 1, EPSG,   # ProjectedCSTypeGeoKey = EPSG:3857
    )
    tiffinfo[42113] = "0"  # GDAL_NODATA: background is transparent/NoData

    image.save(path, format="TIFF", compression="tiff_deflate", tiffinfo=tiffinfo)


def write_extent_txt(path, records):
    with path.open("w", encoding="utf-8", newline="\n") as f:
        for cell_id, xmin, xmax, ymin, ymax in records:
            label = f"{cell_id:02d}" if cell_id < 100 else "100"
            f.write(
                f"{label} {xmin:.4f},{xmax:.4f},{ymin:.4f},{ymax:.4f} [EPSG:{EPSG}]\n"
            )


def build_outputs(master4_text, output_dir=OUTPUT_DIR):
    west, east, south, north, master_label = parse_master4(master4_text)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    txt_path = output_dir / f"Master4_{master_label}_Extents.txt"
    tif_path = output_dir / f"Master4_{master_label}_Grid.tif"

    records = cell_records(west, east, south, north)
    write_extent_txt(txt_path, records)
    make_grid_tif(tif_path, west, east, south, north, records)
    return txt_path, tif_path


def main():
    print("Master 4 Grid Maker")
    print("Example: 82w, 81w, 30n, 31n")
    print("East example: 10e, 11e, 30n, 31n")
    print("South example: 82w, 81w, 31s, 30s")
    print()
    master4_text = input("Enter Master 4: ").strip()

    try:
        txt_path, tif_path = build_outputs(master4_text)
    except Exception as exc:
        print(f"\nERROR: {exc}")
        raise SystemExit(1)

    print("\nCreated:")
    print(txt_path)
    print(tif_path)


if __name__ == "__main__":
    main()
