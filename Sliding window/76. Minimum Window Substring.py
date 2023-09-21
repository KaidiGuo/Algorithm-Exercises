class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left,right=0,0
        
        target=collections.defaultdict(int)
        for item in t:
            target[item]+=1
        
        window=collections.defaultdict(int)
        
        valid=0

        start, length = 0, float('inf')
        while right < len(s):
            c = s[right]
            right += 1
            if c in target:
                window[c]+=1
                if target[c]==window[c]:
                    valid+=1
            
            while valid == len(target):
                if right - left < length:
                    start = left
                    length = right - left
                    print(f"__{start},{length}")
                d = s[left]
                left +=1
                if d in target:
                    if target[d] == window[d]:
                        valid -= 1
                    window[d] -=1
                    print(f"valid change, current char is {left}:{d}")
                    print(f"current rright is {right}")

        print(f"{start}, {length}")
        return "" if length == float('inf') else s[start:start + length]



                