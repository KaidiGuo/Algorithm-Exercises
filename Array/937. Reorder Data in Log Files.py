class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits=[]
        letters=[]
        for e in logs:
            if e.split()[1].isdigit():
                digits.append(e)
            else:
                letters.append(e)
        
        letters.sort(key = lambda x : (x.split()[1:],x.split()[0]))
        return letters+digits
# Knowing how to sort list using multiple keys with lambda function