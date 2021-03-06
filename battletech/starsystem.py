#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import json
from os.path import expanduser, expandvars
from pathlib import Path
from shutil import copy
from sys import platform
from typing import Callable, List, NewType as Type, Tuple, TypeVar
from battletech.biomes import BIOMES, Climate

_BLACK_MARKET = "itemCollection_faction_AuriganPirates"


class StarSystem:
    def __init__(self, system_data: dict, file: Path):
        self.data = {**system_data}
        d = self.data
        self.file = file
        self._bak_file = self.file.parent / (self.file.name + ".bak")
        self.name = d["Description"]["Name"]
        self.employers = d["contractEmployerIDs"]
        self.targets = d["contractTargetIDs"]
        self._difficulty = d["DifficultyList"]

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)

    @classmethod
    def from_file(cls, file: Path):
        system_data = json.load(file.open())
        return cls(system_data, file)

    # ****** BEGIN AUTOGENERATED CODE ****** #

    @property
    def name(self) -> str:
        return self.data["Description"]["Name"]

    @name.setter
    def name(self, value: str):
        self.data["Description"]["Name"] = str(value)

    @property
    def biomes(self) -> list:
        return self.data["SupportedBiomes"]

    @biomes.setter
    def biomes(self, value: list):
        self.data["SupportedBiomes"] = list(value)

    @property
    def difficulty(self) -> int:
        return self.data["DefaultDifficulty"]

    @difficulty.setter
    def difficulty(self, value: int):
        self.data["DefaultDifficulty"] = int(value)

    @property
    def difficulty_campaign(self) -> int:
        return self.data["DifficultyList"][0]

    @difficulty_campaign.setter
    def difficulty_campaign(self, value: int):
        self.data["DifficultyList"][0] = int(value)

    @property
    def difficulty_career(self) -> int:
        return self.data["DifficultyList"][1]

    @difficulty_career.setter
    def difficulty_career(self, value: int):
        self.data["DifficultyList"][1] = int(value)

    @property
    def jump_distance(self) -> int:
        return self.data["JumpDistance"]

    @jump_distance.setter
    def jump_distance(self, value: int):
        self.data["JumpDistance"] = int(value)

    @property
    def owner(self) -> str:
        return self.data["ownerID"]

    @owner.setter
    def owner(self, value: str):
        self.data["ownerID"] = str(value)

    @property
    def shop_item_types(self) -> list:
        return self.data["SystemShopItems"]

    @shop_item_types.setter
    def shop_item_types(self, value: list):
        self.data["SystemShopItems"] = list(value)

    @property
    def shop_refresh_rate(self) -> int:
        return self.data["ShopRefreshRate"]

    @shop_refresh_rate.setter
    def shop_refresh_rate(self, value: int):
        self.data["ShopRefreshRate"] = int(value)

    @property
    def shop_specials(self) -> int:
        return self.data["ShopMaxSpecials"]

    @shop_specials.setter
    def shop_specials(self, value: int):
        self.data["ShopMaxSpecials"] = int(value)

    @property
    def tags(self) -> list:
        return self.data["Tags"]["items"]

    @tags.setter
    def tags(self, value: list):
        self.data["Tags"]["items"] = list(value)

    @property
    def employers(self) -> list:
        return self.data["contractEmployerIDs"]

    @employers.setter
    def employers(self, value: list):
        self.data["contractEmployerIDs"] = list(value)

    @property
    def targets(self) -> list:
        return self.data["contractTargetIDs"]

    @targets.setter
    def targets(self, value: list):
        self.data["contractTargetIDs"] = list(value)

    @property
    def market_items(self) -> list:
        return self.data["SystemShopItems"]

    @market_items.setter
    def market_items(self, value: list):
        self.data["SystemShopItems"] = list(value)

    @property
    def num_special_items(self) -> int:
        return self.data["ShopMaxSpecials"]

    @num_special_items.setter
    def num_special_items(self, value: int):
        self.data["ShopMaxSpecials"] = int(value)

        # ****** END AUTOGENERATED CODE ****** #

    def get_black_market(self):
        val = self.data["BlackMarketShopItems"]
        return val if val else []

    def set_black_market(self, value):
        self.data["BlackMarketShopItems"] = value

    def add_markets(self, val: str or list or None = _BLACK_MARKET, append=True):
        """Adds a market or list of markets to this system's available market."""
        if isinstance(val, str):
            val = [val]
        if append:
            val = set(self.get_black_market() + val)
        self.data["SystemShopItems"] = sorted(list(val))

    def _as_dict(self):
        return self.__dict__

    def __str__(self):
        return f'Star system "{self.name}" (difficulty {self.difficulty_career / 2:.1f}), {self.shop_specials} items'

    def save(self, safe=True):
        """Super-safe saving."""
        if not safe:
            return json.dump(self.data, self.file.open(), indent=2)

        json.dump(self.data, self._bak_file.open("w"), indent=2)
        self.file.unlink()  # unlink = delete
        copy(self._bak_file, self.file)
        if self.file.exists():
            self._bak_file.unlink()

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not exc_type:
            self.save()


if platform == "darwin":
    DATA_BASE = Path(r"/Users/rob/Desktop/starsystem")
else:
    DATA_BASE = Path(r"S:\Steam\Steamapps\common\BATTLETECH\BattleTech_Data")


def expandall(p: str, Path):
    return expandvars(expanduser(str(p)))


# Typing
S = TypeVar("S", list, StarSystem)
StarSystemName = Type("UserRequest", str)


def parse_systems_request(request: str):
    request = StarSystemName(request.strip().casefold())
    if request == "*":
        return get_all_systems()
    else:
        return [get_system(request)]


PlanetName = Type("PlanetName", str)
StarSystemResult = Tuple[S, Callable[[S], List[StarSystem]]]

DATA_DIR = Path(DATA_BASE) / "StreamingAssets/data/starsystem"
ORIG_DATA_PKL = DATA_DIR / "orig.pkl"


def get_all_systems() -> List[StarSystem]:
    out = list()
    for file in DATA_DIR.iterdir():
        try:
            out.append(StarSystem.from_file(file))
        except (json.decoder.JSONDecodeError, PermissionError, FileNotFoundError):
            pass
    return out


def get_system(name: StarSystemName):
    name = name.casefold()
    for file in DATA_DIR.iterdir():
        if name in file.name.casefold():
            return StarSystem.from_file(file)


if __name__ == "__main__":
    from battletech.factions import LIAO
    from random import random
    good_biomes = set()
    for biome in BIOMES.values():
        if biome.climate in [Climate.NORMAL, Climate.COLD, Climate.WET]:
            good_biomes.add(biome.value)

    for system in get_all_systems():
        if system.owner == LIAO:
            if system.difficulty_career <= 8 and random() > 0.5:
                system.difficulty_career //= 2
                system.save()
                print(system)
