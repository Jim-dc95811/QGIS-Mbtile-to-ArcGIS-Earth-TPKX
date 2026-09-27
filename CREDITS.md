# Upstream specifications, tools, and acknowledgments

This project appreciates the authors and communities that make interoperable mapping possible. **Being listed here does not imply endorsement or a project partnership.** Licenses on specifications or software do not grant rights to the imagery users convert.

| Resource | Role in this project | Published upstream terms |
| --- | --- | --- |
| [Esri Compact Cache V2](https://github.com/Esri/raster-tiles-compactcache) | Published bundle-file specification and example code; format authored by Esri | [Apache License 2.0](https://github.com/Esri/raster-tiles-compactcache/blob/master/LICENSE.TXT) |
| [Esri tile-package-spec](https://github.com/Esri/tile-package-spec) | Published TPKX structure and metadata description | [Apache License 2.0](https://github.com/Esri/tile-package-spec/blob/master/license.txt) |
| [Mapbox MBTiles specification](https://github.com/mapbox/mbtiles-spec) | Documentation for the raster MBTiles input format | [Specification text: CC BY 3.0 US; implementation use unrestricted per upstream README](https://github.com/mapbox/mbtiles-spec) |
| [Pillow](https://pillow.readthedocs.io/en/stable/about.html#license) | Python image library installed separately by the user; used to inspect input images and create a thumbnail | MIT-CMU |
| [Python](https://www.python.org/) | Runtime and standard-library SQLite, ZIP, and binary-file support | [Python license](https://docs.python.org/3/license.html) |
| [QGIS](https://qgis.org/) | Optional upstream GIS tool for authoring the input MBTiles; **not bundled** in this repository | [Project and license information](https://qgis.org/) and [brand guidelines](https://www.qgis.org/community/organisation/guidelines/) |
| [ArcGIS Earth and ArcGIS Pro](https://www.esri.com/) | Independently tested viewers of TPKX output; **not bundled** | Respective product/service terms apply |

## What is actually included

Only this project's Python script, BAT launcher and documentation are committed. Pillow, QGIS, ArcGIS software, upstream sample repositories, imagery datasets and upstream sample caches are **not** bundled here. The converter includes empirically established TPKX metadata values and a template bundle header derived during compatibility work with ArcGIS Pro-produced files; no independently verified conclusion has been made about whether future use of additional upstream implementation code would trigger separate license notice obligations.

If upstream example code or content is deliberately copied in a future contribution, identify the exact source and version and preserve all required copyright, license and modification notices. Do not assume that citing a public GitHub page alone fulfills those obligations.

This document records format and dependency credits. Image copyright and attribution depend on **each user's input data** and must be handled separately; see [LEGAL.md](LEGAL.md).
