# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getDecimalValue(head: ListNode) -> int:
    pointer = head
    bin_number = ""

    while pointer != None:
        bin_number += str(pointer.val)
        pointer = pointer.next

    return int(bin_number, 2)
