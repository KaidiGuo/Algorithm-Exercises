'''
The key to this type of higest resource using question is to find out where is the max and if the max exceed the limitation
So we can order (by position) all the resource use and free actions like [position 1, + N] [position 2, -N]
And for all the items in this list, the current position resource occupation is just the sum of item[1]
If we see a number exceed the limit, return 
'''

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



