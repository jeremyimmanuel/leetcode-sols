from typing import List, Tuple
import unittest
from solution import addTwoNumbers, ListNode


def init_test_list(l1_vals: List[int], l2_vals: List[int]):
    l1, l2 = ListNode(), ListNode()
    la, lb = l1, l2
    # Preparing test data
    for val in l1_vals:
        la.next = ListNode(val)
        la = la.next

    for val in l2_vals:
        lb.next = ListNode(val)
        lb = lb.next

    return l1.next, l2.next


class TestAddTwoNumbers(unittest.TestCase):

    # test has to start with the word `test`
    def test_same_length(self):
        """
        Check answer linked list's each node val
        """
        l1_vals = [2, 4, 3]
        l2_vals = [5, 6, 4]
        ans_vals = [7, 0, 8]

        l1, l2 = init_test_list(l1_vals, l2_vals)

        ans = addTwoNumbers(l1, l2)

        i = 0
        while ans is not None:
            self.assertEqual(ans.val, ans_vals[i])
            i += 1
            ans = ans.next
