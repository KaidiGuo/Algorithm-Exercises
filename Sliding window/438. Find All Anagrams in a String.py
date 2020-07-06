"""
create a window with the same length of p on s, window[i,j],
create two hash map for p and current window, compare two hash map
if same, means p is an anagram of current window, add start index of current window to result list
if not same, move window[i,j] to [i+1,j+1]
to save some space and time, no need to recreate the whole hash map of new window on each move,
just minus 1 of the oldest char=s[i]'count or pop it if the count is 1 from window's hash map,
and add 1 to the count of new char=s[j+1] or add it if not yet in the map to window's hash map

The following two parts are the same. just one use counter, one use dictionary
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = len(p)
        dicp = Counter(p)
        window = Counter(s[:l - 1])
        result = []
        for i in range(len(p) - 1, len(s)):
            window[s[i]] += 1
            if dicp == window:
                result.append(i - len(p) + 1)
            window[s[i - len(p) + 1]] -= 1
            if window[s[i - len(p) + 1]] == 0:
                window.pop(s[i - len(p) + 1])
        return result


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        l = len(p)
        dicp = {}
        for c in p:
            if c not in dicp:
                dicp[c] = 1
            else:
                dicp[c] += 1
        dics = {}
        for i in range(l - 1):
            if s[i] not in dics:
                dics[s[i]] = 1
            else:
                dics[s[i]] += 1
        result = []
        for i in range(l - 1, len(s)):
            char = s[i]
            if char not in dics:
                dics[char] = 1
            else:
                dics[char] += 1
            if dics == dicp:
                result.append(i - l + 1)
            oldchar = s[i - l + 1]
            if dics[oldchar] > 1:
                dics[oldchar] -= 1
            else:
                dics.pop(oldchar)
        return result