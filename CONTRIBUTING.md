# Contributing

Thank you for helping make offline mapping accessible. Before proposing a substantial change, open a GitHub issue describing the need. The published converter is a tested baseline; changes should be small and accompanied by reproducible evidence.

## Intellectual property and data

- Contribute only code and documents you are entitled to submit. This project's code is published under the [MIT License](LICENSE), but possible agency publication requirements and contributor ownership/provenance remain separate concerns; please discuss significant code contributions with the maintainer first.
- Credit upstream code you actually use and retain any necessary license or modification notices. Implementing a published format and copying someone else's implementation are different activities.
- Do not commit unauthorized imagery, proprietary reference TPKX packages, private Wireshark recordings, incident mapping data, credentials, tokens, personal information or agency-only materials.
- Reproduce issues with synthetic color tiles or explicitly redistributable imagery. Do not paste copyrighted satellite imagery into issue attachments unless permitted.

## Technical changes

Preserve the existing input/output contract and the original source-image bytes. Do not add unrequested downloading, image recompression or resampling. When changing a converter, document exactly what changed and verify byte-for-byte tile extraction, tile coordinates, zoom levels and multi-bundle behavior. Actual acceptance of the exact new output in ArcGIS Earth and, when claimed, ArcGIS Pro matters: archive or GDAL validation alone did not catch some early compatibility failures.

Report only application versions, sanitized logs and test materials that are safe to publish. Follow [SECURITY.md](SECURITY.md) for potential vulnerabilities and [LEGAL.md](LEGAL.md) for imagery-rights concerns.

Be courteous to fellow contributors, software vendors and imagery providers; do not claim their endorsement.
