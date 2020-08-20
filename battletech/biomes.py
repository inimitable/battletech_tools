#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from toml import load
from pathlib import Path

with open(Path(__file__).parent / 'values.toml') as f:
    BIOMES_BY_NAME = load(f)['Biomes']

ALL_BIOMES = [v for _, v in BIOMES_BY_NAME.items()]

if __name__ == '__main__':
    print(BIOMES_BY_NAME)
