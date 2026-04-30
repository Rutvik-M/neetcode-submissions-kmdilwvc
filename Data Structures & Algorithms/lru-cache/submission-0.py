class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # Map key -> Node
        
        # Setup dummy nodes
        self.left = Node(0, 0)  # LRU indicator
        self.right = Node(0, 0) # MRU indicator
        
        # Wire the dummies to point at each other initially
        self.left.next = self.right
        self.right.prev = self.left

    # Helper function to remove a node from the linked list
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node

    # Helper function to insert a node at the right (MRU position)
    def insert(self, node):
        prev_node = self.right.prev
        next_node = self.right
        
        prev_node.next = node
        next_node.prev = node
        
        node.prev = prev_node
        node.next = next_node

    def get(self, key: int) -> int:
        if key in self.cache:
            # We touched it! Snip it out and move it to the MRU position
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            
        # Create a new node and add it to our hash map
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        # If we exceeded capacity, evict the LRU!
        if len(self.cache) > self.cap:
            # The LRU is always right next to the Left Dummy
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key] 
            # ^ THIS is why the Node must store the 'key' as well as the 'val'! 
            # Without it, we wouldn't know what to delete from the Hash Map!