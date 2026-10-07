# Technical continuity: raster MBTiles -> Esri Compact Cache V2 TPKX + Master 4 v3

**Updated:** 2026-10-07  
**Purpose:** preserve the technical invariants, field-test boundaries and current Master 4 behavior needed to maintain the project without re-opening solved problems.

## 1. Direct MBTiles -> TPKX converter: verified architecture

The converter was developed by comparing known-good ArcGIS Pro TPKX packages and Esri's published Compact Cache V2 / tile-package specifications. Early experimental packages could be opened by some generic readers but were rejected by ArcGIS Earth until the package matched the known-good tiling metadata, bundle/index conventions and JSON structure closely enough.

The working converter then passed synthetic multi-bundle tests and real-image tests. Large real outputs have since been used interactively in ArcGIS Earth.

### Conversion invariants

1. **No imagery transformation.** Copy each accepted source PNG/JPEG tile byte-for-byte. Do not stitch, resample, recolor or recompress source tiles. A separate package thumbnail may be generated.
2. **TMS -> XYZ rows.** Standard MBTiles `tile_row` is reversed with `xyz_row = (2**z - 1) - tile_row`.
3. **128 x 128 bundles.** Group Esri XYZ coordinates into Compact Cache V2 128 x 128 tile blocks.
4. **Bundle index.** Each bundle has 16,384 eight-byte index entries. The verified missing-tile sentinel is integer `4`; populated entries encode image length and image offset.
5. **Known-good header.** Preserve the empirically validated 64-byte bundle header template and update only content-dependent fields used by the working implementation.
6. **Known-good tiling scheme.** Preserve the tested Web Mercator origin/resolution/scale values exactly; do not substitute newly rounded/recalculated values without target-viewer regression testing.
7. **Package structure.** `iteminfo.json`, `root.json`, `thumbnail.png`, and `tile/Lxx/*.bundle` are the proven package members.
8. **Extent/zoom metadata.** Derive extents from source tile coordinates and advertise the stored zoom range.

### Converter baseline identities

- `mb2tpkx.py` SHA-256: `c04dc9f3c1ad74b4180b11465df1189a74c500a5d5873d66a57c2d4076fb3670`
- `mb2tpkx.bat` SHA-256: `078e07834b6fa45f8e63192f60033ac5c322ea236372df22cece8be8a24fda66`
- known GitHub blob SHA for Python before the current Master 4-only update: `87ccc955944b994ad156f25488d04df9197184bd`
- known GitHub blob SHA for BAT: `267240f9f9f634ac3d8f66bf3f93f9374973372b`

Do not casually refactor the converter. A generic reader accepting output is useful but is not a substitute for ArcGIS Earth acceptance.

## 2. Real-world converter test record

Owner-reported, screenshot-supported field tests include:

| Test | MBTiles | TPKX | Observed result |
| --- | ---: | ---: | --- |
| First large real input | 4,137,400 KB | 4,108,022 KB | Opened and navigated in ArcGIS Earth |
| Z20 PNG production grid | 39,891,100 KB | 39,587,335 KB | Responsive ArcGIS Earth viewing reported |
| Separate JPEG/75 production grid | 4,354,360 KB | 4,090,206 KB | Detailed hybrid map displayed in ArcGIS Earth |
| Jacksonville Metro Z20 JPEG/75 | 21,786,032 KB | 20,629,591 KB | Large single-file metro map displayed in ArcGIS Earth |

The PNG and JPEG examples are different grids. They do **not** establish a universal same-source compression ratio or identical visual fidelity. JPEG quality is selected upstream in the MBTiles producer; the converter itself does not recompress the tiles.

Do not claim the large real packages were ArcGIS Pro-tested unless separately verified there. Synthetic compatibility work did include ArcGIS Pro acceptance.

## 3. Master 4 standard production geometry

Master 4 defines one whole-degree geographic box in:

```text
west, east, south, north
```

Example:

```text
82w, 81w, 30n, 31n
```

The box is divided into 100 exact geographic cells, each 0.1 degree x 0.1 degree before projection. Web Mercator X/Y values are calculated from the exact geographic tenth-degree boundaries; projected Y is not naively divided into equal pieces.

### Cell addressing

The cell number uses the first decimal digit of absolute latitude as the tens row and the first decimal digit of absolute longitude plus one as the column. Truncate; do not round.

This addressing rule is implemented hemisphere-aware so it remains consistent in W/N, E/N, W/S and E/S Master 4 boxes.

### Standard v3 outputs

The program writes:

```text
Master4_<box>_Extents.txt
Master4_<box>_Grid.tif
```

The TXT contains 100 production rows plus a final full-parent row:

```text
MASTER xmin,xmax,ymin,ymax [EPSG:3857]
```

Example for 82W-81W / 30N-31N:

```text
MASTER -9128198.2450,-9016878.7543,3503549.8435,3632749.1434 [EPSG:3857]
```

The numbered GeoTIFF is 5000 x 5000, EPSG:3857, with background NoData=0.

Current production filename pattern:

```text
W082W081N031N030-055-GHY-Z20.tpkx
```

## 4. Master 4 v3 optional Cell 55 Z10-Z20 TPKX

### User-facing behavior

The optional package is generated only after the standard TXT and GeoTIFF are complete. Prompt:

```text
Create Cell 55 colored zoom-demo TPKX (Z10-Z20)? [y/N]:
```

No is the default. Enter/N skips the demo without affecting standard output. Y/Yes creates a file such as:

```text
W082W081N030N029-055-ZOOM-DEMO.tpkx
```

### Format behavior

The v3 generator uses the same verified Compact Cache V2 structural conventions as the converter's TPKX work, but it manufactures synthetic PNG tiles rather than reading MBTiles.

- target cell: fixed Cell 55
- stored zooms: Z10-Z20
- tile size: 256 x 256 PNG
- color/label: unique color per zoom, large `Zxx`, smaller `CELL 55`
- Esri bundle packet size: 128
- output: ZIP64-capable TPKX with `iteminfo.json`, `root.json`, `thumbnail.png`, and `tile/Lxx/*.bundle`
- existing output: not overwritten

### Coarse-zoom footprint nuance

The package chooses every standard global XYZ tile that intersects Cell 55. It does **not** clip the colored raster within edge tiles.

At coarse zooms, one XYZ tile is larger than a 0.1-degree Master 4 cell. Therefore colored coverage can extend beyond the exact Cell 55 geographic boundary. This is expected and is why the demo must be described as a teaching/geographic sanity tool rather than an exact boundary raster.

The exact cell extent remains authoritative in the Master 4 manifest and GeoTIFF.

### Current v3 identities

- `Master4_Grid_Maker.py` SHA-256: `16a42784005743728837d3dfdc2f3295b30071d5ed37ccbddbb9b9ee23e58888`
- `Master4_Grid_Maker.bat` SHA-256: `abb4e7dd1f1b665e1cf1b9ee4d1bffdef40e336acb746460640be0a043c20c2d`
- `Master4_Grid_Maker.zip` SHA-256: `408ba3e129f912b3b4ef0a7df0d6ccc478ff8935ffec9cb235232505e872e158`

## 5. v3 validation boundary

Before delivery, the standard Master 4 TXT and GeoTIFF behavior was regression-checked against the prior build across representative hemisphere/boundary cases. The demo TPKX package structure, bundle indexes, tile counts, metadata and PNG members were checked programmatically.

The project owner then performed the target-viewer acceptance test on Windows:

- generated a Cell 55 Z10-Z20 package;
- opened it successfully in ArcGIS Earth;
- supplied screenshots showing visible stored-level transitions at Z12, Z13, Z14, Z15, Z17 and Z20;
- reported the resulting TPKX at roughly 1 GB.

This is the field evidence for the current v3 feature. The exact v3 teaching package has not been separately documented as accepted by ArcGIS Pro, so do not claim that.

## 6. Operational interpretation

A practical ArcGIS Earth library can use:

- **area-wide Z17 TPKX** for overview context;
- **Master 4 GeoTIFF** for cell identification;
- **high-resolution production TPKX cells** for detail;
- **optional Cell 55 synthetic TPKX** for teaching, TPKX sanity checking, and offline geographic/zoom reference.

The owner observed that opening the local synthetic package while offline restores a known geographic anchor and obvious zoom-level feedback when familiar online basemap context is unavailable.

**Production rule:** reference overlays ON while planning; OFF before production.

## 7. Historical route that should not be restarted without a new reason

The project previously explored KML SuperOverlay approaches. Google Earth handled them well, but tested ArcGIS Earth KML navigation showed multi-second delays. Local HTTP delivery and synthetic tile experiments did not eliminate the behavior. TPKX bypassed the problem and became the successful native offline route.

Do not restart KML work or rewrite the working converter merely because another representation is theoretically possible. Any new change should answer a specific user need and preserve known-good behavior.

## 8. Regression requirements

### Converter

Before publishing a converter change:

- verify source tile bytes survive unchanged;
- verify TMS -> XYZ coordinates;
- run multi-bundle tests;
- inspect bundle indexes/headers and JSON metadata;
- obtain acceptance of the exact new output in ArcGIS Earth;
- ideally test ArcGIS Pro separately before claiming Pro compatibility.

### Master 4

Before publishing a Master 4 change:

- compare standard TXT rows against the previous build;
- verify the final `MASTER` full-box row;
- compare GeoTIFF georeferencing/appearance;
- verify hemisphere/boundary behavior for geometry-related changes;
- verify the opt-out path does not create a TPKX;
- verify the opt-in demo TPKX structure;
- obtain ArcGIS Earth acceptance for TPKX-related changes.

## 9. Technical references

- [Esri Compact Cache V2](https://github.com/Esri/raster-tiles-compactcache/blob/master/CompactCacheV2.md)
- [Esri TPKX specification](https://github.com/Esri/tile-package-spec/blob/master/README.md)
- [MBTiles 1.3](https://github.com/mapbox/mbtiles-spec/blob/master/1.3/spec.md)

**Scope and attribution:** Esri created Compact Cache V2 and the TPKX specification. This project developed and field-tested its direct conversion/manufacturing workflow. No technical method changes the source imagery's license terms.
