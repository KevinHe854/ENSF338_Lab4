import time
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, node):
        node.next = self.head
        self.head = node

    def insert_tail(self, node):
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def get_size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def get_element_at_pos(self, pos):
        current = self.head
        for _ in range(pos):
            if not current:
                return None
            current = current.next
        return current.data if current else None

    def reverse(self):
        newhead = None
        prevNode = None
        for i in range(self.get_size()-1, -1, -1):
            currNode = self.get_element_at_pos(i)
            currNewNode = Node(currNode)
            if newhead is None:
                newhead = currNewNode
            else:
                prevNode.next = currNewNode
            prevNode = currNewNode
        self.head = newhead

    def reverse_optimized(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

def time_reverse_methods(sizes):
    results = {
        'original': [],
        'optimized': []
    }
    
    for size in sizes:
        # Original method timing
        ll_original = LinkedList()
        for i in range(size):
            ll_original.insert_tail(Node(i))
        
        start = time.time()
        for _ in range(100):
            ll_original.reverse()
        results['original'].append((time.time() - start) / 100)
        
        # Optimized method timing
        ll_optimized = LinkedList()
        for i in range(size):
            ll_optimized.insert_tail(Node(i))
        
        start = time.time()
        for _ in range(100):
            ll_optimized.reverse_optimized()
        results['optimized'].append((time.time() - start) / 100)
    
    return results

# Timing and plotting
sizes = [1000, 2000, 3000, 4000]
results = time_reverse_methods(sizes)

plt.figure(figsize=(10, 6))
plt.plot(sizes, results['original'], marker='o', label='Original Method')
plt.plot(sizes, results['optimized'], marker='o', label='Optimized Method')
plt.xlabel('List Size')
plt.ylabel('Average Execution Time (seconds)')
plt.title('Reverse Methods Performance Comparison')
plt.legend()
plt.grid(True)
plt.savefig('reverse_performance.png')
plt.close()

print("Performance results saved to reverse_performance.png")
