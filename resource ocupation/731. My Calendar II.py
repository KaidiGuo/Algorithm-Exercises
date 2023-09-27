class MyCalendarTwo:

    def __init__(self):
        self.orders=[]

        

    def book(self, start: int, end: int) -> bool:
        orders=self.orders
        bisect.insort(orders,(start,1))
        bisect.insort(orders,(end,-1))
        
        limit=3
        count=0
        for item in orders:
            count+=item[1]
            if count ==limit:
                orders.pop(bisect_left(orders, (start,1)))
                orders.pop(bisect_left(orders, (end,-1)))

                return False
        return True
