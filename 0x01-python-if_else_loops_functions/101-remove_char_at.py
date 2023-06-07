#!/usr/bin/python3
# 101-remove_char_at.py


def remove_char_at(str, n):
    """Create a copy of the string without the character at position n."""
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])


=========================

102-magic_calculation.py

#!/usr/bin/python3
# 102-magic_calculation.py


def magic_calculation(a, b, c):
    """Match bytecode provided by Holberton School."""
    if a < b:
        return (c)
    if c > b:
        return (a + b)
    return (a*b - c)

