from toml import load
from dataclasses import dataclass
from pathlib import Path

with open(Path(__file__).parent / 'values.toml') as f:
    FACTIONS_BY_NAME = load(f)['Factions']

NAMES_BY_FACTION = {v: k for k, v in FACTIONS_BY_NAME.items()}
FACTIONS = [v for _, v in FACTIONS_BY_NAME.items()]
EMPLOYERS = ["Davion", "Kurita", "Liao", "AuriganPirates", "Steiner", "Marik", "ComStar", "AuriganRestoration"]


@dataclass
class Faction:
    id: str
    has_rep: bool = True
    rep_matters: bool = True


    @property
    def is_target(self):
        return not (self.has_rep or not self.rep_matters)

    def is_employer(self):
        return self.id in EMPLOYERS


# Here comes the tedious part!
# {'Locals', 'Liao', 'Kurita', 'TaurianConcordat', 'Davion', 'MagistracyOfCanopus', 'Steiner', 'Marik', 'AuriganPirates', 'ComStar', 'AuriganRestoration'}
FEDERATED_SUNS = FEDSUNS = DAVION = 'Davion'
CAPELLAN_CONFEDERATION = CAPELLANS = LIAO = "Liao"
DRACONIS_COMBINE = KURITANS = KURITA = "Kurita"
MAGISTRACY_OF_CANOPUS = CANOPIANS = CANOPUS = "MagistracyOfCanopus"
LYRAN_COMMONWEALTH = LYRANS = STEINER = "Steiner"
FREE_WORLDS_LEAGUE = FREE_WORLDS = MARIK = "Marik"
AURIGAN_PIRATES = PIRATES = OUTLAWS = "AuriganPirates"
SHADY_SPACE_WIZARD_ILLUMINATI = COMSTAR = "Comstar"
AURIGAN_RESTORATION = AURIGAN = KEONA = "AuriganRestoration"

PLANETARY_GOVERNMENT = 'Locals'
TAURIANS = 'TaurianConcordat'


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
