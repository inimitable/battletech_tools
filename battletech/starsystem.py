#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from pathlib import Path
import json
from shutil import copy

BLACK_MARKET = "itemCollection_faction_AuriganPirates"

class StarSystem:
    def __init__(self, system_data: dict, file: Path):
        self.data = {**system_data}
        d = self.data
        self.file = file
        self._bak_file = self.file.parent / (self.file.name + '.bak')
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

    @property
    def name(self):
        return self.data["Description"]["Name"]

    @name.setter
    def name(self, value):
        self.data["Description"]["Name"] = str(value)

    @property
    def biomes(self) -> list:
        return self.data["SupportedBiomes"]

    @biomes.setter
    def biomes(self, value):
        self.data["SupportedBiomes"] = str(value)

    @property
    def difficulty(self):
        return self.data["DefaultDifficulty"]

    @difficulty.setter
    def difficulty(self, value):
        self.data["DefaultDifficulty"] = str(value)

    @property
    def difficulty_low(self):
        return self.data["DifficultyList"][0]

    @difficulty_low.setter
    def difficulty_low(self, value):
        self.data["DifficultyList"][0] = int(value)

    @property
    def difficulty_high(self):
        return self.data["DifficultyList"][1]

    @difficulty_high.setter
    def difficulty_high(self, value):
        self.data["DifficultyList"][1] = int(value)

    @property
    def jump_distance(self):
        return self.data["JumpDistance"]

    @jump_distance.setter
    def jump_distance(self, value):
        self.data["JumpDistance"] = str(value)

    @property
    def owner(self):
        return self.data["ownerID"]

    @owner.setter
    def owner(self, value):
        self.data["ownerID"] = str(value)

    @property
    def shop_item_types(self):
        return self.data["SystemShopItems"]

    @shop_item_types.setter
    def shop_item_types(self, value):
        self.data["SystemShopItems"] = str(value)

    @property
    def shop_refresh_rate(self):
        return self.data["ShopRefreshRate"]

    @shop_refresh_rate.setter
    def shop_refresh_rate(self, value):
        self.data["ShopRefreshRate"] = str(value)

    @property
    def shop_specials(self):
        return self.data["ShopMaxSpecials"]

    @shop_specials.setter
    def shop_specials(self, value):
        self.data["ShopMaxSpecials"] = str(value)

    @property
    def tags(self):
        return self.data["Tags"]["items"]

    @tags.setter
    def tags(self, value):
        self.data["Tags"]["items"] = str(value)

    @property
    def number_of_shop_items(self):
        return self.data["ShopMaxSpecials"]

    @number_of_shop_items.setter
    def number_of_shop_items(self, val):
        self.data["ShopMaxSpecials"] = val

    @property
    def difficulty_min(self):
        return self._difficulty[0]

    @property
    def difficulty_max(self):
        return self._difficulty[1]

    @difficulty_min.setter
    def difficulty_min(self, value):
        self._difficulty[0] = value

    @difficulty_max.setter
    def difficulty_max(self, value):
        self._difficulty[1] = value

    def _get_black_market(self):
        val = self.data["BlackMarketShopItems"]
        return val if val else []

    def _set_black_market(self, value):
        self.data["BlackMarketShopItems"] = value

    def add_markets(self, val: str or list or None = BLACK_MARKET, append=True):
        """Adds a market or list of markets to this system's available market."""
        if isinstance(val, str):
            val = [val]
        if append:
            val = set(self._get_black_market() + val)
        self.data["SystemShopItems"] = sorted(list(val))

    def _as_dict(self):
        return self.__dict__

    def __str__(self):
        return f"Star system \"{self.name}\" (difficulty {(self.difficulty_max + 1) / 2:.1f}), {self.number_of_shop_items} items"

    def save(self, safe=True):
        """Super-safe saving."""
        if not safe:
            return json.dump(self.data, self.file.open(), indent=2)

        json.dump(self.data, self._bak_file.open('w'), indent=2)
        self.file.unlink()  # unlink = delete
        copy(self._bak_file, self.file)
        if self.file.exists():
            self._bak_file.unlink()


    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not exc_type:
            self.save()
