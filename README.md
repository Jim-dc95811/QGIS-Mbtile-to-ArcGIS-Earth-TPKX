# Direct MBTiles to ArcGIS Earth TPKX

**Make a native, offline Esri tile package from an existing raster MBTiles file, without an intermediate GeoTIFF or ArcGIS Pro export.**

The converter copies each source PNG or JPEG tile **byte-for-byte**, maps MBTiles TMS tile addresses into Esri's tile grid, writes indexed Compact Cache V2 `.bundle` files, and packages them as a `.tpkx` file. It does not change the imagery, invent missing zoom levels, resample pixels, or improve source resolution.

## Why this exists

QGIS can create raster MBTiles from a variety of imagery sources. Previously, this project's ArcGIS Earth workflow involved extra raster conversion and ArcGIS Pro processing, or KML super-overlays that experienced substantial navigation delays in ArcGIS Earth. A directly generated TPKX uses the application's native offline tile-package path instead.

The breakthrough was achieved by comparing two **working ArcGIS Pro-generated TPKX references** against experimental packages, correcting their metadata and binary bundle layout until the new packages worked in ArcGIS Earth. The multi-bundle colored diagnostic TPKX was also accepted by ArcGIS Pro. The project owner has now confirmed that an MBTiles file converted with the distributed script works very well in ArcGIS Earth.

This demonstrates a usable conversion route; it is not a claim that every possible MBTiles source, output size, or GIS application has been validated.

## Download and use

Download [mb2tpkx.zip](mb2tpkx.zip) and extract the two files together:

- `mb2tpkx.py` — standalone Python converter.
- `mb2tpkx.bat` — Windows launcher.

**Requirements:** Python 3 with the Pillow package, installed once with:

```powershell
py -m pip install Pillow
```

On Windows, drag an `.mbtiles` file onto `mb2tpkx.bat`, or double-click the BAT and paste the source file's full path when prompted. The original MBTiles remains unchanged. The resulting TPKX is created beside it; an existing output file is not overwritten.

For command-line use:

```powershell
py mb2tpkx.py "input.mbtiles" "output.tpkx"
```

The converter displays a progress line after completing each bundle. Large maps can require substantial disk space and time.

## Verified scope and limits

- Input: standard **Web Mercator raster MBTiles**, TMS row convention, **256 × 256 PNG/JPEG** tiles at zoom levels **0–23** as implemented. Other formats and grids are not silently converted.
- Output: native Esri **Compact Cache V2 TPKX** with 128 × 128 indexed tile blocks.
- Source imagery bytes are preserved. A separate thumbnail is generated from a source tile; it is not used to replace or alter map imagery.
- Verified during development: exact-tile byte comparisons, multiple bundles at the same zoom level, ArcGIS Earth acceptance of the color and real-imagery demonstration packages, ArcGIS Pro acceptance of the Color 2B package, and a successful real MBTiles-to-TPKX run of the distributed script reported by the project owner in ArcGIS Earth.
- **Still to stress-test:** district-scale files, many bundles across several zoom levels, diverse MBTiles layouts, uneven multizoom coverage, failure recovery, and a separate ArcGIS Pro acceptance check for freshly generated output from the distributed script.

See [TECHNICAL.md](TECHNICAL.md) for architecture, failure history, byte-level findings, and reproducibility notes.

## Imagery permissions

**Technical access is not a redistribution license.** The converter is source-independent, but imagery providers set their own rules for downloading, storing and redistributing their imagery. Before creating or sharing offline packages, verify that your chosen source permits the intended use. In particular, access to Google or Esri imagery through a QGIS service or plugin does not by itself establish permission for bulk download, offline retention, or redistribution.

## Format references

- [Esri Compact Cache V2 technical description](https://github.com/Esri/raster-tiles-compactcache/blob/master/CompactCacheV2.md)
- [Esri tile package specification](https://github.com/Esri/tile-package-spec)
- [MBTiles 1.3 specification](https://github.com/mapbox/mbtiles-spec/blob/master/1.3/spec.md)

**Project status:** working conversion baseline, under continued application and large-dataset validation. No software license is included yet; the repository owner must select one before others can assume permission to reuse or redistribute the code.
