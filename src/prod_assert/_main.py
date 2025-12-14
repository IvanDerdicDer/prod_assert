from typing import Any, Optional, Union


class AssertionFailed(Exception):
    pass


AssertionException = Union[AssertionFailed, AssertionError]


def prod_assert(
    condition: bool,
    message: str,
    assertion_exception: AssertionException=AssertionFailed
) -> None:
    """
    Function that takes a condition and checks if it is True.
    If the condition is False the function raises AssertionFailed exception.

    :param condition: Condition to check.
    :type condition: bool
    :param message: Message to display if check fails.
    :type message: str
    :param assertion_exception: Exeption to be raised when the assertion fails.
    :type assertion_exception: AssertionException
    :raises ValueError: If condition is not bool.
    :raises ValueError: If message is not str.
    :raises ValueError: If assertion_exception is not AssertionFailed or AssertionError
    :raises AssertionException: If condition is False
    """
    if not isinstance(condition, bool):
        raise ValueError("Paramater condition is not bool")

    if not isinstance(message, str):
        raise ValueError("Paramater message is not bool")

    if (assertion_exception != AssertionFailed) and (assertion_exception != AssertionError):
        raise ValueError("Parameter assertion_exception in not AssertionFalied or AssertionError")

    if condition:
        return

    raise assertion_exception(message)


def assert_eq(
    a: Any,
    b: Any,
    message: Optional[str]=None,
    assertion_exception: AssertionException=AssertionFailed
) -> None:
    """
    Function that checks if a equals b.
    A custom message can be provided. The default message is 'Condition {a} == {b} is false'.

    :param a: Any value.
    :type a: Any
    :param b: Any value.
    :type b: Any
    :param message: Optional custom message.
    :type message: Optional[str]
    :raises AssertionFailed: If a does not equals b.
    """


    if message is None:
        message = f'Condition {a} == {b} is false'
    prod_assert(a == b, message, assertion_exception)
    

def assert_not_eq(
    a: Any,
    b: Any,
    message: Optional[str]=None,
    assertion_exception: AssertionException=AssertionFailed
) -> None:
    """
    Function that checks if a does not equals b.
    A custom message can be provided. The default message is 'Condition {a} != {b} is false'.

    :param a: Any value.
    :type a: Any
    :param b: Any value.
    :type b: Any
    :param message: Optional custom message.
    :type message: Optional[str]
    :raises AssertionFailed: If a equals b.
    """


    if message is None:
        message = f'Condition {a} != {b} is false'
    prod_assert(a != b, message=message, assertion_exception=assertion_exception)

