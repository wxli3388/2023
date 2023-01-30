class Node
    def __init__(self, val):
        self.val = val
        self.fre = 0
        self.next = null
        self.pre = null
    
class LFUCache:

    def __init__(self, capacity: int):
        self.freqH = defaultdict(Node)
        self.h = defaultdict(Node)
        self.capacity = capacity
        self.minFreq = math.max
    def get(self, key: int) -> int:

    def put(self, key: int, value: int) -> None:
        
        if key in h:
            node = self.h[key]
            node.pre.next = null
            node.next = null
            node.pre+=1
            if node.pre in self.freqH:
                self.freqH
        node = Node(value)
        self.h[key] = node
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)