'''
Very same to 438.
Maintain a window dict that is the same length of the target substring
shifting the window 
+1 to value of existed char on j+l position
-1 to value of existed char on j position
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return
        target = defaultdict(int)
        window = defaultdict(int)
        l = len(s1)
        for index,char in enumerate(s1):
            target[char] +=1
            window[s2[index]] +=1
        
        for i in range(len(s2)-l+1):
            if target == window:
                return True

            if i+l >= len(s2):
                pass
            else: 
                window[s2[i+l]] +=1
                window[s2[i]] -=1
                if window[s2[i]] ==0:
                    window.pop(s2[i])
        return False 