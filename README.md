# MBTiles → TPKX: offline maps for ArcGIS Earth

**Make a native offline ArcGIS Earth map from an existing raster MBTiles file—without ArcGIS Pro or an intermediate GeoTIFF.** Bring MBTiles from QGIS or another compatible producer; the converter preserves the original map tiles at every recorded zoom level.

## Watch the demonstration

**[Google Maps OFFLINE — The Impossible Is Now Possible!](https://www.youtube.com/watch?v=8uziJNzan1g)**

[![Watch the offline maps demonstration](https://img.youtube.com/vi/8uziJNzan1g/hqdefault.jpg)](https://www.youtube.com/watch?v=8uziJNzan1g)

The video shows online Street and Hybrid map navigation over Jacksonville, then an offline demonstration in ArcGIS Earth. The synthetic color-tile sequence makes the separately stored zoom levels visible. **This reproduces the captured map-display experience, not Google's complete application:** search, live traffic, Street View, routing and other online services are not reproduced.

**New here?** [See the four-step visual explanation and video notes](DEMO.md). **Continuing the engineering project?** Start with [CONTINUITY.md](CONTINUITY.md) and the current [technical record](TECHNICAL.md).

## Four steps, from imagery to offline map

1. **Choose an imagery source** appropriate for your purpose, with the necessary rights for your intended use.
2. **Create raster MBTiles.** QGIS is one example; the converter does not require QGIS specifically.
3. **Convert MBTiles → TPKX** with the included Python program. It copies the original PNG/JPEG image tiles without re-encoding or rebuilding the zoom pyramid.
4. **Open the TPKX in ArcGIS Earth** and navigate the captured map offline.

```mermaid
flowchart LR
    A[Imagery source] --> B[Raster MBTiles producer]
    B -->|MBTiles| C[Python converter]
    C -->|TPKX| D[ArcGIS Earth offline]
```

## Download and use

Use this repository's **Code → Download ZIP**, then extract `mb2tpkx.py` and `mb2tpkx.bat` into the same folder.

**Requirements:** Python 3 and [Pillow](https://pillow.readthedocs.io/) installed once:

```powershell
py -m pip install Pillow
```

**Windows:** Drag your existing `.mbtiles` file onto `mb2tpkx.bat`, or double-click the BAT and paste the source path when prompted.

**Command line:**

```powershell
py mb2tpkx.py "input.mbtiles" "output.tpkx"
```

The source file is retained. Output is created alongside it unless you specify another location, and **an existing output is not overwritten**. Allow additional disk space and time for large datasets. Open the finished `.tpkx` with ArcGIS Earth. This is a Python CLI with a Windows launcher, not a GUI program.

## Real-world results

The project owner has supplied Windows Explorer screenshots and tested the converted packages interactively in ArcGIS Earth. These are **reported field tests**, not universal performance or quality guarantees.

| Example | Source MBTiles (Windows-displayed KB) | Resulting TPKX (KB) | Reported observation |
| --- | ---: | ---: | --- |
| First large real-data test | 4,137,400 | 4,108,022 | Loaded and navigated correctly |
| Z20 PNG grid, Master 3-1 | 39,891,100 | 39,587,335 | Responsive viewing of a roughly 40 GB-class package |
| Z20 JPEG/75 grid, Master 3-2 | 4,354,360 | 4,090,206 | Clear zoom-dependent hybrid cartography in the tested locations |
| Jacksonville Metro Z20, JPEG/75 | 21,786,032 | 20,629,591 | Large single-file metropolitan hybrid map loaded in ArcGIS Earth |

**JPEG/75 is chosen while producing MBTiles, not in the converter.** The two Master grid runs are different grids, so their substantial size difference is useful production evidence, **not** a controlled identical-source image-quality or compression benchmark. Hybrid and Street map imagery compress differently. Details and remaining test limitations are in [TECHNICAL.md](TECHNICAL.md).

## What it supports

- **Input:** existing standard Web Mercator **raster** MBTiles with 256 × 256 PNG/JPEG image tiles using the TMS row convention; the implemented tiling scheme covers levels 0–23. It does **not** convert vector MBTiles, arbitrary projections or every unconventional MBTiles layout.
- **Output:** Esri Compact Cache V2 TPKX, containing indexed 128 × 128 tile bundles and the captured input zoom levels.
- **Image handling:** map tile bytes are copied unchanged. A separate presentation thumbnail is derived from a source tile. The converter does not download imagery, create new cartography, invent missing zooms or recompress the tiles.
- **Testing:** a multi-bundle synthetic color package was accepted by both ArcGIS Earth and ArcGIS Pro; real-data output from the distributed script has been field-tested extensively in ArcGIS Earth. See [TECHNICAL.md](TECHNICAL.md) for known limitations.

## Documentation and project status

- [DEMO.md](DEMO.md) — video and nontechnical four-step workflow.
- [CONTINUITY.md](CONTINUITY.md) — how to resume this project and locate the authoritative files.
- [TECHNICAL.md](TECHNICAL.md) — precise format behavior, reproducibility and test history.
- [RELEASE_CHECKLIST.md](RELEASE_CHECKLIST.md) — testing and public-release review.
- [CREDITS.md](CREDITS.md) — upstream specifications, dependencies and acknowledgments.
- [LEGAL.md](LEGAL.md) — imagery-provider rights, attribution, trademarks and intended-use limits.
- [CONTRIBUTING.md](CONTRIBUTING.md) / [SECURITY.md](SECURITY.md) — project participation and reporting.
- [LICENSE_STATUS.md](LICENSE_STATUS.md) — **the project has no selected software license yet**. Publicly viewable source code is not automatically licensed for redistribution or modification; this decision belongs to the authorized rights holder.

### Formats and attribution

The converter connects two documented formats: [Mapbox MBTiles](https://github.com/mapbox/mbtiles-spec) and Esri's published [Compact Cache V2](https://github.com/Esri/raster-tiles-compactcache) / [TPKX specification](https://github.com/Esri/tile-package-spec). Format specifications do not grant rights to third-party imagery. **Use only source imagery you are authorized to acquire, retain, convert and display for your intended purpose.** The current converter does not automatically propagate separate MBTiles attribution fields; users must meet each provider's credit requirements. No commercial imagery or proprietary example TPKX packages are distributed in this repository.

Independent project; **not affiliated with or endorsed by** Google, QGIS, Esri or Mapbox. Actual offline coverage, currency, accuracy, device operation and necessary permissions should be checked before any operational use.
