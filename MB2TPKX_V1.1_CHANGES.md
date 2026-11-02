# mb2tpkx v1.1 - change document

**Released:** 2026-10-31
**Type:** hardening release. Error handling and file safety only.

**The conversion itself is unchanged.** The code that reads tiles, flips TMS rows to XYZ, builds the 128 x 128 Compact Cache V2 bundles and copies image bytes is identical, line for line, to v1.0. v1.1 produces the same TPKX as v1.0 from the same MBTiles.

`mb2tpkx.bat` is unchanged.

## What changed

### 1. Failed runs no longer leave a broken TPKX behind

**v1.0:** if a conversion stopped partway (a corrupt tile, a full disk, Ctrl+C), the output `.tpkx` was left on disk. It was a structurally valid package containing only the zoom levels written so far, so it could look like a normal map. The next run then refused to start with "Output already exists" until the file was deleted by hand.

**v1.1:** the package is built as `<name>.tpkx.partial` and renamed to `<name>.tpkx` only after every tile is written and the final tile count checks out. Any failure or Ctrl+C deletes the partial file, so the next run starts cleanly. If the console window is closed outright, a `.tpkx.partial` file may remain. ArcGIS Earth does not treat it as a map, and the next run replaces it.

### 2. File and folder names containing `#` or `%` now work

**v1.0:** the MBTiles path was placed directly into an SQLite file address. A `#` in any folder or file name cut the path short. The converter then opened the wrong path without read-only protection, created an empty stray file, and failed with a misleading `no such table: metadata`. A `%` could cause similar problems.

**v1.1:** the path is escaped before opening, so any valid Windows name works and the source MBTiles is always opened read-only.

### 3. Plain error messages instead of Python tracebacks

Common problems now print one line starting with `ERROR:` and exit with code 1, which the `.bat` reports as "Conversion failed". Examples:

```text
ERROR: Output already exists: Bryceville.tpkx - delete or rename it and run again.
ERROR: MBTiles file not found: Brycevile.mbtiles
ERROR: Could not read notes.mbtiles as an MBTiles database (file is not a database).
ERROR: Unsupported image format at z12 (1119, 2409)
ERROR: Pillow is not installed. Install it with: py -3 -m pip install Pillow
CANCELLED: no output file was kept.
```

Unexpected internal errors still show a full traceback, so real bugs remain diagnosable.

### 4. Smaller items

- The MBTiles database connection is closed explicitly when conversion ends.
- The console prints `mb2tpkx 1.1` at the start of each run.

## Verification

- **Live acceptance:** Jim Gaddy converted `bryceville_7_layer_mbtile.mbtiles` with v1.1 on Windows and opened the result in ArcGIS Earth, 2026-10-31.
- **Real-data regression:** the same Bryceville file (6,461 JPEG tiles, Z8-Z20) was converted by v1.0 and v1.1. All 14 tile bundles, `root.json` and the thumbnail were byte-identical. The only difference was the package GUID in `iteminfo.json`, which is randomly generated on every run by both versions. All 6,461 tiles were separately unpacked from the v1.1 output and confirmed byte-for-byte identical to the source, at the correct tile position.
- **Synthetic test suite (27 checks, all passed):** regression against v1.0 with PNG, JPEG and multi-zoom inputs; corrupt tile mid-run; Ctrl+C mid-run; leftover `.partial` from an earlier run; names containing `#`, `%`, spaces and `&`; read-only access confirmed; missing file; output already exists (existing file left untouched); not a database; SQLite file that is not MBTiles; empty tile table; 512 px tiles; same input and output path; Pillow not installed.
- **Not yet live-tested on Windows:** the `#`/`%` file-name fix. It was verified in the test environment only.

## Checksums

| File | v1.0 SHA-256 | v1.1 SHA-256 |
|---|---|---|
| `mb2tpkx.py` | `c04dc9f3c1ad74b4180b11465df1189a74c500a5d5873d66a57c2d4076fb3670` | `b2efa752a6f386b6bada84532efe8ee56fed3c9863fa3c6dd76f51129e85f785` |
| `mb2tpkx.bat` | `078e07834b6fa45f8e63192f60033ac5c322ea236372df22cece8be8a24fda66` | unchanged |

v1.0 remains available in the repository history.

## v1.1.1 - launcher update (2026-11-02)

`mb2tpkx.py` is unchanged (v1.1, SHA-256 above). Only `mb2tpkx.bat` changed:

- finds Python through `py -3`, or `python` when the `py` launcher is not installed, and says so plainly if neither exists
- if Pillow is missing, installs it once (`Pillow is not installed yet. Installing it now - one time only...`); if that fails, prints the command to give to IT and stops
- then runs the converter exactly as before (drag-and-drop or typed path)

Live-tested by Jim Gaddy on Windows, 2026-11-02 (including the one-time install after uninstalling Pillow).

| File | v1.1.1 SHA-256 |
|---|---|
| `mb2tpkx.bat` | `7321c148bc3c41ea1f1646ab7f8c84168f08baf1bd36dd06b28b88ae4b90172e` |
| `mb2tpkx.zip` | `3ff8dfa6e0b00a17e6c51fe2adf968f75b2b9ce9233baf1ca6e4bf04a992e9fb` |
