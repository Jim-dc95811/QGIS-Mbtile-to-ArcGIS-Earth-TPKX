# MBTiles -> TPKX: offline maps for ArcGIS Earth

## Download the tools

### **⬇️ [DOWNLOAD MBTILES -> TPKX CONVERTER](mb2tpkx.zip)**
Convert compatible raster MBTiles directly into native offline TPKX packages for ArcGIS Earth.

### **⬇️ [DOWNLOAD MASTER 4 GRID MAKER](Master4_Grid_Maker.zip)**
Create repeatable 1-degree production grids, numbered cells, exact QGIS-ready extents, and deterministic filenames.

**Make native offline ArcGIS Earth maps from compatible raster MBTiles, then organize large areas with the Master 4 grid system.** The converter preserves the original PNG/JPEG map tiles at every recorded zoom level. Master 4 adds repeatable geographic cells, deterministic filenames, a numbered reference overlay, and an optional synthetic TPKX that makes stored zoom levels visible before QGIS production begins.

## Watch the videos

**[Google Maps OFFLINE - The Impossible Is Now Possible!](https://www.youtube.com/watch?v=8uziJNzan1g)**

[![Watch the offline maps demonstration](https://img.youtube.com/vi/8uziJNzan1g/hqdefault.jpg)](https://www.youtube.com/watch?v=8uziJNzan1g)

The video shows online Street and Hybrid map navigation over Jacksonville, then an offline demonstration in ArcGIS Earth. The synthetic color-tile sequence makes separately stored zoom levels visible. **This reproduces a captured map-display experience, not Google's complete application:** search, live traffic, Street View, routing and other online services are not reproduced.

### Creating maps that behave like they were online

**[Watch the offline zoomable-map video](https://www.youtube.com/watch?v=GjqZQIU8Ru0)**

[![Watch the offline zoomable-map video](https://img.youtube.com/vi/GjqZQIU8Ru0/hqdefault.jpg)](https://www.youtube.com/watch?v=GjqZQIU8Ru0)

This video focuses on the idea behind the project: modern users expect maps to pan, zoom, and reveal more detail as they move closer. It shows how QGIS-built multiresolution raster maps, MBTiles, TPKX conversion, and ArcGIS Earth can preserve that web-like zoomable-map experience completely offline.

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