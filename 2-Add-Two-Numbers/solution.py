class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    la, lb = l1, l2
    l3 = ListNode()
    lc = l3
    carry = 0

    while la != None or lb != None:
        la_val = 0 if la is None else la.val
        lb_val = 0 if lb is None else lb.val

        total = la_val + lb_val + carry
        carry = total // 10
        new_val = total % 10

        lc.next = ListNode(val=new_val)
        if la is not None:
            la = la.next
        if lb is not None:
            lb = lb.next
        lc = lc.next

    if carry > 0:
        new_node = ListNode(carry)
        lc.next = new_node
        lc = lc.next

    return l3.next
