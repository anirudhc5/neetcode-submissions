class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dct = OrderedDict()
        

    def get(self, key: int) -> int:
        if key in self.dct: 
            ans = self.dct[key]
            self.dct.move_to_end(key)
            return ans
        return -1
        

    def put(self, key: int, value: int) -> None:
        self.dct[key] = value
        self.dct.move_to_end(key)
        if len(self.dct) > self.capacity: 
            self.dct.popitem(last=False)
        
