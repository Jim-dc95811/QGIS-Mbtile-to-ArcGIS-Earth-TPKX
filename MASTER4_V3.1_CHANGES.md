# Master 4 Grid Maker v3.1 - change document

**Released:** 2026-10-31
**Type:** hardening release. Input handling and file safety only.

**The grid itself is unchanged.** Cell numbering, extent calculation, the GeoTIFF overlay (drawing and georeferencing), the production filename pattern and the Cell 55 demo tiles are identical to v3. For the same Master 4 entry, v3.1 writes byte-identical TXT and TIF files.

`Master4_Grid_Maker.bat` is unchanged. Output still goes to `C:\downloads`.

## What changed

### 1. An interrupted Cell 55 demo no longer leaves a broken TPKX

**v3:** if the optional demo build stopped partway (Ctrl+C, a full disk, closing the program), the `...-055-ZOOM-DEMO.tpkx` was left on disk. It was a structurally valid package holding only the zoom levels written so far, for example Z10-Z15 without Z16-Z20. The next attempt refused with "Output already exists" until the file was deleted by hand.

**v3.1:** the demo is built as `<name>.tpkx.partial` and renamed only after every zoom level is complete. A failed or cancelled build deletes the partial file, so the next attempt starts cleanly.

### 2. Whole degrees typed as decimals or with leading zeros now work

**v3:** `82.0w, 81w, 30n, 31n` passed the whole-degree check, then crashed with `ERROR: invalid literal for int() with base 10: '82.0'` and left an empty TXT file. `082w, 081w, 030n, 031n` worked but named the files `Master4_082W_081W_030N_031N_...`, a second name for the same box.

**v3.1:** file names are built from the parsed values, so `82w`, `82.0w` and `082w` all produce `Master4_82W_81W_30N_31N_...` with identical contents. Non-whole entries such as `82.5w` are still rejected.

### 3. An input mistake no longer ends the session

**v3:** any error printed a message and closed the program, so the `.bat` had to be run again.

**v3.1:** the error is shown and the program asks again. A blank entry quits without creating anything. Ctrl+C at any prompt prints `Cancelled.` instead of a Python traceback. Files already created are kept.

### 4. The TXT and TIF are replaced together

**v3:** the TXT was written before the TIF. If the TIF step failed, for example because the old TIF was open in ArcGIS Earth, the result was a new TXT beside an old or missing TIF, with an unclear error.

**v3.1:** both files are written under temporary names and swapped in only after both succeed. If a file cannot be replaced, the previous pair is left untouched and the message reads:

```text
ERROR: Could not replace Master4_82W_81W_30N_31N_Grid.tif - it may be open in ArcGIS Earth or another program. Close it and try again.
```

### 5. Smaller items

- The banner shows `Master 4 Grid Maker v3.1`.
- The demo "already exists" message now says to delete or rename the old demo.
- The prompt reads `Enter Master 4 (blank to quit):`.

## Verification

- **Live acceptance:** Jim Gaddy ran v3.1 on Windows for `82w, 81w, 30n, 31n` on 2026-10-31. The grid TIF and the Cell 55 demo TPKX opened correctly in ArcGIS Earth, and the extents TXT showed the expected rows and filenames.
- **Byte-for-byte regression against v3:** TXT and TIF identical for 10 entries covering W/N, E/N and W/S boxes, both sides of the equator and the prime meridian, +/-180 degrees, +/-85 degrees, upper-case and extra-space input.
- **Owner's reference GeoTIFF:** compared with Jim's existing `82W_81W_30N_31N` grid TIF, v3.1 matches in size, pixel scale, tie point, EPSG:3857 keys, NoData and every grid-line pixel.
- **Cell 55 demo:** identical to v3 in every package entry except the random package ID, which differs on every run of either version.
- **Release zip:** extracted fresh and run end to end; output identical to v3.
- **Failure tests (42 checks in total, all passed):** decimal and leading-zero degrees; invalid entries still rejected; TIF write failure; locked TIF; interrupted demo with clean rerun; existing demo; typo then valid entry; blank entry; input closed; Ctrl+C at the demo question.
- **Verified in the test environment only:** the "may be open in ArcGIS Earth" message for a locked TIF on Windows, and the re-prompt after an input mistake.

## Checksums

| File | v3 SHA-256 | v3.1 SHA-256 |
|---|---|---|
| `Master4_Grid_Maker.py` | `16a42784005743728837d3dfdc2f3295b30071d5ed37ccbddbb9b9ee23e58888` | `5ca38785a5b5e9537dc1b3d2d79c829414efe86816f7bc0f7407fdc3cbe632e7` |
| `Master4_Grid_Maker.bat` | `abb4e7dd1f1b665e1cf1b9ee4d1bffdef40e336acb746460640be0a043c20c2d` | unchanged |
| `Master4_Grid_Maker.zip` | `408ba3e129f912b3b4ef0a7df0d6ccc478ff8935ffec9cb235232505e872e158` | `1c8da1c228aa360696136dfcaa1d2e36e2f1c9eedfc4c0642c864a4001a39ff3` |

The v3 PDF Operator Manual still applies: its workflow, outputs and demo instructions are unchanged. v3 remains available in the repository history.
