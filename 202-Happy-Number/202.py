from typing import List
def isHappy(n: int) -> bool:
        if n is 0:
            return False
        
        arr = getArr(n)
        
        ans = reduce(arr)
        print(f'ans : {ans}')
        s = set()
        while ans is not 1:
            arr = getArr(ans)
            print(arr)
            ans = reduce(arr)
            print(f'ans : {ans}')
            if ans in s:
                return False
            s.add(ans)
            
        return True

def reduce(arr: List) -> int:
    if len(arr) == 1:
        return arr[0]**2
    
    ans = 0
    for i in arr:
        ans += i**2
    return ans

            
def getArr(n: int) -> List:
    arr = []
    while n != 0: 
        val = n % 10
        n //= 10
        arr.append(val)
    return arr

def main():
    print(isHappy(7))

if __name__ == "__main__":
    main()