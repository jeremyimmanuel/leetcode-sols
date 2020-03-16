from collections import defaultdict as dd
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = dd(lambda : 0)
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.d[timestamp] += 1
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        print(f'getHits for {timestamp}...')
        ans = 0
        start = max(1, timestamp - 299)
        print(f'start at {start}')
        for k in self.d.keys():
            if k <= timestamp and k >= start:
                print(f'key : {k}; val : {self.d[k]}')
                ans += self.d[k]
        return ans

def main():
    counter: HitCounter = HitCounter()

    #  hit at timestamp 1.
    counter.hit(1)

    # hit at timestamp 2.
    counter.hit(2)

    # hit at timestamp 3.
    counter.hit(3)

    # get hits at timestamp 4, should return 3.
    counter.getHits(4)

    # hit at timestamp 300.
    counter.hit(300)

    # get hits at timestamp 300, should return 4.
    counter.getHits(300)

    # get hits at timestamp 301, should return 3.
    counter.getHits(301) 

if __name__ == "__main__":
    main()
    