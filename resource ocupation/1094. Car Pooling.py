class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        orders=[]
        for p, st, en in trips:
            orders.append((st,p))
            orders.append((en,-p))

        orders.sort()
        p=0
        for item in orders:
            p += item[1]
            if p > capacity:
                return False
            
        return True

        maxlen=0
        sub=[]
        dic={}
        st=0
        ed=0
        for i,char in enumerate(s) :
            if char not in dic:
                dic[char] = i
                maxlen = max(len(dic),maxlen)
            else:
                ed=dic[char]+1
                for p in range(st,ed):
                    dic.pop(s[p])
                dic[char]=i
                st=ed
        return maxlen