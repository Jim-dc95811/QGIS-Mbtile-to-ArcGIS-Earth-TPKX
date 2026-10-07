# Upstream specifications, tools, and acknowledgments

This project appreciates the authors and communities that make interoperable mapping possible. **Being listed here does not imply endorsement or a project partnership.** Licenses on specifications or software do not grant rights to imagery users convert.

| Resource | Role in this project | Published upstream terms |
| --- | --- | --- |
| [Esri Compact Cache V2](https://github.com/Esri/raster-tiles-compactcache) | Published bundle-file specification and format reference used by the converter and synthetic Master 4 demo TPKX | [Apache License 2.0](https://github.com/Esri/raster-tiles-compactcache/blob/master/LICENSE.TXT) |
| [Esri tile-package-spec](https://github.com/Esri/tile-package-spec) | Published TPKX structure/metadata description | [Apache License 2.0](https://github.com/Esri/tile-package-spec/blob/master/license.txt) |
| [Mapbox MBTiles specification](https://github.com/mapbox/mbtiles-spec) | Documentation for the raster MBTiles input format | [Specification information](https://github.com/mapbox/mbtiles-spec) |
| [Pillow](https://pillow.readthedocs.io/en/stable/about.html#license) | Python image library installed separately by the user; used for tile/image inspection, thumbnails, GeoTIFF drawing and the synthetic color-demo tiles | MIT-CMU |
| [Python](https://www.python.org/) | Runtime and standard-library SQLite, ZIP, binary-file and math support | [Python license](https://docs.python.org/3/license.html) |
| [QGIS](https://qgis.org/) | Optional GIS tool for authoring production MBTiles; not bundled | [Project information](https://qgis.org/) |
| [ArcGIS Earth and ArcGIS Pro](https://www.esri.com/) | Target/test viewers for TPKX output; not bundled | Respective product/service terms apply |

## Human-AI project collaboration

**Jim Gaddy** conceived and directed the project, supplied real-world engineering requirements, conducted the mapping experiments and field-tested the output. **OpenAI's ChatGPT** served as the AI-assisted coding, research, regression, illustration and documentation collaborator.

The project owner elected to distribute the software under the [MIT License](LICENSE). This acknowledgment is not a claim of OpenAI sponsorship or endorsement and does not affect third-party code, software, specification or imagery rights.

## What is included

This repository contains the project's Python scripts, Windows launchers, ZIP packages, MIT License, written documentation, PDF manuals and project-created illustrations. Pillow, QGIS, ArcGIS software, upstream sample repositories and commercial imagery datasets are not bundled.

The optional Master 4 Cell 55 Z10-Z20 demonstration TPKX is generated locally by the script from **synthetic project-created colored tiles**. The repository does not need to distribute a giant prebuilt demo TPKX in order for users to reproduce the teaching/reference package.

If upstream example code/content is deliberately copied in a future contribution, identify the exact source/version and preserve required copyright, license and modification notices.

Image copyright and attribution depend on each user's real input data and must be handled separately; see [LEGAL.md](LEGAL.md).
