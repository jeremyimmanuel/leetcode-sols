"""
Merge multiple linked list

just like merging two sorted list but on steroids
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


import heapq
from typing import List


def mergeKLists(lists: List[ListNode]) -> ListNode:
    if len(lists) == 0:
        return None

    pq = []
    for linked_list in lists:
        pointer = linked_list
        while pointer != None:
            heapq.heappush(pq, pointer.val)
            pointer = pointer.next
    if len(pq) == 0:
        return None
    ans = ListNode()
    pointer = ans
    while len(pq) != 0:
        val = heapq.heappop(pq)
        pointer.val = val
        if len(pq) != 0:
            pointer.next = ListNode()
        pointer = pointer.next

    return ans
