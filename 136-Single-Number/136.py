from collections import defaultdict as dd

def singleNumber(nums: List[int]) -> int:
    # d = dd(list)
    # for num in nums:
    #     if num in d:
    #         del d[num]
    #     else:
    #         d[num]
    
    # return list(d.keys())[0]
    d = dd(int)
    for n in nums:
        d[n] += 1
    
    for k in d:
        if d[k] == 1:
            return k
    
    return -1