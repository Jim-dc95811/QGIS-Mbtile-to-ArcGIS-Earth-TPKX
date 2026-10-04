# Master 4 Grid Maker

**Master 4 Grid Maker** is a companion utility for building repeatable offline-map coverage. Give it the four whole-degree edges of one 1° × 1° geographic master box and it creates a numbered visual reference grid plus a 100-line production manifest containing the exact QGIS-ready EPSG:3857 extent and deterministic TPKX filename for every sub-cell.

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

The TXT file contains exactly 100 production-manifest lines. Each line keeps the QGIS extent syntax and appends the deterministic TPKX filename:

```text
01 xmin,xmax,ymin,ymax [EPSG:3857] W082W081N031N030-001-GHY-Z20.tpkx
02 xmin,xmax,ymin,ymax [EPSG:3857] W082W081N031N030-002-GHY-Z20.tpkx
...
100 xmin,xmax,ymin,ymax [EPSG:3857] W082W081N031N030-100-GHY-Z20.tpkx
```

For the example Master 4, the first real line is:

```text
01 -9028010.7033,-9016878.7543,3503549.8435,3516410.3983 [EPSG:3857] W082W081N031N030-001-GHY-Z20.tpkx
```

### Deterministic TPKX filename

The current filename pattern is:

```text
W082W081N031N030-054-GHY-Z20.tpkx
```

It encodes the Master 4 **west edge, east edge, north edge, south edge**, then a three-digit cell number. Degree values are zero-padded to three digits, so the convention remains sortable and machine-readable worldwide. The current build appends the fixed production suffix `GHY-Z20`.

The cell label at the start of each text row remains `01` through `100`; the filename uses `001` through `100`. Because the filename is attached directly to its exact extent, cells can be selected and produced in any order without depending on a sequential batch-name rule.

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

![Master 4 decimal grid addressing](images/Master4_Grid_Maker_Overview.svg)

## Why EPSG:3857 output is calculated from decimal-degree boundaries

The reference system is defined geographically at exact tenth-degree boundaries. The program first determines those shared geographic edges, then transforms each edge with the standard Web Mercator equations into **EPSG:3857**.

It does **not** merely divide the projected Web Mercator Y distance into ten equal parts. That would not land on exact 0.1° latitude boundaries because Web Mercator Y is nonlinear with latitude.

This also means neighboring cells reuse the same calculated boundary coordinates, preventing gaps caused by independently drawn custom extents.

![Master 4 EPSG:3857 extent catalog](images/Master4_Grid_Maker_Extent_Catalog.svg)

## Typical QGIS workflow

1. Run **Master 4 Grid Maker** for the 1° master box covering the area you want.
2. Add the generated `_Grid.tif` to QGIS as a reference overlay.
3. Visually identify the numbered cell or cells covering the work area.
4. Use the matching row from the `_Extents.txt` production manifest: copy its exact extent into the QGIS batch job and use the appended deterministic filename for that cell. Cells can be chosen in any order; no sequential run is required.
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

For each valid case the generator produced exactly **100 manifest rows** and a **5000 × 5000 EPSG:3857 GeoTIFF with NoData=0**. The cell-54 decimal-address rule was specifically checked in all four hemisphere combinations. The new production filenames were checked for every row in every listed valid case, and the GeoTIFF output was byte-for-byte unchanged from the previous build.

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
SHA-256 e439100aae44245c7f5076724b001bc34159bcc57048fb58825ade3e8f3ccad2

Master4_Grid_Maker.bat
SHA-256 abb4e7dd1f1b665e1cf1b9ee4d1bffdef40e336acb746460640be0a043c20c2d

Master4_Grid_Maker.zip
SHA-256 a3143a22f2049ca8dc3698cc597566fe0788a4e6535554119cc08bcf7f275a97
```

The project's [MIT License](LICENSE) applies to the software and documentation.
