# Get the partition
# when i see a letter
# stop when is i see last instance of that letter

# every new letter that comes after the letter i'm watching, it's last instance
# has to be before the last intacne of the ltter i'm watching

# keep track of the last instance of the ltters
# can we use a dictionary
# last['a'] -> 0

# we were wathcing defg, starting in index 5, we watch for our stop (at first it was 10, now it was 11)
# if we reach 11 and the stop is still 11, we partition
# check d -> 10
# check e -> 11
# check f -> 7
# check g -> 9
# check h -> 15

# do I add h to the watchlist or do i partition it there

# d e f

# when do i stop

from typing import List


def partitionLabels(s: str) -> List[int]:
    ans = []
    last = {}
    for idx, ch in enumerate(s):
        last[ch] = idx

    stop = 0
    start = 0
    for idx, ch in enumerate(s):
        # expand stop point
        stop = max(last[ch], stop)

        # if we're at the stop
        if idx == stop:
            # we partition
            partition = s[start : stop + 1]
            ans.append(len(partition))
            start = stop + 1

    if len(s[start : stop + 1]) is not 0:
        ans.append(len(s[start : stop + 1]))

    return ans
