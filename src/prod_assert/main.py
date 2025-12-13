class AssertionFailed(Exception):
    pass


def prod_assert(condition: bool, message: str) -> None:
    """
    Function that takes a condition and checks if it is True.
    If the condition is False the function raises AssertionFailed exception.

    :param condition: Condition to check.
    :type condition: bool
    :param message: Message to display if check fails.
    :type message: str
    :raises ValueError: If condition is not bool.
    :raises ValueError: If message is not str.
    :raises AssertionFailde: If condition is False
    """
    if not isinstance(condition, bool):
        raise ValueError("Paramater condition is not bool")

    if not isinstance(message, str):
        raise ValueError("Paramater message is not bool")

    if condition:
        return

    raise AssertionFailed(message)

