# MBTiles -> TPKX: offline maps for ArcGIS Earth

**Make native offline ArcGIS Earth maps from compatible raster MBTiles, then organize large areas with the Master 4 grid system.** The converter preserves the original PNG/JPEG map tiles at every recorded zoom level. Master 4 adds repeatable geographic cells, deterministic filenames, a numbered reference overlay, and an optional synthetic TPKX that makes stored zoom levels visible before QGIS production begins.

## Watch the videos

**[Google Maps OFFLINE - The Impossible Is Now Possible!](https://www.youtube.com/watch?v=8uziJNzan1g)**

[![Watch the offline maps demonstration](https://img.youtube.com/vi/8uziJNzan1g/hqdefault.jpg)](https://www.youtube.com/watch?v=8uziJNzan1g)

The video shows online Street and Hybrid map navigation over Jacksonville, then an offline demonstration in ArcGIS Earth. The synthetic color-tile sequence makes separately stored zoom levels visible. **This reproduces a captured map-display experience, not Google's complete application:** search, live traffic, Street View, routing and other online services are not reproduced.

### Make your own offline map - QGIS and ArcGIS Earth tutorial

**[How to Make an Offline Map with QGIS and ArcGIS Earth](https://www.youtube.com/watch?v=C71n8TAByuE)**

[![Watch the Washington, DC map-making tutorial](https://img.youtube.com/vi/C71n8TAByuE/hqdefault.jpg)](https://www.youtube.com/watch?v=C71n8TAByuE)

The Washington, DC follow-along tutorial demonstrates the basic production route: create raster MBTiles in QGIS, convert the file to TPKX with this repository's Python tool, and open the finished map in ArcGIS Earth.

### Master 4 Grid Maker - systematic large-area map production

**[Watch the Master 4 Grid Maker video](https://www.youtube.com/watch?v=zNt-I4KgAy8)**

[![Watch the Master 4 Grid Maker video](https://img.youtube.com/vi/zNt-I4KgAy8/hqdefault.jpg)](https://www.youtube.com/watch?v=zNt-I4KgAy8)

This one-take video demonstrates the large-area chain from an empty 1-degree x 1-degree area through Master 4, exact QGIS-ready extents, deterministic filenames, QGIS batch production, MBTiles, TPKX conversion and final viewing in ArcGIS Earth.

### ArcGIS Earth Mobile - using offline TPKX maps

**[Watch the ArcGIS Earth Mobile offline map-use video](https://www.youtube.com/watch?v=_FT3GOyjL5Y)**

[![Watch the ArcGIS Earth Mobile offline map-use video](https://img.youtube.com/vi/_FT3GOyjL5Y/hqdefault.jpg)](https://www.youtube.com/watch?v=_FT3GOyjL5Y)

This companion video demonstrates using the offline TPKX map workflow in ArcGIS Earth Mobile on Android.

**New here?** Start with [DEMO.md](DEMO.md). **Operating Master 4?** Use the [Master 4 guide](MASTER4_GRID_MAKER.md) and the [official PDF operator manual](Master4_Grid_Maker_User_Manual.pdf). **Continuing the engineering project?** Read [CONTINUITY.md](CONTINUITY.md) and [TECHNICAL.md](TECHNICAL.md).

## Master 4 v3: where the map belongs + what zoom level you are seeing

![Master 4 Cell 55 multi-zoom TPKX teaching graphic](images/Master4_Cell55_MultiZoom_TPKX.jpg)

Master 4 v3 keeps the original production workflow and adds one **optional** teaching/reference product.

Enter one whole-degree Master 4 box in this order:

```text
82w, 81w, 30n, 31n
```

The program always creates the two normal files first:

```text
Master4_82W_81W_30N_31N_Extents.txt
Master4_82W_81W_30N_31N_Grid.tif
```

The TXT contains **100 cell production rows plus one final `MASTER` row** for the full 1-degree box. Each numbered row carries the exact QGIS-ready EPSG:3857 extent and deterministic production filename:

```text
01 -9028010.7033,-9016878.7543,3503549.8435,3516410.3983 [EPSG:3857] W082W081N031N030-001-GHY-Z20.tpkx
...
MASTER -9128198.2450,-9016878.7543,3503549.8435,3632749.1434 [EPSG:3857]
```

After those standard outputs are finished, v3 asks:

```text
Create Cell 55 colored zoom-demo TPKX (Z10-Z20)? [y/N]:
```

**The demo is opt-in. `No` is the default.** Press Enter or type `N` and the program exits normally with the standard Master 4 files already complete. Type `Y` or `Yes` only when you want the synthetic demo/reference TPKX.

For the example above the optional file is named:

```text
W082W081N031N030-055-ZOOM-DEMO.tpkx
```

It contains synthetic colored raster tiles for **Z10 through Z20**, each visibly labeled with its stored zoom level and `CELL 55`. The project owner generated the current v3 package on Windows and opened it successfully in ArcGIS Earth, visually confirming multiple transitions including Z12, Z13, Z14, Z15, Z17 and Z20. The owner reported a current test file of roughly **1 GB**; size varies with latitude and PNG compression.

### Why the optional TPKX exists

It has three useful roles:

- **Teaching:** it makes the multiresolution raster tile pyramid obvious. As ArcGIS Earth changes stored levels, the color and giant Z-number change.
- **Pre-QGIS sanity check:** it gives a new user a real TPKX to open before any imagery production. The package is generated from the same Master 4 geography and acts as a quick check that the viewer, home grid and TPKX path are behaving as expected.
- **Offline reference beacon:** when the online basemap is unavailable and the display loses familiar context, opening the local demo TPKX gives a known geographic anchor and visible zoom-level feedback again.

The colored package uses the standard global XYZ/Web Mercator tile grid. At coarse zooms, a tile is much larger than a 0.1-degree Master 4 cell, so colored tiles can visibly extend beyond the exact Cell 55 boundary. Use the numbered GeoTIFF and manifest for exact cell boundaries; use the synthetic TPKX for geographic/zoom awareness.

## Recommended ArcGIS Earth field flow

1. Keep one or more **area-wide Z17 overview TPKX** maps available for broad context.
2. When an area of interest appears, enable the **Master 4 numbered GeoTIFF overlay**.
3. Identify the numbered cell or adjacent cells covering the area.
4. Use the manifest rows for exact extents and filenames.
5. Optionally open the **Cell 55 Z10-Z20 demo TPKX** as a fast TPKX/geographic sanity check before touching QGIS.
6. Produce only the real high-resolution cells you need in QGIS, convert compatible MBTiles to TPKX, and load them over the overview map.

**Permanent production rule:** reference overlays **ON while planning; OFF before production**. Leaving the numbered overlay visible during raster production can burn the grid into the finished imagery.

## Project illustrations

**The conversion workflow, in four simple steps:**

![Four-step illustration: imagery source, QGIS MBTiles production, Python conversion, and offline ArcGIS Earth](images/ChatGPT%20Image%20Sep%2027%2C%202026%2C%2010_58_45%20PM.png)

**The MBTiles -> TPKX breakthrough:**

![MBTiles to TPKX breakthrough graphic and offline ArcGIS Earth viewer](images/ChatGPT%20Image%20Sep%2027%2C%202026%2C%2012_44_11%20PM.png)

### Understanding zoomable maps

**1. A multiresolution raster tile pyramid - one geographic area at different zoom levels.** Each closer zoom uses more tiles to cover the same territory, revealing progressively finer map detail.

![Exploded multiresolution raster tile pyramid](images/ChatGPT%20Image%20Sep%2029%2C%202026%2C%2008_00_20%20PM-1.png)

**2. Combining imagery and road-overlay pyramids.** Matching geographic extents and zoom levels let road lines and labels appear over satellite imagery, creating a hybrid map view.

![Separate satellite imagery and road-overlay tile pyramids combining into a hybrid map](images/ChatGPT%20Image%20Sep%2029%2C%202026%2C%2008_00_22%20PM-2.png)

**3. Layer order matters.** Put the road overlay above the imagery: reversing the order can hide the roads and labels.

![Correct and incorrect layer order](images/ChatGPT%20Image%20Sep%2029%2C%202026%2C%2008_00_24%20PM-3.png)

These diagrams explain tile pyramids and layer compositing. They do **not** imply that the converter merges separate imagery and overlay MBTiles files; combined views can be rendered upstream while creating the input MBTiles.

## Master 4 Grid Maker downloads

**[Download Master4_Grid_Maker.zip](Master4_Grid_Maker.zip)**  
**[Read the full Master 4 guide](MASTER4_GRID_MAKER.md)**  
**[Open the v3 Operator Manual](Master4_Grid_Maker_User_Manual.pdf)**

The Master 4 numbering is hemisphere-aware. The first decimal digit of absolute latitude gives the tens row; the first decimal digit of absolute longitude plus one gives the column. Thus `30.56N, 81.34W`, `30.56N, 10.34E`, `30.56S, 81.34W`, and `30.56S, 10.34E` all identify **cell 54**.

The standard grid/output regression tests covered W/N, E/N, W/S and E/S boxes, the equator and prime meridian, +/-180 degrees, and whole-degree boxes near the practical Web Mercator latitude limits. The v3 update preserved the standard TXT/GeoTIFF behavior and added the optional synthetic TPKX. See [MASTER4_GRID_MAKER.md](MASTER4_GRID_MAKER.md) and [TECHNICAL.md](TECHNICAL.md) for exact scope.

## Four steps from imagery to offline map

1. **Choose an imagery source** appropriate for your purpose, with the necessary rights for your intended use.
2. **Create compatible raster MBTiles.** QGIS is one example; the converter does not require QGIS specifically.
3. **Convert MBTiles -> TPKX** with `mb2tpkx.py`. The converter copies the original PNG/JPEG image tiles without re-encoding or rebuilding the zoom pyramid.
4. **Open the TPKX in ArcGIS Earth** and navigate the captured map offline.

```mermaid
flowchart LR
    A[Imagery source] --> B[Raster MBTiles producer]
    B -->|MBTiles| C[Python converter]
    C -->|TPKX| D[ArcGIS Earth offline]
```

## Converter download and use

### First-time Windows setup

1. Install Python 3 and confirm `py -3 --version` works.
2. Install the only additional Python library, Pillow:

```powershell
py -3 -m pip install Pillow
```

3. Download this repository or keep `mb2tpkx.py` and `mb2tpkx.bat` in the same folder.

**Run it on Windows:** drag an existing `.mbtiles` file onto `mb2tpkx.bat`, or double-click the BAT and paste the source path when prompted.

**Command line:**

```powershell
py -3 mb2tpkx.py "input.mbtiles" "output.tpkx"
```

The source MBTiles is retained. Existing output is not overwritten. Open the finished `.tpkx` with ArcGIS Earth.

## Real-world converter results

These are owner-reported, screenshot-supported field tests, not universal guarantees.

| Example | Source MBTiles (Windows-displayed KB) | Resulting TPKX (KB) | Reported observation |
| --- | ---: | ---: | --- |
| First large real-data test | 4,137,400 | 4,108,022 | Loaded and navigated correctly in ArcGIS Earth |
| Z20 PNG grid, Master 3-1 | 39,891,100 | 39,587,335 | Responsive offline viewing |
| Z20 JPEG/75 grid, Master 3-2 | 4,354,360 | 4,090,206 | Clear zoom-dependent hybrid cartography |
| Jacksonville Metro Z20, JPEG/75 | 21,786,032 | 20,629,591 | Large single-file metropolitan hybrid map loaded in ArcGIS Earth |

JPEG/75 is chosen while producing MBTiles, not by the converter. The PNG and JPEG examples are different production grids, so they are useful field observations rather than a controlled same-source compression benchmark.

## What the converter supports

- **Input:** standard Web Mercator **raster** MBTiles with 256 x 256 PNG/JPEG image tiles using the TMS row convention; implemented tiling levels 0-23.
- **Output:** Esri Compact Cache V2 TPKX with indexed 128 x 128 tile bundles.
- **Image handling:** source map tile bytes are copied unchanged. A separate presentation thumbnail is generated.
- **Scope:** it does not convert vector MBTiles, arbitrary projections, or every unconventional MBTiles layout.
- **Testing:** a synthetic multi-bundle package was accepted by ArcGIS Earth and ArcGIS Pro; real production output has been field-tested extensively in ArcGIS Earth. Large real packages should not be described as ArcGIS Pro-validated unless separately tested there.

## Documentation

- [00_USER_MANUALS.md](00_USER_MANUALS.md) - official PDF manuals.
- [DEMO.md](DEMO.md) - videos and beginner/field workflow.
- [MASTER4_GRID_MAKER.md](MASTER4_GRID_MAKER.md) - Master 4 v3 operation and optional demo TPKX.
- [CONTINUITY.md](CONTINUITY.md) - current project handoff.
- [TECHNICAL.md](TECHNICAL.md) - technical behavior, format invariants and current v3 record.
- [RELEASE_CHECKLIST.md](RELEASE_CHECKLIST.md) - public-release and regression review.
- [CREDITS.md](CREDITS.md) - specifications, dependencies and acknowledgments.
- [LEGAL.md](LEGAL.md) - imagery-provider rights, attribution and trademark limits.
- [CONTRIBUTING.md](CONTRIBUTING.md) / [SECURITY.md](SECURITY.md) - participation and reporting.
- [LICENSE](LICENSE) - MIT License, copyright 2026 Jim Gaddy.

## Human-AI engineering collaboration

This project was conceived, directed, developed through hands-on experiments, and field-tested by **Jim Gaddy**, working with **OpenAI's ChatGPT** as an AI coding and documentation partner. Jim supplied the problem, technical direction, reference tests and real-world acceptance testing; ChatGPT assisted with implementation, technical research, regression work, diagrams and documentation.

This acknowledgment is not a claim of OpenAI sponsorship or endorsement and does not alter any rights in third-party software, specifications or imagery.

## Formats, source rights and attribution

The converter connects the documented [Mapbox MBTiles](https://github.com/mapbox/mbtiles-spec) format with Esri's published [Compact Cache V2](https://github.com/Esri/raster-tiles-compactcache) / [TPKX specification](https://github.com/Esri/tile-package-spec). Format specifications do not grant rights to third-party imagery.

**Use only source imagery you are authorized to acquire, retain, convert and display for your intended purpose.** The converter does not automatically propagate all separate MBTiles attribution fields. The optional Master 4 color-demo TPKX contains only synthetic project-generated colored tiles; it does not download commercial imagery.

Independent project; **not affiliated with or endorsed by** Google, QGIS, Esri or Mapbox. Actual map currency, alignment, coverage, device operation and permissions should be checked before operational use.
