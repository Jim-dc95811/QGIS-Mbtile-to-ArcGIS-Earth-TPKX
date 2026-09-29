# Release checklist

This is a practical review list, not a declaration of legal compliance, government approval or GIS fitness.

## Ownership and licensing
- [ ] Identify who can authorize publication and license the original code, including any relevant employer or public-agency policy.
- [ ] Review attribution and license notices for any upstream implementation code actually incorporated.
- [ ] Choose and approve the project's license; add the exact approved LICENSE text and update LICENSE_STATUS.md.
- [ ] Review QGIS's brand guidelines regarding use of the QGIS name in this repository and planned promotion.
- [ ] Keep any no-affiliation statements accurate.

## Imagery and sample data
- [ ] Use synthetic examples or record permission for each published dataset, screenshot and sample package.
- [ ] Check acquisition, local storage, offline conversion, display, thumbnail creation and redistribution permissions for the actual source and service.
- [ ] Ensure required credits appear in the destination viewer: the converter currently does not transfer MBTiles attribution metadata.
- [ ] Do not publish restricted ArcGIS Pro reference files, private captures or operational mapping data without authorization.

## Recorded field-test milestones (2026-09-27)

These are **owner-reported, screenshot-supported tests**, not formal third-party certification:

- [x] Real-world ~4 GB MBTiles converted with the distributed script and opened successfully in ArcGIS Earth.
- [x] ~39.9-million-KB PNG MBTiles grid converted to ~39.6-million-KB TPKX; owner reports responsive offline viewing in ArcGIS Earth.
- [x] Separate JPEG/75 grid produced ~4.35-million-KB MBTiles and ~4.09-million-KB TPKX, with a visually clear Z20 hybrid map in ArcGIS Earth; **no converter modification was needed**.
- [ ] If publishing a quantified PNG-versus-JPEG compression claim as a controlled benchmark, reproduce it with *identical tile inventory and imagery*, document actual JPEG quality and retain the test procedure.
- [ ] Independently check larger and more varied inputs, interruptions and missing or uneven zoom coverage before general large-file compatibility claims.

See [TECHNICAL.md](TECHNICAL.md) and [README.md](README.md) for the actual Windows-reported figures and interpretation. Do not publish third-party test imagery solely to substantiate these results.

## Public documentation and video (2026-09-28)

- [x] Link the published [Jacksonville offline-mapping demonstration](https://www.youtube.com/watch?v=8uziJNzan1g) from the README and explain what is—and is not—being reproduced.
- [x] Provide a source-agnostic four-stage explanation, beginner quick start and dedicated [video guide](DEMO.md).
- [x] Record the owner-reported Jacksonville Metro JPEG/75 hybrid test (**21,786,032 KB MBTiles → 20,629,591 KB TPKX**) with evidence limitations in [TECHNICAL.md](TECHNICAL.md).
- [x] Document the corrected synthetic Z12–Z18 color demo and its instructional purpose.
- [ ] Review final publication of any separately supplied illustrations; do not assume they are hosted by GitHub merely because they were uploaded to a chat.
- [ ] Select and approve a software license and any required ownership/source-code notices before representing the repository as open-source-licensed. See [LICENSE_STATUS.md](LICENSE_STATUS.md).
- [ ] Complete any required owner/agency clearance and source-imagery credit review for published screenshots and future demo downloads.

## Converter quality and scope
- [ ] Preserve the working Python/BAT baseline and its checksums.
- [ ] Verify original imagery bytes, tile coordinates, zoom levels and multi-bundle indexes after any code change.
- [ ] Check output from the exact new build in ArcGIS Earth and ArcGIS Pro before claiming compatibility with each.
- [ ] Validate offline navigation, real-world coverage and representative dataset sizes before deployment claims.
- [ ] Document remaining limits on unusual MBTiles layouts, large datasets and attribution.
- [ ] Review dependencies and establish private security reporting if appropriate.

The software is an experimental map-production utility, not a certified navigation or life-safety system. Independent verification of map currency, alignment and coverage is needed before operational reliance. These checks must be completed by people with the authority and evidence to do so.
