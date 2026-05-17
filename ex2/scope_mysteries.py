#!/usr/bin/env python3

from typing import Callable


def mage_counter() -> Callable:

    count: int = 0

    def counter() -> int:

        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:

    power: int = initial_power

    def accumulator(additional_power: int) -> int:

        nonlocal power
        power += additional_power
        return power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:

    def enchantment(item_name: str) -> str:

        return f"{enchantment_type} {item_name}"

    return enchantment


def memory_vault() -> dict[str, Callable]:

    vault: dict[str, int] = {}

    def store(key: str, value: int) -> None:
        vault[key] = value

    def recall(key: str) -> int | str:
        return vault.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall
    }


def main() -> None:

    print("---Testing Counter---\n")
    counter1 = mage_counter()
    counter2 = mage_counter()
    print(f"Counter 1 = {counter1()}")
    print(f"Counter 1 = {counter1()}")
    print(f"Counter 2 = {counter2()}")

    print("\n---Testing Accumulator---\n")
    accumulator = spell_accumulator(5)
    print(f"Run 1 = {accumulator(1)}")
    print(f"Run 2 = {accumulator(2)}")
    print(f"Run 3 = {accumulator(3)}")

    print("\n---Testing Enchantements---\n")
    print("Levitating Factory")
    enchantment1 = enchantment_factory("Levitating")
    print(f"    Sword = {enchantment1("Sword")}")
    print(f"    PC = {enchantment1("PC")}")
    print(f"    Student = {enchantment1("Student")}")

    print("\nFrozen Factory")
    enchantment2 = enchantment_factory("Frozen")
    print(f"    Sword = {enchantment2("Sword")}")
    print(f"    PC = {enchantment2("PC")}")
    print(f"    Student = {enchantment2("Student")}")

    print("\n---Testing Vault---\n")
    vault = memory_vault()
    print("Storing 5 swords")
    vault["store"]("sword", 5)
    print(f"Storage sword count: {vault["recall"]("sword")}")
    print(f"Storage helmet count: {vault["recall"]("helmet")}")


if __name__ == "__main__":
    main()
