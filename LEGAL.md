# Rights, attribution, and responsible use

This document describes this project's intended practices and **known limitations**. It does not certify legal compliance, amend anyone's license, or replace review by the relevant rights holder or agency.

## What the project does and does not do

This independent, public-safety-motivated project now contains two related tools:

- the **MBTiles -> TPKX converter**, which repackages an existing compatible raster MBTiles database into an Esri Compact Cache V2 TPKX package while preserving the source PNG/JPEG map-tile bytes; and
- **Master 4 Grid Maker**, which creates repeatable geographic extents, a numbered reference GeoTIFF, deterministic production filenames, and an optional synthetic Cell 55 Z10-Z20 TPKX made from project-generated colored teaching tiles.

Neither tool downloads commercial map imagery from a provider. The converter does not evade an access control or alter the source map image bytes; it does create a **new thumbnail derived from an input tile**. The optional Master 4 colored TPKX is generated locally from synthetic project-created graphics and does not require third-party imagery.

The project relies on published format descriptions and comparisons with legitimately created example packages. It is **not affiliated with or endorsed by** Esri, QGIS, Google, Mapbox, imagery providers, or any government agency unless authorization is separately documented.

Technical access to a provider, possession of an MBTiles file, or the ability to make a TPKX does not establish permission to copy, cache, repackage, use offline, or redistribute third-party map content.

## Imagery-provider rights

Users must establish permissions applicable to their **specific imagery source, service, contract, jurisdiction, and intended activity**, including acquisition, caching, conversion, offline retention, internal sharing, publication and redistribution. A public-safety, charitable, educational or noncommercial motive does not, by itself, grant those permissions. Provider terms may impose expiration, display, attribution, watermark, geographic, and downstream-distribution requirements.

This converter is format-neutral: imagery from different sources may be technically convertible but carry very different rights. For some services, **offline caching or storage is prohibited without additional authorization**, regardless of whether the tiles can be viewed in QGIS. See, when applicable:

- [Google Maps / Google Earth terms](https://www.google.com/help/terms_maps/)
- [Google Map Tiles API policies](https://developers.google.com/maps/documentation/tile/policies)
- The applicable contract or service terms for **the actual Esri imagery source**, not merely Esri's TPKX format documentation.

The repository intentionally does **not** publish downloaded commercial imagery, third-party licensed reference TPKX packages, credentials, or agency operational data. Inclusion of any future sample data requires documented permission or original/synthetic provenance. The Master 4 Cell 55 colored demo is synthetic project-generated content and is documented separately from real imagery.

## Attribution limitation of the current converter

The current converter preserves any copyright markings already **inside the image pixels** because the tile image bytes are copied unchanged. It currently transfers only the MBTiles **dataset name** into package metadata; it does **not** propagate separate source attribution, provider copyright strings, license URLs, required logos, or service-specific credits. It separately generates a thumbnail from a source tile.

**Do not treat a successful conversion as a fully attributed map.** Review the source's credit requirements and ensure attribution is properly preserved and displayed in the resulting application and in any shared files, documentation, or downstream products. If you cannot satisfy a source's obligations in the destination application, do not use that source in the workflow without permission.

No software feature here verifies a user's imagery license. The `exportTilesAllowed` metadata value is not a statement of legal permission or an access-control mechanism.

## Format documentation, upstream licenses and acknowledgments

Esri openly publishes [Compact Cache V2 documentation and example Python code](https://github.com/Esri/raster-tiles-compactcache) and the [TPKX specification](https://github.com/Esri/tile-package-spec), both under **Apache License 2.0**. They document a technical format and provide material for interoperable implementations. They do **not** endorse this project, license Esri-hosted imagery, authorize use of Esri products, or license unrelated third-party imagery. The public specifications are credited in [CREDITS.md](CREDITS.md).

The converter also reads the [MBTiles format](https://github.com/mapbox/mbtiles-spec); its documentation license is **not** a license for arbitrary imagery stored in an MBTiles file. See [CREDITS.md](CREDITS.md) for dependency and specification acknowledgments.

**Source-code provenance review remains necessary:** publishing a format description does not eliminate obligations if someone actually incorporates copyright-protected upstream example code. No claim of a formally audited clean-room implementation is made here. Record sources for any future borrowed implementation code, preserve required notices and review compatibility with the license selected for this repository.

## Names, logos and affiliation

References to QGIS and Esri describe software compatibility and workflow. Their marks belong to their owners. **Do not use their logos or imply sponsorship.** [QGIS trademark and brand guidelines](https://www.qgis.org/community/organisation/guidelines/) distinguish ordinary descriptive references from certain software-product names that may require permission. Because this repository's current name contains “QGIS,” the owner should confirm that the current descriptive use is appropriate or obtain any required permission before wider promotion; do not assume the existing name has been approved.

## Repository code licensing and agency rights

The project owner added the [MIT software license](LICENSE) with a copyright notice naming Jim Gaddy (2026). The license permits use, modification and redistribution of the project's software under its stated notice requirement; it does **not** license the underlying map imagery or unrelated third-party materials. Any applicable ownership, employer/agency publication approval, or upstream-source attribution obligations remain separate matters for appropriate review. See [LICENSE_STATUS.md](LICENSE_STATUS.md).

The project owner's public-safety employment is context for the project's motivation, **not** a claim of official governmental endorsement or authorization. Do not add an agency seal, agency name as sponsor, or official status absent approval.

## Reliability and operational safeguards

These experimental map-production tools and their outputs are provided without a representation of fitness for emergency response, navigation, or any life-safety purpose. Satellite imagery may be incomplete, inaccurate, outdated or geospatially misaligned; output quality and permissions cannot exceed the real imagery input. Independently confirm map currency, coverage, coordinates, multi-zoom transitions, device operation and offline functionality before operational deployment. Maintain authorized fallback maps and procedures.

The synthetic Cell 55 TPKX is a teaching/reference aid. Its low-zoom whole-tile footprint may extend beyond the exact Cell 55 boundary, and it is not a substitute for an authoritative offline basemap or navigation product.

## Rights-holder concerns and corrections

If you own rights in material accidentally committed here, identify the **repository file or link** and the nature of the concern in a GitHub issue without publicly posting more protected content or personal details. For sensitive matters, request private contact information rather than posting confidential materials. Maintainers should review the concern, restrict affected material where appropriate, and seek rights-holder or agency guidance rather than arguing that emergency-response motivation overrides license terms.