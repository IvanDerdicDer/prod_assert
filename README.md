# prod_assert

# The What?

prod_assert is a Python library containing prod safe assert function.
This library contains asserts functions as prod_assert (the base assert), assert_eq, assert_in, etc.
Asserts in this library, by default, raise AssertionFailed excetption, with the option to raise AssertionError.

# The Why?

A senior at work annoyed me by saying I can't use assert in prod, so here are asserts I can use in prod.

# Example

```python
from prod_assert import assert_eq

# Nothing happens
assert_eq(1, 1)

# Assert fails and raises AssertionFailde with the default message
assert_eq(1, 2)
### prod_assert._main.AssertionFailed: Condition 1 == 2 is false

# Assert fails and raises AssertionFailed with the custom message
assert_eq(1, 2, "One does not equal two")
### prod_assert._main.AssertionFailed: One does not equal two

# Assert fails and raises AssertionError with the default message
assert_eq(1, 2, assertion_exception=AssertionError)
### AssertionError: Condition 1 == 2 is false

```
