class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity):

        self.capacity = capacity
        self.curr_capacity = 0
        self.map = {}  # key -> node

        # dummy sentinel nodes
        self.head = Node(0, 0)  # least recent side
        self.tail = Node(0, 0)  # most recent side
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        # TODO: remove a node from the linked list

        temp = node

        if node.prev:
            node.prev.next = temp.next
        
        if node.next:
            node.next.prev = temp.prev
        

    def _insert_right(self, node: Node) -> None:
        # TODO: insert a node just before tail (most recent position)
        prev_node = self.tail.prev

        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:

        if key not in self.map:
            return -1
        
        node = self.map[key]

        self._remove(node)
        self._insert_right(node)

        return node.val

    def put(self, key: int, value: int) -> None:

        if key in self.map:
            curr_node = self.map[key]
            curr_node.val = value
            self._remove(curr_node)
            self._insert_right(curr_node)
        else:

            if self.curr_capacity >= self.capacity:
                target = self.head.next
                self._remove(target)
                del self.map[target.key]

            curr_node = Node(key, value)
            self._insert_right(curr_node)
            self.map[key] = curr_node
            self.curr_capacity += 1


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)