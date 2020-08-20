import io

from battletech.starsystem import StarSystem, get_all_systems
from battletech.biomes import BIOMES_BY_NAME
from json import load, dump

bad_biomes = [BIOMES_BY_NAME['Lunar']]

BLACK_MARKET = "itemCollection_faction_AuriganPirates"


systems = get_all_systems()

employers = set()
for system in systems:
    with system:  # StarSystem

        for faction in 'Liao,Locals'.split(','):
            if faction not in system.targets:
                system.targets = list(set(system.targets) | {faction})

        if 'Locals' in system.employers and len(system.employers) > 2:
            system.employers.remove('Locals')

        for bad_biome in bad_biomes:
            if bad_biome in system.biomes:
                try:
                    system.biomes.remove(bad_biomes)
                except ValueError:
                    pass
        if 'polarFrozen' not in system.biomes:
            system.biomes.append('polarFrozen')

        system.jump_distance = 1

        system.add_markets()
        system.shop_specials = min(20, system.shop_specials * 2)

        print(f"""{system.name} ({system.jump_distance})

    HOSTILES:
    {', '.join(system.targets)}          
    FRIENDS:
    {', '.join(system.employers)}
    """)

# with open('..\\data\\data.json', 'w') as f:
#     try:
#         _data = load(f)
#     except io.UnsupportedOperation:
#         _data = dict()
#     _data['employers'] = employers = sorted(list(employers))
#     dump(_data, f)
