import math


def isPalindrome(x: int) -> bool:
    # negative numbers
    if x < 0:
        return False

    # single digit ints
    if x < 10:
        return True

    # multiply of 10
    if x % 10 == 0:
        return False
    n = x

    length = math.floor(math.log10(n)) + 1
    divider = 10 ** (length - 1)

    for _ in range(length // 2):
        if n < 10:
            return True
        most_sig = n // divider
        least_sig = n % 10

        if most_sig is not least_sig:
            return False
        else:
            # trim n
            n %= divider
            n //= 10

            # because we are trimming two sides
            # we divide the divider with 100 (10**2)
            divider //= 100

    return True


def isPalindrome2(x: int) -> bool:
    # negative numbers
    if x < 0:
        return False

    # single digit ints
    if x < 10:
        return True

    # multiply of 10
    if x % 10 == 0:
        return False

    n = x
    _n = 0

    while n > _n:
        _n += _n * 10 + n % 10
        n //= 10

    return n is _n or n is _n // 10


if __name__ == "__main__":
    isPalindrome(1000021)
