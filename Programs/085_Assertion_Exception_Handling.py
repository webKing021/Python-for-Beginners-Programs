# Assertion Exception Handling
x = "hello"
try:
    # if condition is false, then it will throw AssertionError
    assert x == "hello"
except AssertionError as e:
    print("Assertion failed", e)
finally:
    print("Assertion passed")