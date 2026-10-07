# Release checklist

This is a practical review list, not a declaration of legal compliance, government approval or GIS fitness.

## Ownership and licensing
- [ ] Identify who can authorize publication and license the original code, including any relevant employer/public-agency policy.
- [ ] Review attribution/license notices for any upstream implementation code actually incorporated.
- [x] MIT License is present for the project software.
- [ ] Review QGIS/Esri/other brand usage in public promotion where applicable.
- [ ] Keep no-affiliation statements accurate.

## Imagery and sample data
- [ ] Use synthetic examples or record permission for each published real dataset/screenshot/sample package.
- [ ] Check acquisition, local storage, offline conversion, display, thumbnail creation and redistribution permissions for real imagery.
- [ ] Ensure required credits remain visible when needed; the converter does not transfer every MBTiles attribution field.
- [ ] Do not publish restricted ArcGIS Pro reference packages, private captures or operational mapping data without authorization.
- [x] The Master 4 Cell 55 Z10-Z20 teaching package is synthetic project-generated color content and does not download commercial imagery.

## Converter field-test milestones
- [x] Real-world ~4 GB MBTiles converted with the distributed script and opened in ArcGIS Earth.
- [x] ~39.9-million-KB PNG MBTiles grid converted to ~39.6-million-KB TPKX and used in ArcGIS Earth.
- [x] Separate JPEG/75 grid converted without converter modification and displayed clearly in ArcGIS Earth.
- [x] Jacksonville Metro JPEG/75 hybrid test recorded: 21,786,032 KB MBTiles -> 20,629,591 KB TPKX.
- [ ] Do not publish a universal PNG-vs-JPEG compression claim without a controlled identical-source comparison.
- [ ] Do not claim the large real packages are ArcGIS Pro-validated unless separately tested there.

## Master 4 v3 release checks
- [x] Standard TXT/GeoTIFF production behavior regression-checked against the prior build.
- [x] Final full-box `MASTER` row documented.
- [x] Optional Cell 55 TPKX prompt is explicit and defaults to **No** (`[y/N]`).
- [x] Opt-out path leaves the standard Master 4 files complete and does not require a demo TPKX.
- [x] Optional demo zoom range is Z10-Z20.
- [x] Demo TPKX structure checked programmatically before delivery.
- [x] Project owner generated the v3 package on Windows and opened it successfully in ArcGIS Earth.
- [x] Owner-supplied screenshots visibly confirmed several stored-level transitions including Z12, Z13, Z14, Z15, Z17 and Z20.
- [x] Current field-test size described as roughly 1 GB without presenting that as a fixed guarantee.
- [x] Coarse-zoom whole-XYZ-tile footprint documented; do not imply the colored raster is clipped exactly to Cell 55.
- [x] Reference overlay rule documented: ON while planning; OFF before production.
- [x] Offline-reference-beacon use documented as an owner-observed convenience, not a replacement for authoritative offline mapping.

## Public documentation/video
- [x] Jacksonville offline-mapping demonstration linked.
- [x] Washington, DC QGIS-to-ArcGIS Earth tutorial linked.
- [x] Master 4 + QGIS end-to-end video linked.
- [x] v3 Master 4 guide updated for optional Cell 55 TPKX.
- [x] v3 Operator Manual updated.
- [x] Master 4 multi-zoom teaching illustration added.
- [x] Area-wide Z17 -> grid -> selected cells -> production flow documented.
- [ ] Add the future ArcGIS Earth follow-up video only after the owner publishes a real URL/title.

## Software quality
- [ ] Preserve the working `mb2tpkx.py`/BAT baseline unless a converter change is explicitly requested.
- [ ] After any converter change, verify imagery bytes, coordinates, zoom levels, multi-bundle indexes and exact new output in ArcGIS Earth.
- [ ] After any Master 4 geometry change, verify standard manifest rows, full-box row, GeoTIFF georeferencing and representative hemisphere/boundary cases.
- [ ] After any Master 4 TPKX change, verify opt-out behavior and open the exact new demo package in ArcGIS Earth before claiming success.
- [ ] Review dependencies/security reporting as the project grows.

The software is an experimental map-production utility, not a certified navigation or life-safety system. Independent verification of map currency, alignment and coverage is required before operational reliance.
