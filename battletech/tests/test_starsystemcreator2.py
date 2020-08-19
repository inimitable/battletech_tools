#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from battletech.update_ss2 import build_accessor
import pytest


@pytest.mark.parametrize([
    ('"System",0', '["System"][0]'),
    ('"Marauder","Weapons","PPCs",3', '["Marauder"]["Weapons"]["PPCs"][3]')
    ])
def build_accessor_test(accessor_desc, output):
    assert build_accessor(accessor_desc) == output


if __name__ == '__main__':
    build_accessor_test()
