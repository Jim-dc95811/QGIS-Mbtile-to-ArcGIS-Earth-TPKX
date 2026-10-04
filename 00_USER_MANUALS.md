# Official User Manuals

The two Python utilities in this repository each have a matching **Official PDF User Manual**. Keep the manual with its script and Windows launcher.

| Tool | Python script | Windows launcher | Official PDF manual |
| --- | --- | --- | --- |
| **MBTiles to TPKX Converter** | [`mb2tpkx.py`](mb2tpkx.py) | [`mb2tpkx.bat`](mb2tpkx.bat) | **[`mb2tpkx_User_Manual.pdf`](mb2tpkx_User_Manual.pdf)** |
| **Master 4 Grid Maker** | [`Master4_Grid_Maker.py`](Master4_Grid_Maker.py) | [`Master4_Grid_Maker.bat`](Master4_Grid_Maker.bat) | **[`Master4_Grid_Maker_User_Manual.pdf`](Master4_Grid_Maker_User_Manual.pdf)** |

Both tools require **Python 3** and **Pillow**. Install Pillow once with:

```powershell
py -3 -m pip install Pillow
```

The converter manual covers compatible MBTiles, conversion, output behavior, common errors, and the QGIS-to-ArcGIS-Earth workflow.

The Master 4 manual covers the 1-degree / 100-cell system, exact input order, **no-rounding decimal cell lookup**, production-manifest filenames, the numbered EPSG:3857 overlay, and the QGIS batch workflow.
