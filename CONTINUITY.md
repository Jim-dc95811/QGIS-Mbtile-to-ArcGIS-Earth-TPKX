# Project continuity handoff

**Snapshot: 2026-09-27.** For the next ChatGPT conversation working with this project, **read this file, the current repository files, and relevant Library materials before resuming**. This is a dated handoff, not a substitute for fetching newer evidence. Later user instructions and actual test results supersede this snapshot.

## Second public video: Washington, DC map-making tutorial (2026-09-29)

- The owner published **[How to Make an Offline Map with QGIS and ArcGIS Earth](https://www.youtube.com/watch?v=C71n8TAByuE)**, a roughly seven-minute beginner video demonstrating QGIS raster MBTiles production, conversion with this project's Python tool, and viewing in ArcGIS Earth using Washington, DC as the map target. The owner provided the YouTube link and confirmed publication; the video was not independently watched during this documentation update.
- The README and DEMO guide now feature both the earlier Jacksonville proof-of-concept video and the new practical tutorial. The Python converter and Windows launcher were not modified for this documentation update.

## Verified repository publication update (2026-09-28)

- The project owner added a root **[MIT LICENSE](LICENSE)** identifying **Jim Gaddy (2026)**; the current [LICENSE_STATUS.md](LICENSE_STATUS.md) and public README describe that license. This changes the **software** licensing status but does not establish rights to third-party imagery or conclusively resolve any outside ownership/agency approvals.
- Both supplied illustrations were uploaded to **[images/](images/)** and are embedded in the main [README](README.md) and [DEMO.md](DEMO.md): the four-stage hand-drawn workflow and the more dramatic MBTiles → TPKX graphic. Their original timestamped filenames were preserved as uploaded.
- The YouTube demonstration is linked on the homepage: https://www.youtube.com/watch?v=8uziJNzan1g . Documentation now distinguishes the source-imagery permission requirements from the MIT software license.
- Verify all of these against the live GitHub repository when resuming, as the historical notes below describe states that were true **before** publication.

## Update after the September 28 public video release

- The owner published **[Google Maps OFFLINE — The Impossible Is Now Possible!](https://www.youtube.com/watch?v=8uziJNzan1g)**. The repository README and [DEMO.md](DEMO.md) now lead with the viewing demonstration and a four-stage, source-agnostic explanation.
- The owner reported a further single-file **Jacksonville Metro JPEG/75 Z20** result: **21,786,032 KB MBTiles → 20,629,591 KB TPKX**, with the output displayed in ArcGIS Earth. A separately created Jacksonville Street Z20 map was also loaded in Earth. Consult [TECHNICAL.md](TECHNICAL.md) for details and limits.
- A synthetic colored Z12–Z18 Jacksonville test package was corrected after an interrupted first generation and then displayed successfully in ArcGIS Earth. The owner also found a useful role for the partial package in visually demonstrating a border and changing zoom levels.
- The project owner requested a video link, two illustrations and a public-readiness audit. At that initial point the illustrations and license were still pending; see the newer verified publication update above and confirm the current repository state when resuming.
- The original Python converter and BAT launcher must remain unchanged unless the owner specifically authorizes an implementation change. Verify current GitHub blob SHAs before claiming the baseline is preserved.

## First steps when refreshing

1. Open this repository: https://github.com/Jim-dc95811/QGIS-Mbtile-to-ArcGIS-Earth-TPKX . The repository URL still contains QGIS, but the **converter itself is source-application-independent**.
2. Read **README.md** for the current public description and test figures; **TECHNICAL.md** for compatibility details, failed approaches, byte-level invariants, checksums and exact validation requirements; **RELEASE_CHECKLIST.md**, **LEGAL.md**, and **LICENSE_STATUS.md** before changes or release claims.
3. Search the user's ChatGPT **Library** for **MB2TPKX_Technical.pdf** and **mb2tpkx.py** (both were found in Library search on 2026-09-27), and any subsequent project files. The PDF and Library code may be earlier snapshots; compare them to the GitHub baseline before relying on them. Request the relevant prior screenshots or private test inputs from the user when needed; they are not intentionally in this public repository.
4. For any new work, obtain the **latest** GitHub file contents and actual current test state. Do not rely solely on chat memory, this snapshot or plausible extrapolations.

## Mission and why this project matters

Enable **map makers and map keepers**, including non-GIS specialists, to select and preserve suitable offline maps. A user may create **standard compatible raster MBTiles in QGIS or another producer** and convert them directly to **Esri Compact Cache V2 TPKX** for native, responsive offline viewing in **ArcGIS Earth**. This is a bridge between formats, **not a Google tile downloader, a QGIS extension, a general raster resampler or a replacement for all Google Maps application features**.

What mattered most to the owner was preserving **the original multizoom visual cartography**: zoom-dependent labels, road hierarchy, typography, place names and imagery captured at each source zoom level. Enlarging one still image to imitate a zoom pyramid does not accomplish that. Once the producer has captured distinct raster tiles at each zoom, our converter preserves their image bytes. The result can display source-specific cartographic states while zooming offline in ArcGIS Earth. Geographic referencing is retained; location/GPS and other viewer functions depend on the device, loaded data and actual configuration.

**ArcGIS Earth is the viewer. MBTiles is the portable production input. TPKX is the native offline output.** Do not frame QGIS as the only route or suggest the converter creates source imagery.

## Working software: preserve this exact baseline

- **mb2tpkx.py**: the tested Python CLI. GitHub baseline SHA-256: `c04dc9f3c1ad74b4180b11465df1189a74c500a5d5873d66a57c2d4076fb3670`.
- **mb2tpkx.bat**: Windows drag/drop or prompt launcher. Baseline SHA-256: `078e07834b6fa45f8e63192f60033ac5c322ea236372df22cece8be8a24fda66`.
- As confirmed at the latest repository documentation update on this date, the actual GitHub **blob SHAs** remained `87ccc955944b994ad156f25488d04df9197184bd` (Python) and `267240f9f9f634ac3d8f66bf3f93f9374973372b` (BAT).
- Requires Python 3 and Pillow; reads standard **256x256 PNG/JPEG Web Mercator raster MBTiles** using expected TMS tile rows. It does not promise vector MBTiles or arbitrary grids/variants.
- Reverses TMS rows to XYZ, partitions tiles into Esri's **128x128 Compact Cache V2** bundles, writes indexes and known-good package metadata. **Copies actual image tiles byte-for-byte**; only a separate package thumbnail is newly generated.
- Original MBTiles stays unchanged. The script does not overwrite an existing TPKX. **No code change was needed for JPEG/75**: JPEG compression is selected in the *upstream MBTiles producer*, not in our converter.
- **Do not casually refactor, rename, optimize, add options or modify these working files.** The owner's standing engineering rule is minimal change: one explicitly requested functional modification only, preserve paths and established behavior, and test the exact modified output before claiming it works. This is a CLI/BAT utility, **not a GUI**. If a future task introduces a GUI program, actually launch and inspect its GUI before delivery.

The full byte-level layout, including reference metadata values and bundle headers, is recorded in **TECHNICAL.md**. Early trial packages passed some generic reader checks but **failed ArcGIS Earth**, so acceptance in the actual target viewer matters more than superficial format validation.

## Historical technical breakthrough

The project previously tried KML super-overlays, including local and HTTP-backed tiled hierarchies. Google Earth navigated them well, but tested ArcGIS Earth KML versions showed multi-second interaction delays. Synthetic color-tile and Wireshark experiments suggested that merely moving KML files onto a fast local HTTP server was not enough; the exact internal bottleneck was not established.

The successful alternative came from studying Esri's **publicly documented Compact Cache V2 and TPKX specifications** and comparing two known-good ArcGIS Pro-produced reference packages. Compatibility required matching exact tiling metadata, JSON and binary bundle conventions. After successful synthetic **Color 2B** multi-bundle testing in ArcGIS Earth and ArcGIS Pro, real Bryceville imagery and then real MBTiles conversions succeeded in ArcGIS Earth.

Do not restart the failed KML route or rewrite the successful parser unless a new, clearly stated user objective requires it.

## Test record: separate what was actually observed from inference

**User-reported tests supported by user-provided screenshots; no claim that ChatGPT independently ran these large files:**

| Test | Input MBTiles (Windows-displayed KB) | Output TPKX (Windows-displayed KB) | Observed/reported result |
| --- | ---: | ---: | --- |
| Real MBTiles first large field test (`3-1-1_10`) | 4,137,400 | 4,108,022 | Worked in ArcGIS Earth, including a scene that previously exposed poor KML responsiveness |
| `Master Grid 3-1 z20`, PNG-source run | 39,891,100 | 39,587,335 | Worked in ArcGIS Earth; owner reports instantaneous screen presence, very responsive navigation and no conspicuous pixelation |
| `Master Grid 3-2 z20 jpg`, JPEG/75-source run | 4,354,360 | 4,090,206 | Worked in ArcGIS Earth; screenshot shows legible Z20 hybrid labels and detailed imagery |

The two master-grid runs are **different grids**, albeit described by the owner as comparable in area. The JPEG/75 run was about 9.2 times smaller on MBTiles and 9.7 times smaller on TPKX, a compelling field observation, **not a controlled same-source, same-tile PNG/JPEG benchmark**. Do not claim equivalent pixel fidelity or guaranteed 90% savings for all content. Google Hybrid's labels and varying font sizes make visual errors unusually easy to spot.

**Other current production status at this snapshot:** the owner reported a **Jacksonville Metro Z18 MBTiles at roughly 1.6 GB** and started a more ambitious metro **Z20 JPEG/75** run. The final Z20 metro size and outcome were **not confirmed in this handoff**; ask the user or review later records rather than inventing them. The user also intends/has the ability to produce comparable Esri-sourced imagery for geographic comparison.

## Upcoming public-facing videos: do not mix up the audiences

**Video 1 is a completely nontechnical teaser**, not a QGIS tutorial. Proposed storyboard:

1. In **live Google Maps**, start above Jacksonville; in **Street mode**, zoom in to downtown/riverfront and back out. Emphasize progressive changes in typography, named places, road graphics and hierarchy.
2. Repeat **online in Google Hybrid mode**, so viewers see the same changing cartography over satellite photography.
3. **Disconnect the internet visibly** and establish that the computer is offline.
4. Open **ArcGIS Earth**, repeat the Street journey on its offline map; switch to the separately captured Hybrid map with a layer checkbox and repeat the second journey. The key reveal is the **same map-display navigation experience**, without implying Google search, directions, Street View, right-click tools or live information are duplicated.
5. Optionally demonstrate a genuine **offline GPS position** or viewer drawings/measurements *only if actually verified on the filming device*. A brief **synthetic colored zoom-level tile** demonstration may explain how each zoom has separate stored imagery. Close with a promise of how-to videos, not a technical lecture.

Working hook: **same maps, same zoom, no internet**. Visually compare shifting labels and fonts; a photograph of a forest alone conceals mistakes. The user has already discussed a thumbnail and multiple prospective titles, but do not pretend the title, footage or finished video is final.

**Video 2 / tutorial** can demonstrate a simple QGIS workflow using the current canvas extent and the appropriate MBTiles generation tool and image format, then the independent converter and ArcGIS Earth. **Do not lead beginners into district-scale split grids, extensive coordinate math or DPI experiments in the first lesson.** Emphasize that QGIS is an example producer, not a requirement. Other compatible raster MBTiles-making applications can supply the input. Advanced systematic coverage and map-library management are separate topics.

## Follow-up opportunities, but no authorization to implement

- Capture and compare source imagery (e.g. visual cartography, clarity, apparent freshness) before creating each offline map. A user can keep different provider maps for different purposes, subject to the particular provider permissions.
- A controlled same-source PNG/JPEG comparison and further JPEG quality experiments are possible, but not required to accept the existing observed successes.
- An optional advanced experiment obtained USGS elevation GeoTIFF data and contemplated combining it with offline imagery for ArcGIS Earth elevation profiles. The user explicitly **paused** that exploration to avoid sidetracking the main video. An image displayed in the viewer is **not proof** that a GeoTIFF has been configured and successfully used as offline terrain.
- Broader offline GPS and public-safety uses, and future neighborhood/district map library management, are possible follow-ups. Do not assert an operational certification or untested device capability.

## Publication status, evidence discipline and source rights

The repository already includes **README.md**, **TECHNICAL.md**, **RELEASE_CHECKLIST.md**, **LEGAL.md**, **CREDITS.md**, **LICENSE_STATUS.md**, **CONTRIBUTING.md**, **SECURITY.md**, and the original program/launcher. The README, technical notes and release checklist were updated to include the PNG/JPEG breakthroughs on 2026-09-27. **No project software license had been selected at this snapshot**; do not choose one or claim official agency authorization on behalf of the owner.

The converter is an independent interoperability utility; it does **not download imagery**, grant provider rights, change existing embedded raster markings, or automatically transfer all separate MBTiles attribution metadata (only the dataset name). File-format openness does not decide the usage rights of the image content. See the current rights documents rather than making new blanket legal claims or changing the user's technical work.

A prior broad documentation search in conversation found **no verified, documented predecessor matching the full independently sourced, native offline multizoom conversion-and-ArcGIS-Earth workflow** examined there. This is a finding **within that documented search's criteria**, not a claim to have established worldwide historical priority; do not derail a precise evidence-based discussion with unsupported hypotheticals.

When working with the owner, **distinguish user-observed facts, tool-verified contents, reasonable inferences and unknowns**. Prioritize getting functional results with the smallest change. If asked to update a project, inspect GitHub and applicable Library materials first. Never claim that software, a graphic result, a specific viewer path or new code has been tested unless that exact test occurred.

## One-sentence next-conversation refresh request

**"Read CONTINUITY.md, README.md and TECHNICAL.md in my MBTiles-to-TPKX GitHub repository and refresh from my relevant ChatGPT Library files before we continue. Preserve the original working converter unless I explicitly request a change."**
