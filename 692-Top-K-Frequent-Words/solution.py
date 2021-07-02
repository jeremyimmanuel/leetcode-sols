"""
1. Get count of each word
2. Sort by count -> alphabetically
3. Slice first k elements
4. Return array of only the words
"""


from typing import List
from collections import defaultdict as dd


def topFrequent(words: List[str], k: int) -> List[str]:
    count_dict = dd(int)
    for w in words:
        count_dict[w] += 1
    return list(
        map(
            lambda pair: pair[0],
            sorted(count_dict.items(), key=lambda pair: (-pair[1], pair[0]))[:k],
        )
    )
