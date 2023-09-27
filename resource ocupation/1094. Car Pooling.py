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

