class AssertionFailed(Exception):
    pass


def prod_assert(condition: bool, message: str) -> None:
    if not isinstance(condition, bool):
        raise ValueError("Paramater condition is not bool")

    if not isinstance(message, str):
        raise ValueError("Paramater message is not bool")

    if condition:
        return

    raise AssertionFailed(message)

