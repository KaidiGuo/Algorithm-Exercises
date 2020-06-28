'''
Methods: travers the string, create all longest-none-repeating-character-substring that ends with each character
example: for string "abcbb"
we would have "a","ab","abc","cb","b" for each character

Use a dictionary to track all the chars in the current substring
for char in string s, if this char is not in the dic, add dic[char]=index to the dic, maxlen = max(len(dic),maxlen)
if this char is in the dic, get the index of this existed char using dic[char] = index, pop everything before/include this index
meaning, find the longest-none-repeating-character-substring end with this char
and do not forget to re-append this char into the dic with current new index
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        dic={}
        st=0
        ed=0
        for i,char in enumerate(s) :
            if char not in dic:
                dic[char] = i
                maxlen = max(len(dic),maxlen)
            else:
                ed = dic[char]+1
                for p in range(st,ed):
                    dic.pop(s[p])
                dic[char]=i
                st = ed
        return maxlen