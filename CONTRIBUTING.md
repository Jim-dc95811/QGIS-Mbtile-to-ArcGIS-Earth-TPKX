# Contributing

Thank you for helping make offline mapping accessible. Before proposing a substantial change, open a GitHub issue describing the need. The published **MBTiles -> TPKX converter** and **Master 4 Grid Maker** are tested baselines; changes should be small, narrowly scoped, and accompanied by reproducible evidence.

## Intellectual property and data

- Contribute only code and documents you are entitled to submit. This project's code is published under the [MIT License](LICENSE), but possible agency publication requirements and contributor ownership/provenance remain separate concerns; please discuss significant code contributions with the maintainer first.
- Credit upstream code you actually use and retain any necessary license or modification notices. Implementing a published format and copying someone else's implementation are different activities.
- Do not commit unauthorized imagery, proprietary reference TPKX packages, private Wireshark recordings, incident mapping data, credentials, tokens, personal information or agency-only materials.
- Reproduce issues with synthetic color tiles or explicitly redistributable imagery. Do not paste copyrighted satellite imagery into issue attachments unless permitted.

## Technical changes

### MBTiles -> TPKX converter

Preserve the existing input/output contract and the original source-image bytes. Do not add unrequested downloading, image recompression or resampling. When changing the converter, document exactly what changed and verify byte-for-byte tile extraction, tile coordinates, zoom levels and multi-bundle behavior. Actual acceptance of the exact new output in ArcGIS Earth and, when claimed, ArcGIS Pro matters: archive or GDAL validation alone did not catch some early compatibility failures.

### Master 4 Grid Maker

Preserve the established 100-cell geometry, numbering, deterministic filename convention, standard TXT/GeoTIFF outputs, and final `MASTER` extent row unless the requested change specifically requires altering them. For geometry-related changes, compare representative W/N, E/N, W/S and E/S outputs against the prior build.

The optional Cell 55 colored TPKX must remain **opt-in** unless an intentional design decision changes that behavior. Its current prompt defaults to No (`[y/N]`). For TPKX-related changes, verify both paths: skipping the demo must leave the normal Master 4 outputs complete, while opting in must create a structurally valid package that is accepted by the target ArcGIS Earth viewer before compatibility is claimed.

Report only application versions, sanitized logs and test materials that are safe to publish. Follow [SECURITY.md](SECURITY.md) for potential vulnerabilities and [LEGAL.md](LEGAL.md) for imagery-rights concerns.

Be courteous to fellow contributors, software vendors and imagery providers; do not claim their endorsement.