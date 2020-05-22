import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.length = 0
        self.dict = {}
        self.storage = DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        node = self.dict[key]
        self.storage.move_to_end()
        if node:
            return node
        else: 
            return None
    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if self.length < self.limit:
            self.dict[key] = value
            self.storage.add_to_head(value)
            self.length += 1
        elif key in self.dict.keys():
            self.dict[key] = value
        else: 
            new_dict = {key:val for key, val in self.dict.items() if self.storage.tail.value != val}
            self.dict = new_dict
            self.dict[key] = value
            self.storage.add_to_head(value)
            self.storage.tail.delete()

lru = LRUCache(2)
lru.set('item1', 1)
lru.set('item2', 2)
lru.set('item3', 3)
lru.set('item3', 4)
print(lru.dict)