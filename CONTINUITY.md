# Project continuity handoff

**Current snapshot: 2026-10-10.** Read this file together with the live repository before resuming. Later user instructions and actual field tests supersede older notes in Git history.

## Current mission

The project is now an end-to-end offline-map manufacturing and field-use system:

```text
Public/web map sources
        +
QGIS map construction and blending
        +
Raster MBTiles
        +
Direct MBTiles -> native TPKX conversion
        +
ArcGIS Earth Desktop/Mobile
        +
Offline GPS-centered field use
```

The guiding idea is not merely to make one map. It is to **manufacture geographic coverage** in repeatable, replaceable pieces that can scale from a small personal map library to very large regional collections without changing the underlying method.

The user-facing experience is increasingly best described as:

> **Google Maps Offline and Improved**

Meaning: zoomable, pannable, high-resolution, GPS-aware maps with mission-specific overlays that remain useful when cellular service disappears.

## Current public repository

Use this repository, not the older ArcGIS Pro project:

`Jim-dc95811/QGIS-Mbtile-to-ArcGIS-Earth-TPKX`

Current main after the latest infographic upload:

`8cf823d13fd966028465c9509bf2e8b974fddf01`

Key files:

- `mb2tpkx.py` / `mb2tpkx.bat` - working direct raster MBTiles -> TPKX converter.
- `Master4_Grid_Maker.py` / `Master4_Grid_Maker.bat` - current Master 4 v3 utility.
- `Master4_Grid_Maker.zip` - current packaged Master 4 program.
- `Master4_Grid_Maker_User_Manual.pdf` - current v3 operator manual.
- `MASTER4_GRID_MAKER.md` - current Master 4 operation/field guide.
- `README.md` - public landing page.
- `TECHNICAL.md` - technical invariants and current validation record.
- `DEMO.md` - public video/teaching flow.
- `CONTINUITY.md` - this handoff file.

## Converter baseline: preserve unless explicitly authorized

The MBTiles converter remains the working byte-preserving bridge. Do not casually refactor or mix new Master 4 behavior into it.

Known baseline identities:

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

The TXT contains **100 cell production rows plus one final `MASTER` row** containing the full 1-degree EPSG:3857 extent.

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

## New operational Z17 product: FFS-style enhanced overview map

A major new product direction is now proven in QGIS: create **grid-wide Z17 operational basemaps** that already contain the mission-relevant overlays, then use Master 4 Z20 cells only when tighter detail is needed.

The working seven-layer FFS-style build is:

1. Google Satellite / Google Earth imagery.
2. Google Labels.
3. FDOT Railroad Routes.
4. ORNL Electric Power Transmission Lines.
5. FFS forest boundaries (`FFS_Current` / public state-forest boundary service).
6. FFS Recreation Trails.
7. ESRI Reference Overlay.

The natural-gas pipeline layer was tested and then deliberately removed from the standard recipe because it added clutter and was comparatively rare for the intended FFS/dozer mission.

The governing operational filter is:

> **Does this layer help answer where the crew can go, where they should not go, or how they get there?**

If not, it probably does not belong in the standard field product.

### Final styling direction

The owner tested both translucent and fully opaque line work and preferred:

- very skinny lines;
- full opacity;
- strong distinct colors;
- black halo only where it improves separation;
- line width allowed to scale with zoom using a QGIS data-defined expression based on `@map_scale`.

The key visual lesson is: use **line width**, not reduced opacity, to control dominance. Reduced opacity looked muddy at tight zoom levels. Thin fully opaque lines stay crisp while preserving the imagery underneath.

### Flattening behavior

When QGIS exports the active map as raster MBTiles, all visible sources are rendered together into final tile images.

That means:

```text
imagery + labels + railroad + power + forest boundaries + FFS trails + reference overlay
        -> one flattened raster MBTiles
        -> one TPKX
```

After export, those individual layers cannot be toggled, recolored, or separated back out of the raster MBTiles/TPKX. This is intentional for the Z17 operational product.

## Public GIS / ArcGIS REST discovery workflow

A major teaching breakthrough is now documented: useful public government GIS layers can often be found in ArcGIS Online / agency map viewers and loaded directly into QGIS.

The practical path is:

```text
Find useful public layer
-> open the search result details
-> click View details (not just the map)
-> find the Service URL
-> copy the FeatureServer / MapServer URL
-> QGIS Data Source Manager
-> ArcGIS REST Server
-> New
-> paste URL
-> Connect
-> select vector layer
-> Add
```

On some ArcGIS Map Viewer links, the underlying service URL is already visible in the browser address bar after `?url=`.

Key translation for beginners:

> **REST = the web doorway QGIS uses to talk directly to the GIS server.**

QGIS having **ArcGIS REST Server** as a built-in Data Source Manager type is important. Do not overstate this as a formal QGIS/Esri partnership unless evidence exists; the important verified fact is technical interoperability through published ArcGIS services.

The project teaching philosophy remains deliberately minimalist:

> **First become an operator. Then become an explorer.**

For videos: follow every click exactly, do not touch unrelated settings until the known-good reference works, then experiment afterward. The videos do not pretend to explain every QGIS internal mechanism.

## QGIS project-save rule

A power surge caused loss of an unsaved QGIS project and forced a rebuild. The rebuild improved the final styling, but the permanent operating lesson is:

> **Save the damn project.**

Practical habit:

```text
connect layer -> style layer -> verify -> Ctrl+S
```

Especially before launching long MBTiles generation runs.

## GPS is a central part of the field concept

The offline map is not merely a static reference. ArcGIS Earth can remain **GPS geocentered in real time** even when cellular service is unavailable.

This is one of the strongest arguments for the system:

```text
offline map + live GPS = current position relative to roads, trails, rail, power corridors, boundaries and imagery
```

The user has described the stripped-down Moto G Play field device as an **ArcGIS appliance**. The appliance model is now:

```text
ArcGIS Earth
+ local TPKX library
+ GPS
+ mission-specific operational map
```

Do not conflate loss of cell service with loss of GPS positioning.

## Android vs Windows field-device reality

Android remains the low-cost field appliance, but Windows is increasingly the preferred full-strength field platform when budget/size allow.

### Android current reality

- Roughly 2 GB Z17 grid-wide TPKX files are in the practical range the current Android device can ingest.
- Large TPKX files do **not** reliably open directly from the SD card.
- Treat the SD card as **warehouse / transfer storage**.
- Copy the active TPKX from SD card to the phone's internal storage first, then open it in ArcGIS Earth Mobile.

Operational shorthand:

```text
SD card = warehouse
internal phone storage = working set
ArcGIS Earth = viewer
GPS = live position
```

### Windows advantage

Windows ArcGIS Earth Desktop has far fewer storage/file-handling restrictions. The plan is to place all regional Z17 TPKX files in one folder/group so that the full collection can behave like one logical statewide library.

The desired end state is essentially:

> **one folder, one group, one click: Florida**

while still keeping each grid package modular and individually replaceable.

## Operation Map Florida

The current statewide effort is now referred to as **Operation Map Florida**.

The plan is to build enough enhanced Z17 packages to cover Florida. Some edge grids may be intentionally extended beyond the nominal 1-degree Master 4 box where that avoids creating a second mostly-empty package.

Example accepted extended extent for the 82W-81W / 29N-30N area:

```text
-9128198.2450,-8994614.8561,3375646.0349,3503549.8435 [EPSG:3857]
```

This intentionally extends the east side to roughly 80.8W to capture the southeast coastal sliver in one Z17 package.

### Future statewide index overlay

Do **not** build the final statewide index overlay until all Florida Z17 package extents are locked.

Permanent rule:

> **Measure three times, form once.**

Once final:

- create one Florida-wide GeoTIFF index overlay;
- draw each production grid extent;
- give each statewide Z17 grid a simple shorthand number (`1`, `2`, `3`, ...);
- use those numbers for folder/file selection and operator callouts;
- once published, a number should never be casually reassigned.

## Master 4 short-location idea

A new concept is being explored for human/radio-friendly location shorthand inside a known Master 4 grid.

A precise four-digit address such as:

```text
55-44
```

means:

- `55` = one 0.1-degree Master 4 cell;
- `44` = one 0.01-degree subcell inside Cell 55 after another 10 x 10 split.

At roughly north Florida latitude, the second-level subcell is approximately:

- ~3,100 ft wide;
- ~3,600 ft tall;
- ~262 acres;
- under about one mile corner-to-corner.

A caller could potentially transmit:

```text
55-44
```

as the **known four digits**, then visually estimate digits 5-6 if additional refinement is needed. A further 10 x 10 estimate would narrow the search to roughly a 300 x 360 ft box.

The key field question is not survey precision but whether a precise four-digit cell puts responders easily into visual acquisition range of something like a smoke plume. This remains a concept to test, not yet a formal published system.

## ArcGIS Earth routing / address-search limitation

The current TPKX-based offline Earth experience still lacks a complete offline turn-by-turn routing system.

Important distinction:

- TPKX/raster map = visual map content;
- turn-by-turn routing requires a local road-network graph plus routing logic;
- offline address search requires an offline locator/geocoder or separate app/database.

ArcGIS Earth is not currently being treated as a full offline navigation engine.

A likely practical workaround is a two-app field appliance:

```text
ArcGIS Earth = custom operational map + GPS awareness
OsmAnd or another offline navigator = address search + routing + turn-by-turn
```

This has not yet been field-integrated. Do not present it as completed.

## Pin-drop / location sharing concept: next major build candidate

ArcGIS Earth Desktop right-clicking a pin exposes **Copy coordinate**, and this was confirmed to place the coordinate pair into the Windows clipboard.

The current proposed utility is a Python/Windows workflow:

```text
ArcGIS Earth pin
-> Copy coordinate
-> Python clipboard watcher recognizes valid GPS coordinates
-> creates QR-code JPEG
-> prompts for recipient(s) from a predefined email-address dropdown/list
-> creates email
-> embeds the QR visibly in the email body (not only as an attachment)
-> includes plain-text coordinates and ideally a clickable ArcGIS Earth app link
-> sends to selected recipient(s)
```

The receiving workflow would be:

```text
email arrives
-> recipient scans QR with the ArcGIS appliance phone
or taps the embedded link on the device
-> ArcGIS Earth opens centered on the transmitted location
```

ArcGIS Earth supports app links with a viewpoint/center concept. Before implementation, verify the exact current ArcGIS Earth app-link syntax and whether it merely centers the view or can create an actual persistent placemark. Do **not** assume it creates a permanent pin unless verified.

This QR/email utility is the next significant software idea. Apply the user's minimal-build rule when implementing it. Do not add unrelated features.

## Operational ArcGIS Earth flow

1. Keep area-wide **Z17 overview TPKX** map(s) enabled.
2. Use the enhanced Z17 operational map as the normal wide-area field view.
3. When an area of interest appears, enable the Master 4 numbered GeoTIFF overlay.
4. Identify the cell(s) needed.
5. Use the manifest rows for exact extents and filenames.
6. Optionally create/open the Cell 55 demo TPKX before QGIS to prove local TPKX loading, home-grid geography and stored zoom behavior.
7. Produce only the needed high-resolution cells in QGIS.
8. Convert compatible MBTiles to TPKX and load the final cells into ArcGIS Earth.

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
- ArcGIS Earth Mobile app-use video: `https://www.youtube.com/watch?v=_FT3GOyjL5Y`

The major video still outstanding is a **full MRTP / multiresolution raster tile pyramid** explanation. Additional videos may revisit the same project from narrower operational angles rather than trying to put every feature into one video.

## Current visual library added to GitHub

The following new project graphics were added under `images/` in commit `8cf823d13fd966028465c9509bf2e8b974fddf01`:

- `Enhanced_Z17_Grid_Visual_Tour.webp`
- `Google_Maps_Offline_Improved.webp`
- `Find_Layer_Step_1.webp`
- `Find_Layer_Step_2.webp`
- `Find_URLs_Load_Layers.webp`
- `Building_Offline_Operational_Map.webp`

`images/README.md` was updated to index them.

The graphics summarize several months of project development and are useful video teaching aids, but generated artwork must not be treated as authoritative technical geometry or proof where exact numbers matter.

## Evidence and rights discipline

- Separate verified fact, owner-observed field behavior, inference and unknown.
- Do not claim the converter downloads imagery; it does not.
- Do not claim third-party imagery redistribution rights from file-format openness.
- Do not publish commercial imagery test packages merely to prove the converter.
- The optional Master 4 demo TPKX is synthetic project-generated color content and is safe to describe separately from real imagery.
- Do not claim formal life-safety certification or universal compatibility.
- Government/public GIS availability does not automatically mean unrestricted downstream redistribution; preserve source/rights discipline.

## First steps on the next session

1. Fetch the live repository head before changing anything.
2. Read this `CONTINUITY.md` together with `README.md`, `MASTER4_GRID_MAKER.md`, `TECHNICAL.md`, `RELEASE_CHECKLIST.md`, and the current scripts before major edits.
3. Preserve the working converter unless the owner explicitly requests a converter change.
4. For software changes, apply the owner's minimal-build rule: one requested functional change, preserve existing behavior, and test the exact requested path.
5. For the proposed clipboard -> QR -> email utility, verify ArcGIS Earth app-link behavior first, then build only the minimum working Windows GUI path requested.
6. Prefer actual ArcGIS Earth acceptance over generic reader acceptance for TPKX claims.
7. For Operation Map Florida, do not create the final statewide numbered index until all Z17 production extents are finalized.
