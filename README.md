# camera-calibration-patterns

SVG pattern generator for camera calibration (checkerboard, radon checkerboard, circles, asymmetric circles, charuco board), packaged as a Python library and CLI.

- 📦 PyPI package: `camera-calibration-patterns`
- 🐍 Module: `camera_calibration_patterns`
- 🖥️ CLI: `generate-pattern`

Based on OpenCV’s `gen_pattern.py` script, refactored and packaged as a standalone Python library + CLI.

## 🚀 Installation

### Option 1: pipx (recommended for CLI use)
```bash
pipx install camera-calibration-patterns
# then:
generate-pattern -h
```

### Option 2: pip (as a library)
```bash
pip install camera-calibration-patterns
```

### Option 3: from GitHub
```bash
pipx install "git+https://github.com/victor1234/camera-calibration-patterns.git@v0.1.0"
```

### Requirements:
- Python >= 3.11

## 🧰 CLI

Generate a 9x7 checkerboard with 25 mm square size:
```bash
generate-pattern -T checkerboard -r 9 -c 7 -s 25 -u mm -o chess_9x7_25mm.svg
```

Generate a 4×11 radon checkerboard with 15 mm square size:
```bash
generate-pattern -T radon_checkerboard -r 15 -c 12 -s 15 -u mm -m 5 7 5 8 6 7 radon_15x12_15mm.svg
```

Generate a 15×6 asymmetric circle grid with 15 mm diameter:
```bash
generate-pattern -T acircles -r 15 -c 6 -s 15 -u mm -R 3 -o acircles_15x6_15mm.svg
```

Show all options:
```bash
generate-pattern -h
```

> Tip: Print SVGs with **no scaling** to ensure square sizes match the specified units (`mm`/`in`).

## ⚙️ CLI Options

| Flag | Description | Example |
|------|-------------|---------|
| `-o output` | Output SVG filename | `-o pattern.svg` |
| `-c columns` | Pattern columns | `-c 9` |
| `-r rows` | Pattern rows | `-r 7` |
| `-T {circles,acircles,checkerboard,`<br>`radon_checkerboard,charuco_board}` | Pattern type | `-T checkerboard` |
| `-u {mm,inches,px,m}` | Units for size | `-u mm` |
| `-s square_size` | Size of squares in pattern | `-s 20` |
| `-R radius_rate` | Circles_radius = square_size/radius_rate | `-R 0.8` |
| `-w page_width` | Page width in units | `-w 210` |
| `-h page_height` | Page height in units | `-h 297` |
| `-a {A0,A1,A2,A3,A4,A5}` | Page size, supersedes -h -w arguments | `-a A4` |
| `-m markers [markers ...]` | List of cells with markers for the radon checkerboard | `-m 0 1 2 3` |
| `-p aruco_marker_size` | Size of ArUco markers | `-p 10` |
| `-f dict_file` | file name of custom aruco dictionary for ChAruco pattern | `-f custom_dict.yml` |
| `-H` | Show help | `-H` |


## License

This package is licensed under the Apache License 2.0 (see [LICENSE](./LICENSE)).

This project includes code from:
- `gen_pattern.py` by [OpenCV](https://github.com/opencv/opencv), licensed under the Apache License 2.0.
- `svgfig.py` by Jim Pivarski — licensed under the BSD 3-Clause License.

The code has been modified and packaged as a Python library by Victor Kataev in 2025.
