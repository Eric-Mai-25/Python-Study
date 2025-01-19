from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)  # Mark as recently used
            return self.cache[key]
        return -1  # Key not found
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)  # Update usage order
        self.cache[key] = value
        if len(self.cache) > self.capacity:  # Evict least recently used
            self.cache.popitem(last=False)

# Example
lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))  # 1
lru.put(3, 3)      # Evicts key 2
print(lru.get(2))  # -1
print(lru.get(3))  # 3