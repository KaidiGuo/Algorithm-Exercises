# Learning how to use OrderedDict() and its popitem(last=False) function to pop the first in element


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = collections.OrderedDict()
        

    def get(self, key: int) -> int:
        if key in self.dict:
            v = self.dict[key]
            del self.dict[key]
            self.dict[key] = v
            return self.dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            del self.dict[key]
            self.dict[key] = value
            
        else:
            if len(self.dict) >= self.capacity:
                self.dict.popitem(last=False)
            self.dict[key] = value
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)