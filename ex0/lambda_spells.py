#!/usr/bin/env python3


def artifact_sorter(artifacts: list[dict]) -> list[dict]:

    return sorted(
        artifacts, key=lambda artifact: artifact["power"], reverse=True
    )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:

    return list(
        filter(lambda mage: mage["power"] >= min_power, mages)
    )


def spell_transformer(spells: list[str]) -> list[str]:

    return list(
        map(lambda spell: "* " + spell + " *", spells)
    )


def mage_stats(mages: list[dict]) -> dict:

    if not mages:
        return {
            "max_power": 0,
            "min_power": 0,
            "avg_power": 0.0
        }

    max_power: int = max(mages, key=lambda mage: mage["power"])["power"]

    min_power: int = min(mages, key=lambda mage: mage["power"])["power"]

    avg_power: float = round(
        sum(map(lambda mage: mage["power"], mages)) / len(mages), 2
    )

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power,
    }


def main() -> None:

    artifacts: list[dict] = [
        {"name": "A", "power": 3, "type": "aa"},
        {"name": "C", "power": 2, "type": "cc"},
        {"name": "B", "power": 5, "type": "bb"},
        {"name": "E", "power": 4, "type": "ee"},
        {"name": "D", "power": 1, "type": "dd"},
    ]

    print("---SORTED---")
    print(artifact_sorter(artifacts))

    print("\n---FILTERED---")
    print(power_filter(artifacts, 3))

    spells: list[str] = ["water", "gold", "alohomora"]

    print("\n---TRANSFORMED---")
    print(spell_transformer(spells))

    print("\n---STATS---")
    print(mage_stats(artifacts))


if __name__ == "__main__":
    main()
