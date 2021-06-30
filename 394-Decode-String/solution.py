"""
1. Get multiplier
2. Get string

"""


from typing import Tuple


def solve(s: str) -> str:
    i = 0
    ans = ""
    while i < len(s):
        if s[i].isdigit():
            multiplier, num_digits = get_multiplier(s[i:])
            # move iterator to idx right behind opening square bracket
            i += num_digits - 1

            substring = get_square_bracket_string(s[i + 1 :])
            ans += multiplier * solve(substring[1:-1])

            # move iterator to idx next to closing bracket
            i += len(substring) + 1
        else:
            ans += s[i]
        i += 1
    return ans


def get_multiplier(s: str) -> Tuple[int, int]:
    i = 0
    ch = s[i]
    ans = ""
    while ch != "[":
        ans += ch
        i += 1
        ch = s[i]
    return int(ans), len(ans)


def get_square_bracket_string(s: str) -> str:
    """
    s is guaranteed to start with an opening
    square bracket '['

    1. Use a stack to determine where the outer most closing bracket is
    2. When you see a '[', append to stack
    3. When you see a ']', pop stack

    """
    i = 1
    ans = "["
    stack = ["["]
    while len(stack) != 0:
        if s[i] == "[":
            stack.append("[")
        elif s[i] == "]":
            stack.pop()
        ans += s[i]
        i += 1
    return ans


def main():
    # print(get_square_bracket_string("[a][asdf3[d]fd]2[dasdf]"))
    # print(solve("3[a2[c]]"))
    print(solve("3[a]2[bc]"))
    print(get_multiplier("100[leetcode]"))
    print(solve("10[leetcode]"))


if __name__ == "__main__":
    main()
