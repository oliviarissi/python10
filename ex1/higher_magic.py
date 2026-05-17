#!/usr/bin/env python3

from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple[Callable, Callable]:
        return (
            spell1(target, power),
            spell2(target, power)
        )
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> Callable:
        return (base_spell(target, power * multiplier))
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditioned(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return conditioned


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        all: list[str] = []
        for spell in spells:
            all.append(spell(target, power))
        return all
    return sequence


def strong_enough(target: str, power: int) -> bool:
    return power >= 20


def fireball(target: str, power: int) -> str:
    return f"Fireball burns {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def lightning(target: str, power: int) -> str:
    return f"Lightning strikes {target} for {power} damage"


def freeze(target: str, power: int) -> str:
    return f"Freeze traps {target} in ice with power {power}"


def main() -> None:

    target: str = "Dragon"
    power: int = 5

    print("Testing spell combiner...")
    combined: Callable = spell_combiner(fireball, heal)
    print(combined(target, power))

    print("\nTesting power amplifier...")
    amplified: Callable = power_amplifier(fireball, 5)
    print(amplified(target, power))

    print("\nTesting conditional caster...")
    conditioned: Callable = conditional_caster(strong_enough, heal)
    print(conditioned(target, power))

    print("\nTesting spell sequence...")
    spells: list[Callable] = [fireball, lightning, freeze]
    sequenced: Callable = spell_sequence(spells)
    print(sequenced(target, power))


if __name__ == "__main__":
    main()
