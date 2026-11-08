# mb2tpkx 2.1 and Master 4 Grid Maker 2.1 - what changed

**Released 2026-11-08** after Jim's live test (re-hardening pass). Downloads keep their names: [`mb2tpkx.zip`](mb2tpkx.zip) and [`Master4_Grid_Maker.zip`](Master4_Grid_Maker.zip). The 2.0 zips are in [`archive/`](archive/).

Both programs are protected baselines. **What they make is unchanged:** every TPKX tile bundle, `root.json` and thumbnail from mb2tpkx 2.1 is byte-identical to 2.0 (only the random package ID differs, as on every run), and Master 4's TXT, TIF and Cell 55 demo are byte-identical for every box tested.

## mb2tpkx 2.1

| # | Before (2.0) | Now (2.1) |
|---|---|---|
| 1 | No disk check: a 40 GB conversion on a too-full drive ran a long time, then failed with "No space left on device". | Disk space is checked before any work (tile bytes + 4 bytes per tile + 128 KB per bundle + 50 MB); a too-full drive stops at once with a plain message. |
| 2 | One line per bundle (`z17 tile/... complete`), no idea how far along. | `bundle 812 of 4,630 (17%) - z17 tile/...` |
| 3 | An existing TPKX stopped the run: delete it yourself. | `... already exists ... Replace it? [y/N]` - Y builds over it, N or Enter keeps it. A TPKX held open by ArcGIS Earth is caught **before** building. |
| 4 | An empty tile record showed `AttributeError: 'NoneType'...`. | `Tile z16 (x, y) is empty - the MBTiles is damaged. Make it again in QGIS.` |

## Master 4 Grid Maker 2.1

| # | Before (2.0) | Now (2.1) |
|---|---|---|
| 5 | `-82,-81,30,31` -> only `Invalid coordinate: -82`. | Adds `Type the box like 82w, 81w, 30n, 31n (west, east, south, north - whole degrees with a letter).` |

## Live test (Jim, 2026-11-08)

Kit `mb2tpkx_and_Master4_v2.1_TEST.zip`: TEST_1_Bryceville.mbtiles converted with the bundle count and opened in ArcGIS Earth (labelled Z10-Z16 tiles over Bryceville); TEST_2_Damaged.mbtiles stopped with the damaged-tile message; Master 4 showed the typing example for `82,81,30,31`. The disk check needs a nearly full drive, so it was proven by the rig only.

## Proof here

Rig [`tools/test-rigs/mb2tpkx_master4_test_v21.py`](https://github.com/Jim-dc95811/ArcGIS-Earth-Unlocked/blob/main/tools/test-rigs/mb2tpkx_master4_test_v21.py) (ArcGIS Earth Unlocked): 21 checks ALL PASS - a 1,546-tile JPEG + PNG MBTiles in 10 bundles converted by 2.0 and 2.1 (all bundles, root and thumbnail identical), the Replace answers (No / Enter / Yes / locked), the disk check, the damaged tile; Master 4 boxes 82w-81w 30n-31n, 10e-11e, south, and the equator/prime-meridian box 1w-0e 0n-1n.

## New baseline checksums (SHA-256)

| File | 2.1 |
|---|---|
| `System Files/mb2tpkx.py` | `ca6d11791a457a68ccbdaa15a9dbb2bc42090bf8dac5eef47c4445db071692fd` |
| `mb2tpkx.bat` | `22d6126cc80976364f4b5a2cbf7114979ecd04780871e12f416a16bec2dd6f69` |
| `mb2tpkx.zip` | `6229d3e86ae891245ebbc89ccad66b6fa038c2ad7191872339d40a0fa0367d29` |
| `System Files/Master4_Grid_Maker.py` | `2b719c30842c9809d6974c54b55aa40e24d7ca269af8e98f9defbc7982f9eae4` |
| `Master4_Grid_Maker.bat` | `ef0be1f6e7c48ca0d46bb19f80070753daf5a5e0ae27e643ba36832fe5034284` |
| `Master4_Grid_Maker.zip` | `54e68bab63a1724d44c35bed2d2a65c227e8518d45ffbe3314d1b5e261fc7694` |
