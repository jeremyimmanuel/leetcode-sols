"""
do three at a time

RTL
123

i = 0
0-9

i = 1
10-90
ten, twenty, thirthy, forty, fifty

i = 2
one hundred - nine hundred

numberToWordsBasic(num)

"""


def numberToWords(num: int) -> str:
    def numberToWordsHundred(num: int) -> str:
        if not (1 < num < 1000):
            raise ValueError("Number must be between 1 and 999 (inclusive)")

        ones = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
        ]
        tens = [
            "",
            "Ten",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]
        teens = [
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]

        ans = []
        i = 0
        while num is not 0:
            digit = num % 10
            to_append = ""
            # ones
            if i == 0:
                to_append = ones[digit]
            if i == 1:
                # special case for the tens
                if digit == 1:
                    # eleven to nineteen
                    if len(ans) >= 1:
                        ones_place = ones.index(ans.pop())
                        to_append = teens[ones_place]
                    # special case for 'ten'
                    else:
                        to_append = teens[0]
                # 20 - 99
                else:
                    to_append = tens[digit]
            # hundreds
            if i == 2:
                to_append = ones[digit] + " Hundred"

            if to_append:
                ans.append(to_append)

            num //= 10
            i += 1
        return " ".join(ans[::-1])

    if num == 0:
        return "Zero"

    i = 0
    ans = []

    while num is not 0:
        to_append = ""
        three_digit = num % 1000
        if three_digit != 0:
            if i == 0:
                to_append = numberToWordsHundred(three_digit)
            if i == 1:  # thousand
                to_append = numberToWordsHundred(three_digit) + " Thousand"
            if i == 2:  # million
                to_append = numberToWordsHundred(three_digit) + " Million"
            if i == 3:  # billion
                to_append = numberToWordsHundred(three_digit) + " Billion"
            ans.append(to_append)

        num //= 1000
        i += 1

    return " ".join(ans[::-1])
