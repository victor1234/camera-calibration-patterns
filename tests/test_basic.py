import os
import sys
import tempfile

from camera_calibration_patterns import gen_pattern


def test_generate_checkerboard_creates_svg(monkeypatch):
    with tempfile.TemporaryDirectory() as tmpdir:
        output = os.path.join(tmpdir, "pattern.svg")
        test_args = [
            "generate-pattern",
            "-o",
            output,
            "-r",
            "3",
            "-c",
            "4",
            "-T",
            "circles",
            "-s",
            "10",
            "-u",
            "mm",
        ]

        # Patch sys.argv
        monkeypatch.setattr(sys, "argv", test_args)
        gen_pattern.main()

        # Check that the file was created
        assert os.path.exists(output)

        # Check that the file contains SVG content
        content = open(output).read()
        assert "<svg" in content

        # Check for the expected number of squares (3 rows * 4 columns)
        assert content.count("<circle") == 3 * 4
