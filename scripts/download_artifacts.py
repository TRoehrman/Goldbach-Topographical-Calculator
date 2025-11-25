#!/usr/bin/env python3
import os, sys, subprocess

FOLDER_ID = os.environ.get("GB_DRIVE_FOLDER", "1BSsH8OgPti4aLu47YO4whu6RM_6XAOme")
TARGET = os.path.join(os.path.dirname(_file_), "..", "data")


def sh(*cmd):
    return subprocess.check_call(list(cmd))


if _name_ == "_main_":
    os.makedirs(TARGET, exist_ok=True)
    try:
        import gdown  # noqa: F401
    except Exception:
        sh(sys.executable, "-m", "pip", "install", "gdown>=5.2.0")
    sh(sys.executable, "-m", "gdown", "--folder", f"https://drive.google.com/drive/folders/{FOLDER_ID}", "-O", TARGET)
