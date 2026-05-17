#!/usr/bin/env python3

from typing import Callable, Any
import functools as ft
import time


def spell_timer(func: Callable) -> Callable:

    @ft.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:

    def decorator(func: Callable) -> Callable:

        @ft.wraps(func)
        def wrapper(
            self: Any, spell_name: str, power: int, *args: Any, **kwargs: Any
        ) -> Any:

            if power >= min_power:
                return func(self, spell_name, power, *args, **kwargs)
            return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:

    def decorator(func: Callable) -> Callable:

        @ft.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:

            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            "Spell failed, retrying... (attempt"
                            f" {attempt}/{max_attempts})"
                        )
                    else:
                        return (
                            "Spell casting failed after"
                            f" {max_attempts} attempts"
                        )

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (
            len(name) >= 3 and
            name.replace(" ", "").isalpha()
        )

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:

    print("---Testing spell timer---")

    @spell_timer
    def printing() -> str:
        return "Random print"

    print(printing())

    print("\nTesting retrying spell...")

    counter = {"attempts": 0}

    @retry_spell(3)
    def unstable_spell() -> str:
        counter["attempts"] += 1
        if counter["attempts"] < 3:
            raise Exception("fail")
        return "Waaaaaaagh spelled !"

    result = unstable_spell()
    print(result)

    print("\nTesting MageGuild...")

    mage = MageGuild()

    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("Al"))

    print(mage.cast_spell("Lightning", 15))
    print(mage.cast_spell("Spark", 5))


if __name__ == "__main__":
    main()
