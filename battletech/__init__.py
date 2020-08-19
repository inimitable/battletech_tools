#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from typing import Tuple, Callable, TypeVar, List, NewType as Type
from pathlib import Path
import json
from textwrap import dedent

from battletech.starsystem import StarSystem

# Typing
S = TypeVar('S', list, StarSystem)
UserRequest = Type('UserRequest', str)
PlanetName = Type('PlanetName', str)
StarSystemResult = Tuple[S, Callable[[S], List[StarSystem]]]

DATA_BASE = Path(r'S:\Steam\Steamapps\common\BATTLETECH\BattleTech_Data')
DATA_DIR = DATA_BASE  / "\StreamingAssets\data\starsystem"
ORIG_DATA_PKL = DATA_DIR / 'orig.pkl'


def get_all_systems():
    out = list()
    for file in DATA_DIR.iterdir():
        try:
            out.append(StarSystem.from_file(file))
        except (json.decoder.JSONDecodeError, PermissionError, FileNotFoundError):
            pass
    return out


def get_system(name: UserRequest):
    for file in DATA_DIR.iterdir():
        if name in file.name.casefold():
            return StarSystem.from_file(file)


def parse_systems_request(request: str):
    request = UserRequest(request.strip().casefold())
    if request == "*":
        return get_all_systems()
    else:
        return [get_system(request)]


if __name__ == '__main__':

    # Select our desired system(s)
    user_input = input(dedent("""Please select the system(s) you wish to modify.
    Systems can be comma-separated to act on many different systems, may be matched via regex with
    an input starting with /, or with * for all. 
    \tEnter the system(s) to modify. > ')"""))
    selected_systems = parse_systems_request(user_input)
    for system in selected_systems:
        system: StarSystem
        with system:
            if 40 >= system.number_of_shop_items <= 6:
                system.number_of_shop_items *= 2
                system.add_markets()
        system.add_markets()
        system.save()
