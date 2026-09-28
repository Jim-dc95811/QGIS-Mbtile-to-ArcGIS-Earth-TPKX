# MBTiles to TPKX

**Convert existing raster MBTiles from any compatible producer into native offline Esri TPKX, without an intermediate GeoTIFF or ArcGIS Pro export.**

**Latest field results (September 27, 2026):** the owner reports smooth offline navigation of a roughly 40 GB-class converted TPKX; a separate JPEG/75 production grid yielded a much smaller package with visually clear Z20 hybrid cartography. See [test figures and important comparison limits](#larger-file-field-tests-and-jpeg75-milestone-2026-09-27).

The converter copies each source PNG or JPEG tile **byte-for-byte**, maps MBTiles TMS tile addresses into Esri's tile grid, writes indexed Compact Cache V2 `.bundle` files, and packages them as a `.tpkx` file. It does not change the imagery, invent missing zoom levels, resample pixels, or improve source resolution.

## Why this exists

Raster MBTiles may come from any compatible map-making software. Previously, this project's ArcGIS Earth workflow involved extra raster conversion and ArcGIS Pro processing, or KML super-overlays that experienced substantial navigation delays in ArcGIS Earth. A directly generated TPKX uses the application's native offline tile-package path instead.

The breakthrough was achieved by comparing two **working ArcGIS Pro-generated TPKX references** against experimental packages, correcting their metadata and binary bundle layout until the new packages worked in ArcGIS Earth. The multi-bundle colored diagnostic TPKX was also accepted by ArcGIS Pro. The project owner has now confirmed that an MBTiles file converted with the distributed script works very well in ArcGIS Earth.

This demonstrates a usable conversion route; it is not a claim that every possible MBTiles source, output size, or GIS application has been validated.

## Download and use

Use **Code → Download ZIP** on this repository, extract it, and keep these two files together:

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

## Real-world conversion milestone (2026-09-27)

The project owner successfully ran the **distributed Python converter** against a much larger MBTiles imagery dataset, not just the synthetic and small real-imagery test packages:

- Input: `3-1-1_10.mbtiles`, **4,137,400 KB** as displayed in Windows Explorer (approximately 3.94 GiB).
- Output: `3-1-1_10.tpkx`, **4,108,022 KB** as displayed in Windows Explorer.
- Application check: the resulting package loaded and displayed in **ArcGIS Earth**, including a map location where the earlier KML super-overlay workflow had exhibited slow navigation. The owner reported that the converted package worked correctly there.

This is a **reported, screenshot-supported application test of a multi-gigabyte conversion**, rather than an independent reproduction on the maintainer's computer. It does not establish universal large-dataset compatibility, offline operational certification, or ArcGIS Pro acceptance of this particular file. The imagery and project screenshots are not redistributed here.

## Larger-file field tests and JPEG/75 milestone (2026-09-27)

The project owner subsequently tested the **unchanged converter** with much larger real-world raster MBTiles and reported responsive offline navigation in ArcGIS Earth. Windows Explorer screenshots supplied these file sizes:

| Production run | Input MBTiles | Converted TPKX | Observed viewer result |
| --- | ---: | ---: | --- |
| Master Grid 3-1 Z20, PNG source tiles | 39,891,100 KB | 39,587,335 KB | Loaded in ArcGIS Earth; owner reports very responsive navigation and immediate screen display |
| Master Grid 3-2 Z20, JPEG quality 75 source tiles | 4,354,360 KB | 4,090,206 KB | Loaded in ArcGIS Earth; screenshot shows detailed hybrid cartography and legible Z20 labels |

These are **different grid runs**, although the owner reports comparable grid dimensions/coverage. Their displayed sizes differ by approximately **9.2× for MBTiles** and **9.7× for TPKX** (roughly 89–90% smaller in the JPEG/75 run). This is an important *production observation*, **not** a controlled PNG-versus-JPEG experiment using byte-identical source imagery, an independently confirmed identical tile inventory, or a measured image-fidelity benchmark.

**The JPEG/75 choice is made upstream when creating the MBTiles.** The converter already accepts PNG or JPEG and copies every source map tile's image bytes unchanged into the TPKX. It performs **no JPEG conversion or extra compression**; neither the Python script nor the Windows launcher required modification for this result.

The owner reports that the large PNG package remained highly responsive during zooming and that the JPEG/75 output retained visually clear, zoom-dependent Google Hybrid road labels and graphics. These are owner-reported, screenshot-supported ArcGIS Earth observations, not a measured performance comparison or proof that JPEG/75 will preserve every source equally well. For mixed text/graphics, transparency, and different imagery types, producers should inspect their own results before choosing an output image format.

These packages are **not included** in the repository; rights and redistribution requirements for their imagery have not been established.

## Verified scope and limits

- Input: standard **Web Mercator raster MBTiles**, TMS row convention, **256 × 256 PNG/JPEG** tiles at zoom levels **0–23** as implemented. Other formats and grids are not silently converted.
- Output: native Esri **Compact Cache V2 TPKX** with 128 × 128 indexed tile blocks.
- Source imagery bytes are preserved. A separate thumbnail is generated from a source tile; it is not used to replace or alter map imagery.
- Verified during development: exact-tile byte comparisons, multiple bundles at the same zoom level, ArcGIS Earth acceptance of the color and real-imagery demonstration packages, ArcGIS Pro acceptance of the Color 2B package, and a successful real MBTiles-to-TPKX run of the distributed script reported by the project owner in ArcGIS Earth.
- **Still to validate:** full district-scale coverage, independently repeated large-file tests, diverse MBTiles producers/layouts, uneven multizoom coverage, failure recovery, and a separate ArcGIS Pro acceptance check for freshly generated output from the distributed script. The owner-reported ~40 GB success is a substantial field test, not a universal maximum-size guarantee.

See [TECHNICAL.md](TECHNICAL.md) for architecture, failure history, byte-level findings, and reproducibility notes.

## Project policies and release status

- [LEGAL.md](LEGAL.md) — imagery rights, attribution limitations, trademarks, agency approval, lack of affiliation and operational-use cautions.
- [CREDITS.md](CREDITS.md) — Esri's public specifications and licenses, the MBTiles format, Pillow, Python and QGIS acknowledgments.
- [LICENSE_STATUS.md](LICENSE_STATUS.md) — **no project software license has been granted yet**; the authorized owner must resolve ownership and choose one.
- [CONTRIBUTING.md](CONTRIBUTING.md) — safe contributions, source provenance and reproducible test expectations.
- [SECURITY.md](SECURITY.md) — how to request private reporting without posting sensitive material publicly.
- [RELEASE_CHECKLIST.md](RELEASE_CHECKLIST.md) — owner review and testing required before broader claims or redistribution.

No imagery datasets, proprietary example tile packages or agency data are intentionally included. References to QGIS, Esri or other providers are descriptive and are not claims of affiliation, sponsorship or official certification.

## Respect for imagery providers and their rights

This is an independent, noncommercial **file-format conversion project** motivated by public-safety and offline-mapping needs. We appreciate the technology and imagery made available by GIS software developers, imagery providers, and the wider mapping community. **We respect imagery providers' copyrights, licenses, terms of service, attribution requirements, and decisions about permitted uses.**

The converter does not download imagery, bypass provider access controls, intentionally edit embedded watermarks, or grant permission to store or redistribute anyone's data. It converts an MBTiles file the user already has, copying its image tiles without altering them. **Attribution limitation:** the current version transfers the MBTiles dataset name but does not automatically carry over separate MBTiles attribution metadata, service credits, or license notices into the TPKX. Users must preserve and display any credits required by their imagery providers when using or sharing the resulting maps. **Users are responsible for ensuring they have the appropriate rights or permission** for the imagery they acquire, convert, retain offline, use, or share; noncommercial or emergency-service intent does not, by itself, establish those permissions.

Technical access through QGIS or another viewer does not automatically authorize bulk downloading, offline retention, or redistribution. Check the specific provider's applicable terms or obtain permission where necessary; for example, consult [Google Maps/Google Earth terms](https://www.google.com/help/terms_maps/) and [Google Map Tiles API policies](https://developers.google.com/maps/documentation/tile/policies) for relevant Google services.

This project is **not affiliated with or endorsed by QGIS, Google, Esri, or any imagery provider**, unless such a relationship is expressly documented. Our work concerns interoperability between published file formats, not ownership of the imagery those formats can contain.

## Publicly documented formats: Mapbox MBTiles and Esri TPKX

**Both ends of this conversion are publicly documented, and neither format requires a particular map-making application.** This project reads compatible raster MBTiles made by any producer and independently writes Esri's Compact Cache V2 TPKX format. It does not check which program originally created the MBTiles.

**Input — Mapbox's [MBTiles specification](https://github.com/mapbox/mbtiles-spec).** Mapbox publicly maintains the open MBTiles format for tiled map data. Its official README explicitly says use of the specification in products and code is free, with no royalties, restrictions or requirements. The *text of the specification* has its own [Creative Commons Attribution license](https://github.com/mapbox/mbtiles-spec); the right to implement the format is distinct from republishing the specification text. MBTiles is **not owned by QGIS**.

**Output — Esri's published specifications and example code:**

- [Esri Compact Cache V2](https://github.com/Esri/raster-tiles-compactcache): publicly documents the bundle format and supplies example Python code for constructing bundles from image tiles.
- [Esri Tile Package Specification](https://github.com/Esri/tile-package-spec): publicly documents the TPKX container, metadata, tiling scheme and Compact Cache V2 tile storage, and recommends TPKX instead of the older TPK format.

Esri publishes those two repositories under **Apache License 2.0** and invites contributions to its TPKX specification repository. Together with Mapbox's implementation-friendly MBTiles specification, these publications establish a documented technical basis for independent interoperability tools. We credit both organizations for publishing the respective formats; neither organization is claimed to endorse or participate in this project.

**Format openness is not imagery permission.** Neither specification grants rights to download, cache, convert, display offline or redistribute Google, Esri or other providers' map imagery. Those activities remain governed by the applicable provider terms and permissions, as explained above. The project code also has its own separate [pending license decision](LICENSE_STATUS.md).

## Format references

- [Esri Compact Cache V2 technical description](https://github.com/Esri/raster-tiles-compactcache/blob/master/CompactCacheV2.md)
- [Esri tile package specification](https://github.com/Esri/tile-package-spec)
- [MBTiles 1.3 specification](https://github.com/mapbox/mbtiles-spec/blob/master/1.3/spec.md)

**Project status:** user-tested working conversion baseline, with additional testing and owner review pending. The public repository has **no software license yet**; see [LICENSE_STATUS.md](LICENSE_STATUS.md).
