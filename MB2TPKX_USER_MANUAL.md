# MBTiles to TPKX Converter v1.1 - User Manual

A printable copy of this manual is available as [mb2tpkx_User_Manual.pdf](mb2tpkx_User_Manual.pdf).

## Purpose

Convert an existing raster MBTiles file directly to a native Esri TPKX for offline viewing in ArcGIS Earth. ArcGIS Earth cannot open MBTiles itself; it can open the converted TPKX.

Source PNG/JPEG map tiles are copied unchanged. The converter does not download imagery and does not rebuild or add zoom levels.

## Requirements

- Windows
- Python 3 from python.org, with the `py` launcher
- Pillow (one extra Python library)
- An existing compatible raster MBTiles file

Check Python and install Pillow once from a Command Prompt:

```text
py -3 --version
py -3 -m pip install Pillow
```

## Get the converter

1. Download [`mb2tpkx.zip`](mb2tpkx.zip).
2. Extract it into a folder of its own. The zip holds `mb2tpkx.py` and `mb2tpkx.bat` directly, not a subfolder.
3. Keep the two files together.

## Run it

1. Drag your `.mbtiles` file onto `mb2tpkx.bat`, or double-click the BAT and paste the full path when asked:

   ```text
   Enter the full path to your MBTiles file:
   ```

2. The console shows `mb2tpkx 1.1`, then one line per finished tile bundle, for example `z20 tile/L20/R69480C45b00.bundle complete`.
3. Wait for the `SUCCESS` line, for example:

   ```text
   SUCCESS: 6461 original tiles, 14 bundles -> C:\Maps\bryceville_7_layer_mbtile.tpkx
   ```

   The window then shows `Conversion complete.` and waits for a key press.
4. The TPKX is created beside the MBTiles with the same base name. The MBTiles is not changed.
5. Open the TPKX in ArcGIS Earth and check the map.

## Command line

```text
py -3 mb2tpkx.py "input.mbtiles" "output.tpkx"
```

If the output name is left out, the input name is reused with `.tpkx`.

## Supported input

Standard Web Mercator raster MBTiles with 256 x 256 PNG or JPEG tiles, TMS tile rows, zoom levels 0-23. QGIS is one way to make them; the converter does not require QGIS. Vector MBTiles and other projections are outside the verified scope.

## What it does

1. Reads the MBTiles database.
2. Converts its TMS tile rows to Esri XYZ rows.
3. Groups the tiles into 128 x 128 Compact Cache V2 bundles.
4. Writes the TPKX metadata.
5. Copies every source tile byte for byte.

Only a separate presentation thumbnail is generated.

## Safe output

- An existing TPKX is never overwritten.
- The new TPKX is written as `<name>.tpkx.partial` and renamed only when the conversion has fully succeeded.
- If a conversion fails or is cancelled, the partial file is removed. Nothing needs cleaning up before you try again.

## Messages and what to do

Problems are reported as one plain `ERROR:` line, followed by `Conversion failed. Check the error above.`

| Message | What to do |
|---|---|
| `ERROR: Pillow is not installed...` | Run `py -3 -m pip install Pillow`. |
| `MBTiles file not found` | Check the path, or drag the file onto the BAT. |
| `Output already exists ... delete or rename it and run again.` | Move, rename or delete the old TPKX. |
| `Input and output paths cannot be the same.` | Give the output a `.tpkx` name. |
| `MBTiles has no imagery tiles.` | The MBTiles is empty; rebuild it in QGIS. |
| `Could not read ... as an MBTiles database` | The file is damaged or not an MBTiles file. |
| `Only 256 x 256 PNG/JPEG MBTiles are supported...` or `Unsupported image format` | Rebuild the MBTiles with 256-pixel PNG or JPEG tiles. |
| `A tile is not a readable PNG/JPEG image.` | A tile in the MBTiles is damaged; rebuild it. |
| `Input zoom levels exceed the verified 0-23 Esri tiling scheme.` | Use zoom levels 0-23. |
| `File problem - ...` | Usually a full disk or a locked file; free space or close the program using it. |

## Large files

Allow enough time and free disk space: because the tiles are copied unchanged, the TPKX is roughly the same size as the MBTiles (a 97 MB Bryceville MBTiles became a 95 MB TPKX). 4 GB, 20+ GB and 40 GB-class packages have been converted and opened in ArcGIS Earth.

## QGIS workflow

1. Create the raster MBTiles in QGIS with your intended source, extent, zoom range and image format.
2. For large systematic coverage, use the [Master 4 Grid Maker](MASTER4_GRID_MAKER.md) for exact, repeatable extents and file names.
3. Convert each MBTiles with `mb2tpkx.bat`.
4. Check the resulting TPKX in ArcGIS Earth before field use.

## Quick reference

```text
Install:  py -3 -m pip install Pillow
Run:      drag input.mbtiles onto mb2tpkx.bat
Output:   input.tpkx beside input.mbtiles
```

The input MBTiles stays unchanged. An existing TPKX is protected from overwrite.

## Source rights

This utility does not grant rights to third-party imagery. Use only imagery you are authorized to acquire, retain, convert, display or redistribute. See [LEGAL.md](LEGAL.md).
