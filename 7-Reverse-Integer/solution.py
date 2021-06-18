def reverse(x: int) -> int:
    neg = x < 0
    n = abs(x)

    arr = []
    while n > 9:
        arr.append(n % 10)
        n //= 10
    arr.append(n)

    power = len(arr) - 1
    ans = 0
    for num in arr:
        ans += num * (10 ** power)
        power -= 1
    if ans > 2 ** 31 - 1:
        return 0
    return -ans if neg else ans
