#!/usr/bin/env python3

from collections.abc import Callable
from typing import Any
import functools as ft
import operator


def spell_reducer(spells: list[int], operation: str) -> int:

    if not spells:
        return 0

    if operation == "add":
        return ft.reduce(operator.add, spells)
    if operation == "multiply":
        return ft.reduce(operator.mul, spells)
    if operation == "max":
        return ft.reduce(max, spells)
    if operation == "min":
        return ft.reduce(min, spells)

    else:
        return 0


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:

    water_spell = ft.partial(base_enchantment, power=50, element="water")
    fire_spell = ft.partial(base_enchantment, power=50, element="fire")
    ice_spell = ft.partial(base_enchantment, power=50, element="ice")

    return {
        "water": water_spell,
        "fire": fire_spell,
        "ice": ice_spell
    }


@ft.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:

    if n <= 1:
        return n

    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable[[Any], str]:

    @ft.singledispatch
    def spell(x: Any) -> str:
        return "Unknown spell type"

    @spell.register
    def _(x: int) -> str:
        return f"Damage spell: {x} damage"

    @spell.register
    def _(x: str) -> str:
        return f"Enchantment: {x}"

    @spell.register
    def _(x: list) -> str:
        return f"Multi-cast: {len(x)} spells"

    return spell


def enchantment(power: int, element: str, target: str) -> str:
    return f"{element} of power {power} used on {target}"


def main() -> None:

    spell_powers = [26, 34, 21, 48, 11, 12]
    operations = ['add', 'multiply', 'max', 'min']
    fibonacci_tests = [15, 17, 17, 3]

    print("---Spell Reducer---")
    for operation in operations:
        print(f"{operation} = {spell_reducer(spell_powers, operation)}")

    print("\n---Partial Enchanter---")
    enchanters = partial_enchanter(enchantment)
    print(enchanters["water"](target="Eudald"))
    print(enchanters["fire"](target="Brian"))
    print(enchanters["ice"](target="Beny"))

    print("\n---Fibonacci---")
    for nb in fibonacci_tests:
        print(f"Fibonacci {nb} = {memoized_fibonacci(nb)}")
        # print(memoized_fibonacci.cache_info())

    print("\n---Dispatcher---")
    dispatcher = spell_dispatcher()
    print(dispatcher(10))
    print(dispatcher("fireball"))
    print(dispatcher(operations))
    print(dispatcher({"hello": 45}))


if __name__ == "__main__":
    main()
