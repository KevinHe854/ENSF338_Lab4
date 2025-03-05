# Question 4
# The complexity of binary search for linked lists is O(n)
# This may be because we have to iterate through the entire linked list
# to find the middle element since we don't have indices like arrays do.

import timeit
from random import randint
from matplotlib import pyplot as plt

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
        
class LinkedList:
    def __init__(self, num):
        self._head = Node(randint(1, 3))
        self._tail = self._head
        
        for i in range (2, num + 1):
            current = self._tail
            self._tail = Node(current.data + randint(1, 3))
            current.next = self._tail
            
    def binary_search(self, num):
        start = self._head
        end = None
        
        while True:
            mid = self.find_middle(start, end)
            
            if mid is None:
                return False
            
            if mid.data == num:
                return True
            
            elif start == end:
                break
            
            elif mid.data < num:
                start = mid.next
            
            elif mid.data > num:
                end = mid
                
        return False
    
    def find_middle(self, start, end):
        if start is None:
            return None
        
        if start == end:
            return start
        
        slow = start
        fast = start.next
        
        while fast != end:
            fast = fast.next
            slow = slow.next
            if fast != end:
                fast = fast.next
        
        return slow
    
class Array:
    def __init__(self, num):
        self._arr = [randint(1, 3)]
        for i in range(1, num + 1):
            self._arr.append(self._arr[-1] + randint(1, 3))
    
    def binary_search(self, num):
        start = 0
        end = len(self._arr) - 1
        
        while start < end:
            mid = (start + end) // 2
            
            if self._arr[mid] < num:
                start = mid + 1
                
            elif self._arr[mid] > num:
                end = mid - 1
                
            else:
                return True
            
        return False


length = [1000, 2000, 4000, 8000]
ll_times = []
a_times = []

setup_ll_1k = '''
from random import randint
from __main__ import LinkedList
ll_1k = LinkedList(1000)
'''
setup_ll_2k = '''
from random import randint
from __main__ import LinkedList
ll_2k = LinkedList(2000)
'''
setup_ll_4k = '''
from random import randint
from __main__ import LinkedList
ll_4k = LinkedList(4000)
'''
setup_ll_8k = '''
from random import randint
from __main__ import LinkedList
ll_8k = LinkedList(8000)
'''

setup_a_1k = '''
from random import randint
from __main__ import Array
a_1k = Array(1000)
'''
setup_a_2k = '''
from random import randint
from __main__ import Array
a_2k = Array(2000)
'''
setup_a_4k = '''
from random import randint
from __main__ import Array
a_4k = Array(4000)
'''
setup_a_8k = '''
from random import randint
from __main__ import Array
a_8k = Array(8000)
'''

search_ll_1k = 'll_1k.binary_search(randint(1, 3000))'
search_ll_2k = 'll_2k.binary_search(randint(1, 6000))'
search_ll_4k = 'll_4k.binary_search(randint(1, 12000))'
search_ll_8k = 'll_8k.binary_search(randint(1, 24000))'

search_a_1k = 'a_1k.binary_search(randint(1, 3000))'
search_a_2k = 'a_2k.binary_search(randint(1, 6000))'
search_a_4k = 'a_4k.binary_search(randint(1, 12000))'
search_a_8k = 'a_8k.binary_search(randint(1, 24000))'

ll_times.append((timeit.timeit(setup=setup_ll_1k, stmt=search_ll_1k, number=1000)) / 1000)
ll_times.append((timeit.timeit(setup=setup_ll_2k, stmt=search_ll_2k, number=1000)) / 1000)
ll_times.append((timeit.timeit(setup=setup_ll_4k, stmt=search_ll_4k, number=1000)) / 1000)
ll_times.append((timeit.timeit(setup=setup_ll_8k, stmt=search_ll_8k, number=1000)) / 1000)

a_times.append((timeit.timeit(setup=setup_a_1k, stmt=search_a_1k, number=1000)) / 1000)
a_times.append((timeit.timeit(setup=setup_a_2k, stmt=search_a_2k, number=1000)) / 1000)
a_times.append((timeit.timeit(setup=setup_a_4k, stmt=search_a_4k, number=1000)) / 1000)
a_times.append((timeit.timeit(setup=setup_a_8k, stmt=search_a_8k, number=1000)) / 1000)

for i in range(len(ll_times)):
    ll_times[i] *= 1000
    
for i in range(len(a_times)):
    a_times[i] *= 1000

plt.plot(length, ll_times)
plt.title('Linked List Binary Search Times')
plt.xlabel('Length of List')
plt.ylabel("Time (milliseconds)")
plt.show()

plt.plot(length, a_times)
plt.title('Array Binary Search Times')
plt.xlabel('Length of Array')
plt.ylabel("Time (milliseconds)")
plt.show()