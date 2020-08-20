from toml import load
from pathlib import Path

with open(Path(__file__).parent / 'values.toml') as f:
    FACTIONS_BY_NAME = load(f)['Factions']

FACTIONS = [v for _, v in FACTIONS_BY_NAME.items()]

PREFERRED_EMPLOYERS = ['MagistracyOfCanopus', 'Davion', 'Marik', 'ComStar', 'Steiner']
PREFERRED_ENEMIES = ['Liao', 'ComStar', 'Kurita']
REQUIRED_ENEMIES = ['Locals']


def add_to(s: "StarSystem", p: str, v: any) -> list:
    dat = getattr(s, p)
    if p in dat:
        return
    if isinstance(dat, list):
        dat = set(dat)
        dat |= {v}
        dat = sorted(list(dat))
        setattr(s, p, dat)
        return dat


def add_employer(s: "StarSystem", name: str) -> list:
    return add_to(s, 'employers', name)
