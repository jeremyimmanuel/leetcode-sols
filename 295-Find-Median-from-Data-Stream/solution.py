"""
[1,2,3,4,5,6,7,8,9,10,11]
split into to separate parts

[1,2,3,4,5,6], [7,8,9,10,11]
median is 6
or maxheap.heappop()

assumption

the length of maxheap and minheap can only be the same or have 
a diff by one element

in this case we are going to assume the maxheap will be the one with
the extra element when needed

so either
len(maxheap) == len(minheap), or # even
len(maxheap) == len(minheap) + 1 # odd

findMedian:
    # even
    (maxheap.heappop() + minheap.heappop()) / 2

    # odd
    maxheap.heappop()

addNum:
    maxHeap: [4]
    minHeap: [10]

    toAdd: [2, 6, 8, 11, 1]
    2, we put 2 in maxHeap because 2 < 4
        [2, 4]
        [10]
    6, we put 5 in minheap because 6 > 4
        [2, 4]
        [6, 10]
        compare 6 with maxheappeak -> greater, so it should be in minheap
        compare 6 with minheappeak (10) -> less, so just put in minheap
    8,
        [2, 4]
        [6, 8, 10] # this is wrong because we broke our constraint

        [2, 4, 6]
        [8, 10] # correct because constraint is kept

        compare 8 with maxheappeak -> greater, so it should live in minheap
        compare 8 with minheappeak -> greater, so we pop minheap, and move it to maxheap

    11,
        compare 11 with maxheappeak (6) -> greate, so it should be in minheap
        compare 11 with minheappeak (8) -> greater, just add to minheap
        check if even or odd,
        even:
            we cannot just add it to minheap
        odd:
            just add to minheap


[2, 4]
[6]
.push(8)

[2, 4]
[6, 8]

-----

[2, 4]
[6]

.push(3), compare to maxheappeak, less
pop maxheap
move to minheap
push num to maxheap
[2, 3]
[4, 6]
"""


import heapq


class MaxHeap:
    @staticmethod
    def heappush(heap, item):
        heapq.heappush(heap, -item)

    @staticmethod
    def heappop(heap):
        return -heapq.heappop(heap)


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []

    @property
    def maxheappeak(self) -> int:
        return -self.maxheap[0]

    @property
    def minheappeak(self):
        return self.minheap[0]

    @property
    def isEven(self):
        return self.length % 2 == 0

    @property
    def length(self):
        return len(self.maxheap) + len(self.minheap)

    def __len__(self):
        return self.length

    def addNum(self, num: int) -> None:
        # first value
        if len(self.maxheap) == 0:
            MaxHeap.heappush(self.maxheap, num)
            return

        # when odd
        if not self.isEven:
            # compare with maxheappeak
            # if greater than maxheappeak, then add to minheap
            if num > self.maxheappeak:
                heapq.heappush(self.minheap, num)
            else:
                toMove = MaxHeap.heappop(self.maxheap)
                heapq.heappush(self.minheap, toMove)

                MaxHeap.heappush(self.maxheap, num)
        # when even
        else:
            # if num is greater than maxheappeak, then it should be in minheap
            # however, we'll break constraint, so we gotta move some stuff first
            if num > self.maxheappeak:
                # if num is greater than minheappeak,
                # pop minheap, move that to maxheap
                if num > self.minheappeak:
                    toMove = heapq.heappop(self.minheap)
                    MaxHeap.heappush(self.maxheap, toMove)

                    heapq.heappush(self.minheap, num)
                else:
                    MaxHeap.heappush(self.maxheap, num)
            else:
                MaxHeap.heappush(self.maxheap, num)

    def findMedian(self) -> float:
        if self.isEven:
            return (self.maxheappeak + self.minheappeak) / 2

        return self.maxheappeak


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
