'''
move right pointer while adding visited to a map; compare max maxlen on the way with len(map)
when reaching a visited one, find the initial index
move and pop the left pointer to the initial index+1
add the new duplicate and nex index to the visited map

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        left,right=0,0
        dict ={}
        for right in range(len(s)):
            c = s[right]
            if c not in dict:
                dict[c] = right
                maxlen = max(maxlen,len(dict))
            else:
                mark = dict[c]+1
                                
                for i in range(left,mark):
                    dict.pop(s[i])
                dict[c] = right
                left = mark
        
        return maxlen






        