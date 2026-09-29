# Watch the result, then make your own map

## The public demonstration

**[Google Maps OFFLINE — The Impossible Is Now Possible!](https://www.youtube.com/watch?v=8uziJNzan1g)**

[![Watch the demonstration on YouTube](https://img.youtube.com/vi/8uziJNzan1g/hqdefault.jpg)](https://www.youtube.com/watch?v=8uziJNzan1g)

The demonstration compares familiar online Street and Hybrid map displays with independently prepared offline imagery viewed in **ArcGIS Earth**, and uses colored tiles to show how stored imagery can change by zoom level. It illustrates a **map-display** experience, not a duplicate of Google Maps' search, routing, Street View or online services.

## Follow-along tutorial: make your own offline map

**[How to Make an Offline Map with QGIS and ArcGIS Earth](https://www.youtube.com/watch?v=C71n8TAByuE)**

[![Watch the Washington, DC QGIS and ArcGIS Earth tutorial](https://img.youtube.com/vi/C71n8TAByuE/hqdefault.jpg)](https://www.youtube.com/watch?v=C71n8TAByuE)

The published Washington, DC video follows the actual production route: QGIS creates MBTiles, the Python converter turns the file into TPKX, and ArcGIS Earth opens the finished map.

## Illustrated workflow

![Four players: imagery source, QGIS MBTiles production, Python MBTiles-to-TPKX converter, and ArcGIS Earth](images/ChatGPT%20Image%20Sep%2027%2C%202026%2C%2010_58_45%20PM.png)

The demonstration's companion artwork illustrates the same conversion route:

![MBTiles-to-TPKX converter breakthrough artwork](images/ChatGPT%20Image%20Sep%2027%2C%202026%2C%2012_44_11%20PM.png)

## The four players

```mermaid
flowchart LR
  A[Imagery provider] --> B[Compatible raster MBTiles producer]
  B -->|MBTiles| C[Our Python converter]
  C -->|TPKX| D[ArcGIS Earth — offline viewer]
```

**1. Source imagery.** Choose an imagery provider and obtain the permissions required for your particular acquisition, caching, conversion, offline use, display and distribution. This project does not fetch or authorize any provider's imagery.

**2. Produce MBTiles.** QGIS's **Generate XYZ Tiles (MBTiles)** is the project's example route. Other producers can also work if their output meets the converter's supported raster MBTiles requirements. For photographic sources, JPEG/75 can greatly reduce the size of some MBTiles datasets; check legibility and visual fidelity for the source actually used.

**3. Convert with Python.** Download this project's `mb2tpkx.py` and `mb2tpkx.bat` as described in [README.md](README.md). The converter preserves input PNG/JPEG tile bytes and constructs native indexed TPKX bundles. It does not independently reproduce a map service's live rendering engine.

**4. View offline.** Open the resulting TPKX in ArcGIS Earth. The video illustrates locally stored zoom-specific cartography. Actual availability of GPS positioning, terrain profiles and other application features depends on the particular device and separately configured datasets.

## The colored-tile explanation

The synthetic demonstration is deliberately **not** commercial map imagery. Each stored zoom level has different colors and large level numbers. When the viewer switches between those levels, the change becomes obvious. The original test package was constructed for the Jacksonville experiment and was opened successfully by the project owner in ArcGIS Earth.

The source content must genuinely include different tiles at those zooms for the resulting map to reproduce different labels and other cartographic states. The converter **does not create the differences**: it preserves the tiles that the map maker supplied.

## Start with one map

The Washington, DC tutorial linked above is the beginner follow-up to the Jacksonville demonstration. It shows the practical QGIS → MBTiles → Python → TPKX → ArcGIS Earth route. District-scale production and complex geographic splitting are separate advanced topics.

[Return to the converter](README.md) · [Full technical record](TECHNICAL.md) · [Source-data rights and attribution](LEGAL.md)
