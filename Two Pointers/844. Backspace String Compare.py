# We don't use list and its pop() function for [:-1] because if # is at the start
# you cannot pop from empty list

class Solution:    

    def backspaceCompare(self, s: str, t: str) -> bool:
        def create(s):
            p1,p2=0,0
            s_new = ""
            for i,c in enumerate(s):
                if c != '#':
                    s_new += c  
                else:
                    s_new = s_new[:-1]
            return s_new
        return create(s) == create(t)
        
