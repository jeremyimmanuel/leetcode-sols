class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def isPalindrome(self, head: ListNode) -> bool:
    arr = []
    curr = head
    while curr != None:
        arr.append(curr.val)
        curr = curr.next
    return arr == arr[::-1]

def main():
    pass

if __name__ == "__main__":
    pass