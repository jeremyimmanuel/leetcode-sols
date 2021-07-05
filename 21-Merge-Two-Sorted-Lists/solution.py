"""
Traverse through both list
compare both elements
pick the smallest one,
append smallest to new list

while (h1 and h2 not empty)


# at the end
if h1 empty
    move every element in h2
vice versa
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = x
        self.next = None


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 == None and l2 == None:
        return None

    ans = ListNode()
    pointer = ans

    while l1 != None and l2 != None:
        # pick l1's val
        if l1.val <= l2.val:
            pointer.val = l1.val
            pointer.next = ListNode()
            l1 = l1.next
        else:
            pointer.val = l2.val
            pointer.next = ListNode()
            l2 = l2.next

        pointer = pointer.next

    if l1 == None:
        while l2 != None:
            pointer.val = l2.val
            if l2.next != None:
                pointer.next = ListNode()
                pointer = pointer.next
            l2 = l2.next
    elif l2 == None:
        while l1 != None:
            pointer.val = l1.val
            if l1.next != None:
                pointer.next = ListNode()
                pointer = pointer.next
            l1 = l1.next

    return ans
