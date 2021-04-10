#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from dataclasses import dataclass
from enum import Enum
from pprint import pprint


class Climate(Enum):
    COLD = "cold"
    WET = "wet"
    NORMAL = "normal"
    HOT = "hot"
    MARTIAN = "martian"
    VACUUM = "vacuum"

    def __repr__(self):
        return f"{self.name}"


__biomes = {
    "Badlands": ("badlandsParched", Climate.HOT),
    "Desert": ("desertParched", Climate.HOT),
    "Fall Highlands": ("highlandsFall", Climate.NORMAL),
    "Spring Highlands": ("highlandsSpring", Climate.NORMAL),
    "Jungle": ("jungleTropical", Climate.WET),
    "Fall Lowlands": ("lowlandsFall", Climate.NORMAL),
    "Spring Lowlands": ("lowlandsSpring", Climate.NORMAL),
    "Lunar": ("lunarVacuum", Climate.VACUUM),
    "Martian": ("martianVacuum", Climate.MARTIAN),
    "Polar": ("polarFrozen", Climate.COLD),
    "Tundra": ("tundraFrozen", Climate.COLD),
    "urbanHighTech": ("urbanHighTech", Climate.NORMAL),
}


@dataclass
class Biome:
    name: str
    value: str
    climate: Climate


BIOMES = {name: Biome(name, *data) for name, data in __biomes.items()}

ALL_BIOMES = [biome.name for biome in BIOMES.values()]

pprint(BIOMES)
