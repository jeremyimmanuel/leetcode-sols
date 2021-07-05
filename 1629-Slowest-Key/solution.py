"""
1. Find the duration of the keypress
releaseTime[i] - releaseTimes[i - 1]

edge case, where i = 0
releaseTime[i]

for timestamp in releaseTimes

tiebreaker, if duration is the same as current max duration
compare lexicograph ordder
"""

from typing import List


def slowestKey(releaseTimes: List[int], keysPressed: str) -> str:
    ans = keysPressed[0]
    max_duration = releaseTimes[0]

    for idx, ch in enumerate(keysPressed):
        if idx == 0:
            continue

        duration = releaseTimes[idx] - releaseTimes[idx - 1]
        if duration > max_duration:
            ans = ch
            # update max_duration
            max_duration = duration
        elif duration == max_duration:
            ans = max(ch, ans)

    return ans
