#!/usr/bin/env python3
"""Resmi ama eğlenceli birim testleri."""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_tohum_tekrarlanabilir():
    sys.path.insert(0, str(ROOT))
    from btk_usb import deneme_yap

    a = deneme_yap(5, tohum=7)
    b = deneme_yap(5, tohum=7)
    assert [(x.yon, x.basarili, x.ihlal_puani) for x in a] == [
        (x.yon, x.basarili, x.ihlal_puani) for x in b
    ]


def test_ilk_iki_hemen_hemen_ters():
    sys.path.insert(0, str(ROOT))
    from btk_usb import deneme_yap

    d = deneme_yap(2, tohum=1)
    assert all(not x.basarili for x in d)


def test_cli_calisir():
    r = subprocess.run(
        [sys.executable, str(ROOT / "btk_usb.py"), "-n", "3", "--tohum", "3"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert "USB Yön Spektrumu" in r.stdout
    assert "Kayyum Grok" in r.stdout
    assert r.returncode in (0, 1)


if __name__ == "__main__":
    test_tohum_tekrarlanabilir()
    test_ilk_iki_hemen_hemen_ters()
    test_cli_calisir()
    print("tüm resmi testler geçti — spektrum sakin")
