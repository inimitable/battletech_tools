#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import pytest

from battletech.update_ss2 import build_accessor


@pytest.mark.parametrize(
    ["accessor_desc", "output"],
    [
        ('"System",0', '["System"][0]'),
        ('"Marauder","Weapons","PPCs",3', '["Marauder"]["Weapons"]["PPCs"][3]'),
    ]
)
def test_build_accessor_test(accessor_desc, output):
    assert build_accessor(accessor_desc) == output


if __name__ == "__main__":
    test_build_accessor_test()
