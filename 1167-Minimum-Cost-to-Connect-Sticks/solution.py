"""
the coast of adding a + b = (a+b)

ex:
try doing the smallest possible transaction
[1,2,3,4,5]

1+2 = 3
[3,3,4,5]

3+3 = 6
[4,5,6]

4+6=10
[5,10]


6+9 = 15
[15]

total = 33

The greedy part is to add the two smallest number each time.
We want to minimize a+b

Edge case:
len(sticks) == 1 -> return 0


sort ascending
add first two

Priority queue, the lesser the number the higher priority

stop when len(sticks) == 1

"""
import heapq
from typing import List


def connectSticks(sticks: List[int]) -> int:
    total_cost = 0
    heapq.heapify(sticks)

    while len(sticks) > 1:
        a = heapq.heappop(sticks)
        b = heapq.heappop(sticks)
        ab_sum = a + b
        total_cost += ab_sum
        heapq.heappush(sticks, ab_sum)

    return total_cost
