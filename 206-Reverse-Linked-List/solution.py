# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode) -> ListNode:
    h = head
    prev = None

    while h != None:
        next_node = h.next
        h.next = prev
        prev = h
        h = next_node

    return prev
