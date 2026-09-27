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

## Converter quality and scope
- [ ] Preserve the working Python/BAT baseline and its checksums.
- [ ] Verify original imagery bytes, tile coordinates, zoom levels and multi-bundle indexes after any code change.
- [ ] Check output from the exact new build in ArcGIS Earth and ArcGIS Pro before claiming compatibility with each.
- [ ] Validate offline navigation, real-world coverage and representative dataset sizes before deployment claims.
- [ ] Document remaining limits on unusual MBTiles layouts, large datasets and attribution.
- [ ] Review dependencies and establish private security reporting if appropriate.

The software is an experimental map-production utility, not a certified navigation or life-safety system. Independent verification of map currency, alignment and coverage is needed before operational reliance. These checks must be completed by people with the authority and evidence to do so.
