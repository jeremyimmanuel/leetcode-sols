from typing import List
from enum import Enum


class Logs(Enum):
    DIGITS = "digits"
    LETTERS = "letters"


# "a1 9 2 3 1"
def getLogType(s: str) -> bool:
    arr = s.split()
    log_content = arr[1]
    if log_content.isdigit():
        return Logs.DIGITS
    else:
        return Logs.LETTERS


def getLogContent(s: str) -> str:
    return " ".join(s.split()[1:])


def getLogId(s: str) -> str:
    return s.split()[0]


def reorderLogFiles(logs: List[str]) -> List[str]:
    digits = []
    letters = []
    for log in logs:
        if getLogType(log) is Logs.DIGITS:
            digits.append(log)
        else:
            letters.append(log)
    letters.sort(key=lambda log: (getLogContent(log), getLogId(log)))
    return [*letters, *digits]


def main():
    test1 = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
    test2 = [
        "dig1 8 1 5 1",
        "let1 art zero",
        "dig2 3 6",
        "let2 own kit dig",
        "let3 art zero",
    ]
    ans = reorderLogFiles(test2)
    print(ans)


if __name__ == "__main__":
    main()
