# 1. map the words to the letter
# 2. find if it's consistent in the string


def wordPattern(pattern: str, s: str) -> bool:
    # mapping
    d = {}
    length = len(pattern)
    s_arr = s.split()

    # if length is different, then definately False
    if length != len(s_arr):
        return False

    for idx in range(length):
        ch = pattern[idx]
        word = s_arr[idx]

        if ch in d.keys():
            # check if the value is the same with the existing value in the dictionary
            if word != d[ch]:
                return False
        # new ch
        else:
            # if word already in dict (since it's a bijection mapping)
            if word in d.values():
                return False
            else:
                d[ch] = word
    return True
