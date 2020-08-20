#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from textwrap import dedent as _dedent
from battletech.starsystem import StarSystem, parse_systems_request as _parse_system_request


if __name__ == '__main__':

    # Select our desired system(s)
    biomes = set()
    user_input = input(_dedent("""Please select the system(s) you wish to modify.
    Systems can be comma-separated to act on many different systems, may be matched via regex with
    an input starting with /, or with * for all. 
    \tEnter the system(s) to modify. > """))
    selected_systems = _parse_systems_request(user_input)
    for system in selected_systems:
        system: StarSystem
        # with system:
        # if 20 >= system.number_of_shop_items <= 6:
        #     system.number_of_shop_items *= 2
        #     system.add_markets()
        # system.add_markets()
        biomes |= set(system.biomes)
    pprint(biomes)
