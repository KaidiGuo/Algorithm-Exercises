"""
use counter to find all chars that repeated only 1 time
if none, return -1
else, use string.find() function find all the index of these chars
return the minimum index
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = Counter(s)
        mim = float("inf")
        nr = [item for item in dic if dic[item] == 1]
        if not nr: return -1
        for char in nr:
            ind = s.find(char)
            mim = min(mim, ind)
        return mim