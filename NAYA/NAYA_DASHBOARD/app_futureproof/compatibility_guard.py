# -*- coding: utf-8-sig -*-
import sys

def check_python():
    major, minor = sys.version_info[:2]
    if major < 3 or minor < 11:
        raise RuntimeError("Python 3.11+ required")

check_python()
