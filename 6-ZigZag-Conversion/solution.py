def convert(s: str, numRows: int) -> str:
    arr = [[] for _ in range(numRows)]
    delta = 1
    arr_idx = 0

    for ch in s:
        arr[arr_idx].append(ch)

        if arr_idx is 0:
            delta = 1
        elif arr_idx == len(arr) - 1:
            delta = -1
        arr_idx += delta

    ans = ""
    for subarr in arr:
        ans += "".join(subarr)
    return ans
