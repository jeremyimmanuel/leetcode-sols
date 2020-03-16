from typing import List

def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    ans = set()
    s1, s2 = set(nums1), set(nums2)
    small = s1 if len(s1) < len(s2) else s2
    big = s1 if len(s1) >= len(s2) else s2

    while len(small) > 0:
        num = small.pop()
        if num in big:
            ans.add(num)

    return list(ans)

def test1():
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    ans = [2]
    res = intersection(nums1, nums2)
    print(res)
    assert  res == ans

def test2():
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    ans = [9, 4]
    res = intersection(nums1, nums2)
    print(res)
    assert  res == ans

def main():
    test1()

if __name__ == "__main__":
    main()
