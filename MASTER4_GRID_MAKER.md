# Master 4 Grid Maker

**Master 4 Grid Maker** is a companion utility for building repeatable offline-map coverage. Give it the four whole-degree edges of one 1° × 1° geographic master box and it creates both a numbered visual reference grid and the exact QGIS-ready EPSG:3857 extents for all 100 sub-cells.

## Input

Run `Master4_Grid_Maker.bat` and enter the Master 4 in this exact order:

```text
west longitude, east longitude, south latitude, north latitude
```

Example:

```text
82w, 81w, 30n, 31n
```

The four edges must be whole degrees and must describe exactly one 1° × 1° box.

## Output

The program writes two files to **C:\downloads**. For the example above:

```text
Master4_82W_81W_30N_31N_Extents.txt
Master4_82W_81W_30N_31N_Grid.tif
```

The TXT file contains exactly 100 lines in QGIS extent syntax:

```text
01 xmin,xmax,ymin,ymax [EPSG:3857]
02 xmin,xmax,ymin,ymax [EPSG:3857]
...
100 xmin,xmax,ymin,ymax [EPSG:3857]
```

The GeoTIFF is a matching 5000 × 5000 numbered reference overlay in **EPSG:3857**. Its black background is tagged as NoData so only the grid and labels remain visible over a basemap in applications that honor the NoData value. The project owner has verified the generated reference overlay in both **QGIS** and **ArcGIS Earth**.

## The 01–100 addressing system

Every Master 4 box is subdivided into 100 geographic cells, each exactly **0.1° longitude × 0.1° latitude** before projection.

The cell number is designed so a latitude/longitude can reveal its sub-cell quickly:

- first decimal digit of the **absolute latitude** = tens row
- first decimal digit of the **absolute longitude**, plus 1 = column

For example, all four of these positions identify **cell 54**:

```text
30.56N, 81.34W -> 54
30.56N, 10.34E -> 54
30.56S, 81.34W -> 54
30.56S, 10.34E -> 54
```

The numbering reverses physical direction as needed in different hemispheres so the decimal lookup remains consistent worldwide.

![Master 4 decimal grid addressing](images/Master4_Grid_Maker_Overview.png)

## Why EPSG:3857 output is calculated from decimal-degree boundaries

The reference system is defined geographically at exact tenth-degree boundaries. The program first determines those shared geographic edges, then transforms each edge with the standard Web Mercator equations into **EPSG:3857**.

It does **not** merely divide the projected Web Mercator Y distance into ten equal parts. That would not land on exact 0.1° latitude boundaries because Web Mercator Y is nonlinear with latitude.

This also means neighboring cells reuse the same calculated boundary coordinates, preventing gaps caused by independently drawn custom extents.

![Master 4 EPSG:3857 extent catalog](images/Master4_Grid_Maker_Extent_Catalog.png)

## Typical QGIS workflow

1. Run **Master 4 Grid Maker** for the 1° master box covering the area you want.
2. Add the generated `_Grid.tif` to QGIS as a reference overlay.
3. Visually identify the numbered cell or cells covering the work area.
4. Use the matching numbered extent from the `_Extents.txt` file when creating or batch-producing the raster MBTiles.
5. Convert the finished compatible raster MBTiles to TPKX with this repository's `mb2tpkx.py` utility when ArcGIS Earth is the target viewer.

The same master and cell number can be regenerated later to check newer imagery or reproduce an exact coverage area.

## Windows use

Keep these two files together:

```text
Master4_Grid_Maker.py
Master4_Grid_Maker.bat
```

Requirements:

- Python 3
- Pillow

Install Pillow if needed:

```powershell
py -3 -m pip install Pillow
```

Double-click `Master4_Grid_Maker.bat`, enter the Master 4, and the program creates its two outputs in `C:\downloads`. The launcher waits for **any key to close** after completion.

A ready-to-use package is available here:

**[Download Master4_Grid_Maker.zip](Master4_Grid_Maker.zip)**

## Validation performed

The current hemisphere-aware build was programmatically tested with all of the following Master 4 inputs:

```text
82w,81w,30n,31n
10e,11e,30n,31n
82w,81w,31s,30s
10e,11e,31s,30s
1w,0e,0n,1n
0e,1e,1s,0n
179e,180e,84n,85n
180w,179w,85s,84s
```

For each valid case the generator produced exactly **100 extents** and a **5000 × 5000 EPSG:3857 GeoTIFF with NoData=0**. The cell-54 decimal-address rule was specifically checked in all four hemisphere combinations.

The program also rejected tested invalid inputs including non-whole-degree edges, a two-degree longitude span, latitude outside the practical Web Mercator limit, and invalid direction suffixes.

## Geographic scope and limits

The method is global **within the practical latitude coverage of EPSG:3857 / Web Mercator**. It does not cover the poles. Because the master grid is geographic, the physical ground area of a 0.1° × 0.1° cell changes with latitude; that is expected.

The utility:

- creates reference extents and a numbered GeoTIFF;
- does **not** download imagery;
- does **not** create MBTiles or TPKX itself;
- does **not** alter the existing MBTiles-to-TPKX converter.

## Current file checksums

```text
Master4_Grid_Maker.py
SHA-256 87bf15b15842ec37ba6ca6ff481275c4060cddfd14a91c054ce568f447c392e6

Master4_Grid_Maker.bat
SHA-256 abb4e7dd1f1b665e1cf1b9ee4d1bffdef40e336acb746460640be0a043c20c2d

Master4_Grid_Maker.zip
SHA-256 400b281bf8fb701e7bde263830db4815e5ac4cc0bae8ea66cb14592031ffc452
```

The project's [MIT License](LICENSE) applies to the software and documentation.
