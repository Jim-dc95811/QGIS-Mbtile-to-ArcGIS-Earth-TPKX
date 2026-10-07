# Project continuity handoff

**Current snapshot: 2026-10-07.** Read this file together with the live repository before resuming. Later user instructions and actual field tests supersede older notes in Git history.

## Current mission

The project is now an end-to-end offline-map manufacturing system:

```text
Area-wide overview coverage
        +
Master 4 repeatable geographic indexing
        +
QGIS or another compatible raster MBTiles producer
        +
Direct MBTiles -> native TPKX conversion
        +
ArcGIS Earth offline viewing
```

The guiding idea is not merely to make one map. It is to **manufacture geographic coverage** in repeatable, replaceable pieces that can scale from a small personal map library to very large regional collections without changing the underlying method.

## Current public repository

Use this repository, not the older ArcGIS Pro project:

`Jim-dc95811/QGIS-Mbtile-to-ArcGIS-Earth-TPKX`

Key files:

- `mb2tpkx.py` / `mb2tpkx.bat` - working direct raster MBTiles -> TPKX converter.
- `Master4_Grid_Maker.py` / `Master4_Grid_Maker.bat` - current Master 4 v3 utility.
- `Master4_Grid_Maker.zip` - current packaged Master 4 program.
- `Master4_Grid_Maker_User_Manual.pdf` - current v3 operator manual.
- `MASTER4_GRID_MAKER.md` - current Master 4 operation/field guide.
- `README.md` - public landing page.
- `TECHNICAL.md` - technical invariants and current validation record.
- `DEMO.md` - public video/teaching flow.

## Converter baseline: preserve unless explicitly authorized

The MBTiles converter remains the working byte-preserving bridge. Do not casually refactor or mix new Master 4 behavior into it.

Known GitHub baseline identities before the current Master 4-only update:

- `mb2tpkx.py` blob SHA: `87ccc955944b994ad156f25488d04df9197184bd`
- `mb2tpkx.py` SHA-256: `c04dc9f3c1ad74b4180b11465df1189a74c500a5d5873d66a57c2d4076fb3670`
- `mb2tpkx.bat` blob SHA: `267240f9f9f634ac3d8f66bf3f93f9374973372b`
- `mb2tpkx.bat` SHA-256: `078e07834b6fa45f8e63192f60033ac5c322ea236372df22cece8be8a24fda66`

The converter accepts compatible 256 x 256 PNG/JPEG Web Mercator raster MBTiles, reverses TMS rows to XYZ, groups tiles into Esri Compact Cache V2 128 x 128 bundles, and copies source image bytes unchanged. It does not download imagery, create missing zooms, or promise vector/arbitrary MBTiles support.

Large real field tests have opened successfully in ArcGIS Earth, including roughly 4 GB, 20+ GB and 40 GB-class converted packages. Do not claim those large real packages were validated in ArcGIS Pro unless separately tested there.

## Master 4 v3 current state

Input remains one whole-degree box in:

```text
west, east, south, north
```

Example:

```text
82w, 81w, 30n, 31n
```

The program always creates:

- `Master4_<box>_Extents.txt`
- `Master4_<box>_Grid.tif`

The TXT now contains **100 cell production rows plus one final `MASTER` row** containing the full 1-degree EPSG:3857 extent.

Current production filename pattern:

```text
W082W081N031N030-055-GHY-Z20.tpkx
```

Current Master 4 v3 SHA-256 values:

- `Master4_Grid_Maker.py`: `16a42784005743728837d3dfdc2f3295b30071d5ed37ccbddbb9b9ee23e58888`
- `Master4_Grid_Maker.bat`: `abb4e7dd1f1b665e1cf1b9ee4d1bffdef40e336acb746460640be0a043c20c2d`
- `Master4_Grid_Maker.zip`: `408ba3e129f912b3b4ef0a7df0d6ccc478ff8935ffec9cb235232505e872e158`

## v3 optional Cell 55 Z10-Z20 teaching/reference TPKX

After the standard files are already complete, v3 asks:

```text
Create Cell 55 colored zoom-demo TPKX (Z10-Z20)? [y/N]:
```

**No is the default.** Press Enter/N to skip. Y/Yes creates a synthetic file such as:

```text
W082W081N030N029-055-ZOOM-DEMO.tpkx
```

The demo contains synthetic colored tiles at every stored level Z10-Z20. Each level has a different color and visible zoom label.

### Validation/evidence boundary

Before delivery, the standard Master 4 outputs were regression-checked and the demo TPKX structure was checked programmatically. The owner then generated the exact v3 package on Windows and opened it successfully in ArcGIS Earth. Screenshots supplied in chat visibly showed several level transitions including Z12, Z13, Z14, Z15, Z17 and Z20.

The owner reports the current Cell 55 package is roughly 1 GB. This is expected for the dense Z10-Z20 synthetic pyramid and is not a storage-efficiency target.

At coarse zoom levels, standard XYZ tiles are larger than one 0.1-degree Master 4 cell; visible colored coverage can extend beyond the exact Cell 55 boundary. The exact boundary remains the GeoTIFF/manifest. Do not misdescribe the low-zoom colored footprint as an exact clipped cell polygon.

## Operational ArcGIS Earth flow now being documented/videoed

1. Keep area-wide **Z17 overview TPKX** map(s) enabled.
2. When an area of interest appears, enable the Master 4 numbered GeoTIFF overlay.
3. Identify the cell(s) needed.
4. Use the manifest rows for exact extents and filenames.
5. Optionally create/open the Cell 55 demo TPKX before QGIS to prove local TPKX loading, home-grid geography and stored zoom behavior.
6. Produce only the needed high-resolution cells in QGIS.
7. Convert compatible MBTiles to TPKX and load the final cells into ArcGIS Earth.

**Permanent production rule:** reference overlays ON while planning; OFF before production.

## Offline reference-beacon behavior

The owner observed that when ArcGIS Earth is offline and familiar online basemap context disappears, opening the synthetic Cell 55 TPKX provides:

- a known geographic anchor in the home Master 4;
- strong visual structure;
- obvious stored zoom-level feedback;
- a quick confirmation that local TPKX loading still works.

Document this as an operator convenience/teaching aid, not as a replacement for a real offline basemap or certified navigation product.

## Published videos currently linked

- Google Maps OFFLINE proof/demo: `https://www.youtube.com/watch?v=8uziJNzan1g`
- Washington, DC QGIS -> TPKX tutorial: `https://www.youtube.com/watch?v=C71n8TAByuE`
- Master 4 + QGIS batch end-to-end video: `https://www.youtube.com/watch?v=zNt-I4KgAy8`

A follow-up ArcGIS Earth operating-flow video is planned but not yet linked in the repository. Do not invent a URL/title until the owner publishes it.

## Evidence and rights discipline

- Separate verified fact, owner-observed field behavior, inference and unknown.
- Do not claim the converter downloads imagery; it does not.
- Do not claim third-party imagery redistribution rights from file-format openness.
- Do not publish commercial imagery test packages merely to prove the converter.
- The optional Master 4 demo TPKX is synthetic project-generated color content and is safe to describe separately from real imagery.
- Do not claim formal life-safety certification or universal compatibility.

## First steps on the next session

1. Fetch the live repository head before changing anything.
2. Read `README.md`, `MASTER4_GRID_MAKER.md`, `TECHNICAL.md`, `RELEASE_CHECKLIST.md` and the current Master 4 script.
3. Preserve the working converter unless the owner explicitly requests a converter change.
4. For Master 4 changes, apply the owner's minimal-build rule: one requested functional change, preserve existing behavior, and test exact outputs.
5. Prefer actual ArcGIS Earth acceptance over generic reader acceptance for TPKX claims.
