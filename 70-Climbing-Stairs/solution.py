def climbStairs(n: int) -> int:
    one, two = 1, 1

    for _ in range(n - 1):
        one, two = one + two, one
    return one
