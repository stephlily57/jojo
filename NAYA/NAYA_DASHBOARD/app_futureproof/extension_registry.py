# -*- coding: utf-8-sig -*-
EXTENSIONS = []

def register_extension(name: str):
    if name not in EXTENSIONS:
        EXTENSIONS.append(name)

def list_extensions():
    return EXTENSIONS
