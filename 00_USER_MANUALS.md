# User Manuals

The two Python utilities in this repository each have a user manual, on GitHub and as a printable PDF. Both PDFs were regenerated for the current versions on 2026-11-01; the earlier v1.0 and v3 PDFs remain in the repository's Git history.

| Tool | Python script | Windows launcher | User manual |
| --- | --- | --- | --- |
| **MBTiles to TPKX Converter 2.1** | [`mb2tpkx.py`](System%20Files/mb2tpkx.py) | [`mb2tpkx.bat`](mb2tpkx.bat) | **[Manual](MB2TPKX_USER_MANUAL.md)** / [PDF](mb2tpkx_User_Manual.pdf) |
| **Master 4 Grid Maker 2.1** | [`Master4_Grid_Maker.py`](System%20Files/Master4_Grid_Maker.py) | [`Master4_Grid_Maker.bat`](Master4_Grid_Maker.bat) | **[Manual](MASTER4_GRID_MAKER.md)** / [PDF](Master4_Grid_Maker_User_Manual.pdf) |

Both tools require **Python 3** and **Pillow**. Since v1.1.1 / v3.1.1 the launchers install Pillow automatically the first time. To install it by hand:

```powershell
py -3 -m pip install Pillow
```

The converter manual covers compatible raster MBTiles, direct conversion, safe output, every error message, and the QGIS-to-ArcGIS-Earth workflow.

The **Master 4 v3.1 manual** (see [MASTER4_V3.1_CHANGES.md](MASTER4_V3.1_CHANGES.md) for what v3.1 adds) covers:

- the 1-degree / 100-cell system;
- exact input order and no-rounding decimal cell lookup;
- deterministic production filenames;
- the numbered EPSG:3857 GeoTIFF overlay;
- the final full-box `MASTER` extent row;
- the optional Cell 55 colored **Z10-Z20 TPKX**;
- the fact that the demo TPKX is **opt-in and defaults to No**;
- the area-wide Z17 -> grid -> selected cells -> high-resolution production workflow;
- the demo TPKX's use as a teaching tool, pre-QGIS sanity check, and offline geographic/zoom reference;
- the permanent rule: reference overlays ON while planning, OFF before production.
