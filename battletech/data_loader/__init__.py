from toml import load, dump

with open("../values.toml", "w") as f:
    data = load(f)

    data["factions"] = [
        "AuriganPirates",
        "AuriganRestoration",
        "ComStar",
        "Davion",
        "Kurita",
        "Liao",
        "Locals",
        "MagistracyOfCanopus",
        "Marik",
        "Steiner",
        "TaurianConcordat",
    ]
    dump(data, f)
