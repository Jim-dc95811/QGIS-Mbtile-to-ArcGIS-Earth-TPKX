# MBTiles to TPKX

**Convert existing raster MBTiles from any compatible producer into native offline Esri TPKX, without an intermediate GeoTIFF or ArcGIS Pro export.**

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

## Verified scope and limits

- Input: standard **Web Mercator raster MBTiles**, TMS row convention, **256 × 256 PNG/JPEG** tiles at zoom levels **0–23** as implemented. Other formats and grids are not silently converted.
- Output: native Esri **Compact Cache V2 TPKX** with 128 × 128 indexed tile blocks.
- Source imagery bytes are preserved. A separate thumbnail is generated from a source tile; it is not used to replace or alter map imagery.
- Verified during development: exact-tile byte comparisons, multiple bundles at the same zoom level, ArcGIS Earth acceptance of the color and real-imagery demonstration packages, ArcGIS Pro acceptance of the Color 2B package, and a successful real MBTiles-to-TPKX run of the distributed script reported by the project owner in ArcGIS Earth.
- **Still to stress-test:** district-scale files, many bundles across several zoom levels, diverse MBTiles layouts, uneven multizoom coverage, failure recovery, and a separate ArcGIS Pro acceptance check for freshly generated output from the distributed script.

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

## Esri's published format documentation

This converter is an **independent implementation of publicly documented file formats**, not an attempt to reverse-engineer or circumvent a closed service. Esri itself maintains two public repositories directly relevant to this work:

- [Esri: Compact Cache V2 documentation and sample code](https://github.com/Esri/raster-tiles-compactcache). Esri describes how its raster tile bundles are structured and publishes an example Python implementation for building bundles from individual image tiles.
- [Esri: Tile Package Specification](https://github.com/Esri/tile-package-spec). Esri documents the TPKX container layout, tiling scheme, metadata, and Compact Cache V2 tile storage. Its repository explicitly recommends TPKX rather than the older TPK format, whose specification is not published.

Esri publishes the material in both repositories under the **Apache License 2.0**. These publications provide a clear technical basis for developers to study the formats and create interoperable tools such as this converter. We appreciate Esri making that work publicly available and acknowledge its authorship of the formats.

**Important distinction:** Publishing format documentation and sample code is not an endorsement of this particular project, nor does it grant rights to third-party imagery or waive the terms of any imagery or mapping service. The imagery-permissions statement above applies independently.

## Format references

- [Esri Compact Cache V2 technical description](https://github.com/Esri/raster-tiles-compactcache/blob/master/CompactCacheV2.md)
- [Esri tile package specification](https://github.com/Esri/tile-package-spec)
- [MBTiles 1.3 specification](https://github.com/mapbox/mbtiles-spec/blob/master/1.3/spec.md)

**Project status:** user-tested working conversion baseline, with additional testing and owner review pending. The public repository has **no software license yet**; see [LICENSE_STATUS.md](LICENSE_STATUS.md).
