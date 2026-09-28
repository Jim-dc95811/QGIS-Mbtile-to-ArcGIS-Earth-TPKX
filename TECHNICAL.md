# Technical continuity: MBTiles → Esri Compact Cache V2 TPKX

**Date:** 2026-09-27  
**Purpose:** preserve the exact reasoning, experimental sequence and technical constraints needed to maintain the working converter. This is an engineering handoff, not a new format specification.

## Verified result and its limits

Two native ArcGIS Pro TPKX files of substantially different sizes were analyzed as reference packages. Our first experimental TPKX files were rejected in ArcGIS Earth with a tiling-scheme/spatial-reference error. Merely declaring WKID 102100 / latestWkid 3857, or adopting approximately equivalent resolution values, did **not** solve it. After reproducing the known-good package's exact tiling values, JSON conventions, binary header fields and empty-index convention, the independently generated `Color_Mirror` package opened correctly in ArcGIS Earth. `Color_2B` then verified multiple bundles at the same zoom level, zoom 14–20, and acceptance in **both ArcGIS Earth and ArcGIS Pro**. Real Bryceville PNG imagery then displayed correctly in ArcGIS Earth from a directly built TPKX. The project owner subsequently reported success opening the first real MBTiles output from the distributed `mb2tpkx.py` script in ArcGIS Earth. This is not yet proof of all-dataset or all-application compatibility.

The earlier KML super-overlay architecture also worked in Google Earth but produced approximately 3–4-second navigation lockouts in ArcGIS Earth for the tested overlays. The same symptom appeared for locally linked and HTTP-delivered KML, and with synthetic color tiles without external internet. A 5,461-GroundOverlay flat KML was worse. Wireshark established fast local HTTP responses but did not directly identify ArcGIS Earth's internal bottleneck. The TPKX work *bypasses* this workload; it did not prove the root cause of the KML issue.

## Multi-gigabyte application test (2026-09-27)

The project owner supplied screenshots showing a completed conversion with the distributed script of `3-1-1_10.mbtiles` (**4,137,400 KB in Windows Explorer**, approximately 3.94 GiB) to `3-1-1_10.tpkx` (**4,108,022 KB**). A companion screenshot shows the resulting map open in **ArcGIS Earth**. The owner reports correct operation at the specific map scene associated with the original KML navigation problem.

This was the **first multi-gigabyte real-world input** tested with the distributed script. The observed TPKX size reflects the input tile bytes and packaging; it is not evidence of a general compression ratio. The original satellite imagery is not included in the public repository because its redistribution permissions have not been established. This particular package has **not** been separately documented as accepted by ArcGIS Pro, and neither full-district coverage nor all MBTiles variants have been fully validated.

## Large-package and source-JPEG/75 application tests (2026-09-27)

The project owner next used the **same distributed converter without code changes** on additional production grid datasets. Explorer screenshots recorded the following sizes (Windows-displayed KB):

| Input run | MBTiles size | Converted TPKX size | Reported application evidence |
| --- | ---: | ---: | --- |
| `Master Grid 3-1 z20`, PNG tiles | 39,891,100 KB | 39,587,335 KB | Package loaded in ArcGIS Earth; owner reports responsive offline navigation, immediate display and no noticeable zoom-time pixelation |
| `Master Grid 3-2 z20 jpg`, JPEG/75 tiles | 4,354,360 KB | 4,090,206 KB | Package loaded in ArcGIS Earth; owner supplied screenshots showing detailed Z20 hybrid graphics and legible labels |

The observed JPEG/75 run was roughly **9.2× smaller at the MBTiles stage** and **9.7× smaller at the TPKX stage** than the reported PNG run (approximately 89–90% smaller). They were **different production grids**, not a controlled encode of the exact same pixels and tile inventory. The large difference strongly motivates a controlled same-source comparison, but these two files alone cannot establish a universal JPEG/75 compression factor or equivalent pixel-level fidelity. Viewer responsiveness is based on the owner's interactive observations, not frame-time benchmarks.

**Mechanism:** The JPEG/75 setting belongs to the *MBTiles-producing application*. This converter copies each accepted source JPEG or PNG tile **byte-for-byte** into Esri Compact Cache V2 bundles. It does not invoke JPEG compression, regenerate the zoom pyramid, resample cartography, or change the verified binary packaging logic. A source format change therefore required **zero changes** to `mb2tpkx.py` or `mb2tpkx.bat`.

The screenshots and owner observations constitute a successful, substantial **~40 GB-class field test** plus a smaller, visually inspected JPEG/75 test. They do **not** establish maximum file size, tolerance for every MBTiles producer, equivalent image quality for all imagery, or formal compatibility certification. Preserve representative map tiles and exact inventories privately if a future controlled PNG/JPEG comparison is needed. Do not commit third-party imagery without permission.

## Conversion invariants

1. **No imagery transformation.** Copy each input tile's exact PNG or JPEG bytes. Do not stitch, resample, recolor or recompress. A separate `thumbnail.png` can be generated for package presentation.
2. **Coordinate direction.** Standard MBTiles stores TMS `tile_row` from the bottom. Convert to Esri XYZ row with `row = (2**z - 1) - tile_row`. Preserve column and zoom.
3. **Bundle partitioning.** For each zoom, group tiles into blocks of **128 × 128**: `bundle_row = (xyz_row // 128)*128`, `bundle_col = (column // 128)*128`. Emit `tile/L{zoom:02d}/R{bundle_row:04x}C{bundle_col:04x}.bundle` as the reference packages do.
4. **Index.** Each bundle contains **16,384 eight-byte entries**. The accepted references use the integer `4` for absent tiles. For a populated tile, `entry = (image_length << 40) | image_offset` and the stored image is preceded by its four-byte length. Check bounds and source-byte round trips.
5. **Bundle header.** Mirror the known-good 64-byte header, changing the file-length field at byte offset **24** and the observed image-size-related field at byte offset **8**. Across inspected reference bundles the latter equaled `max(131092, largest_stored_image_size)`. Do not replace the reference's byte-4 and byte-48 fields with superficially equivalent values taken from generic documentation; that was one of the differences observed in rejected experiments. *These are empirical compatibility observations, not a universal guarantee.*
6. **Tiling scheme.** Copy the tested ArcGIS Pro `root.json` Web Mercator tile origin, level resolutions and scales exactly. Do not substitute recalculated values that differ in the last few decimals: our first packages did so and ArcGIS Earth rejected them. The origin in the reference is X = -20037508.342787 and Y = 20037508.342787.
7. **Package structure.** The verified package includes `iteminfo.json`, `root.json`, `thumbnail.png`, and `tile/Lxx/*.bundle`. Keep their proven ZIP packaging conventions. The zero-byte `.bundle.done` marker seen in a separate cache directory was **not** required in our accepted TPKX.
8. **Extent and zoom metadata.** Compute extents from source tile coordinates with the reference tiling scheme. Advertise source min/max zooms. Current script uses the finest available zoom to set the package display extent; validate uneven multizoom geographic coverage before claiming generality.

## Known-working baselines and identities

- **mb2tpkx.py SHA-256**: `c04dc9f3c1ad74b4180b11465df1189a74c500a5d5873d66a57c2d4076fb3670`
- **mb2tpkx.bat SHA-256**: `078e07834b6fa45f8e63192f60033ac5c322ea236372df22cece8be8a24fda66`
- **mb2tpkx.zip SHA-256**: `76c8fbf9eae534db8e79a9ad0768ea30b9327cd69406b4d2ec064ed9c276acb7`
- Color 2B accepted demonstration SHA-256: `f5c9d8b7976290d2a63b010ecab0a6d7bf9129ff388718a41a350a78a415400a`
- Bryce accepted demonstration SHA-256: `f33bf93e9a655e7b7fbefa55cc10138bb845a2d2860b4145d29c4eafe0c2699d`

**Do not commit actual commercial satellite imagery, proprietary reference packages or user Wireshark traffic without explicit permission.** Hashes allow private reference packages to be identified without redistributing them.

## Regression requirements

Preserve the verified Python and BAT files until a narrowly specified code change is needed; change one functional behavior at a time. Before publishing a changed converter, verify every tile's output bytes against the input, run a multiple-bundle test, compare JSON and bundle header/index invariants, and obtain acceptance of the **exact newly generated output** in ArcGIS Earth and ideally ArcGIS Pro. A GDAL reader accepting a package is useful but was **not sufficient**: GDAL opened some early TPKX files that ArcGIS Earth rejected.

The current script is a **CLI with a Windows BAT launcher, not a GUI application**. It processes one bundle at a time, rejects an existing destination file, and validates tile dimensions and image signatures. Known work remains for inputs larger or more complex than the owner-reported ~40 GB test, interrupted runs, unusual MBTiles layouts, spatially uneven zoom coverage, and mixed-format metadata.

## Technical references

- [Esri Compact Cache V2](https://github.com/Esri/raster-tiles-compactcache/blob/master/CompactCacheV2.md)
- [Esri TPKX specification](https://github.com/Esri/tile-package-spec/blob/master/README.md)
- [MBTiles 1.3](https://github.com/mapbox/mbtiles-spec/blob/master/1.3/spec.md)

**Scope and attribution:** Esri created Compact Cache V2. This project developed and validated a direct byte-preserving conversion workflow and its empirically tested compatibility packaging. No technical method changes the source imagery's license terms.
