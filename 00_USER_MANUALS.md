# Official User Manuals

The two Python utilities in this repository each have a matching **Official PDF User Manual**. Keep the manual with its script and Windows launcher.

| Tool | Python script | Windows launcher | Official PDF manual |
| --- | --- | --- | --- |
| **MBTiles to TPKX Converter** | [`mb2tpkx.py`](mb2tpkx.py) | [`mb2tpkx.bat`](mb2tpkx.bat) | **[`mb2tpkx_User_Manual.pdf`](mb2tpkx_User_Manual.pdf)** |
| **Master 4 Grid Maker v3** | [`Master4_Grid_Maker.py`](Master4_Grid_Maker.py) | [`Master4_Grid_Maker.bat`](Master4_Grid_Maker.bat) | **[`Master4_Grid_Maker_User_Manual.pdf`](Master4_Grid_Maker_User_Manual.pdf)** |

Both tools require **Python 3** and **Pillow**. Install Pillow once with:

```powershell
py -3 -m pip install Pillow
```

The converter manual covers compatible raster MBTiles, direct conversion, output behavior, common errors, and the QGIS-to-ArcGIS-Earth workflow.

The **Master 4 v3 Operator Manual** covers:

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
