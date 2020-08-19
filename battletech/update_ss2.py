#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import typing
from re import compile as regex

ONLY_DIGITS = regex('\d+')

__ACCESSOR_TEMPLATE = \
    """
    @property
    def {name}(self) -> {type}:
        return self.data{accessors}
    
    @{name}.setter
    def {name}(self, value: {type}):
        self.data{accessors} = {type}(value) 
    """

__ACCESSORS = {
    'name':              (str, 'Description', 'Name'),
    'biomes':            (list, 'SupportedBiomes',),
    'difficulty':        (int, 'DefaultDifficulty',),
    'difficulty_low':    (int, 'DifficultyList', 0),
    'difficulty_high':   (int, 'DifficultyList', 1),
    'jump_distance':     (int, 'JumpDistance',),
    'owner':             (str, 'ownerID'),
    'shop_item_types':   (list, 'SystemShopItems'),
    'shop_refresh_rate': (int, 'ShopRefreshRate'),
    'shop_specials':     (int, 'ShopMaxSpecials'),
    'tags':              (list, 'Tags', 'items'),
    }


def try_number(s: str) -> (bool, int):
    if ONLY_DIGITS.match(s):
        num = int(s)
        return num, True
    return s, False


class LineFeeder:
    """Creates a big string, adding to it line-by-line."""

    def __init__(self, s: str = None):
        self.s = s if s else ""

    def add(self, line):
        if not self.s.endswith("\n"):
            sep = '\n'
        else:
            sep = ''
        self.s = f"{self.s}{sep}{line}\n"

    def reset(self):
        self.s = ""

    def print(self):
        print(self.s)


def build_accessor(accessor_format: str):
    """Ugly function to create dict accessors from simple strings."""
    out = "["
    for item in accessor_format[1:]:
        if isinstance(item, str):
            item = f'"{item}"'
            type_ = 'str'
        elif isinstance(item, int):
            type_ = 'int'
        else:
            type_ = 'list'
        out = f"{out}{item}]["
    return out[:-1], type_


if __name__ == '__main__':
    pass
    # feeder = LineFeeder()
    # for name, accessor_fmt in __ACCESSORS.items():
    #     accessor, accessor_type = build_accessor(accessor_fmt)
    #     feeder.add(__ACCESSOR_TEMPLATE.format(name=name, accessors=accessor, type=accessor_type))
    # feeder.print()

