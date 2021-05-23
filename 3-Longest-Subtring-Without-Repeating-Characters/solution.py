from collections import defaultdict as dd

def lengthOfLongestSubstring(s: str) -> int:
    l, r = 0, 0
    exists = dd(lambda : False)

    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    ans = 0

    # we right at the legth of s because
    # we need `r` for slicing s
    while r <= len(s):
        if (l is r):
            r += 1
            continue
        sub_s = s[l:r]
        sub_s_length = len(sub_s)
        right_ch = sub_s[-1]
        # if char already exists in substr, move left pointer
        if exists[right_ch]:
            while s[l] != right_ch:
                exists[s[l]] = False
                l += 1
            # take index after dup as starting
            l += 1
        else:
            exists[right_ch] = True

            # update ans
            if (sub_s_length > ans):
                ans = sub_s_length

        r += 1
    return ans

if __name__ == '__main__':
    print(lengthOfLongestSubstring(s='nfpdmpi'))