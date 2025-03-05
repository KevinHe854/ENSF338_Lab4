# Exercise 7 Answers

## Question 1: Time Complexity of reverse() Implementation

The time complexity of the given `reverse()` implementation is O(n), where n is the number of elements in the list.

Reasoning step-by-step:
1. The function uses a single `for` loop that iterates through all elements of the list exactly once.
2. Each iteration performs constant-time operations:
   - `get_element_at_pos(i)`: O(1)
   - Creating a new node: O(1)
   - Updating head and prev node pointers: O(1)
3. Since the loop runs n times and each iteration is O(1), the total time complexity is O(n).

## Question 2: Optimized Implementation

An optimized implementation could use in-place reversal to reduce space complexity:

```python
def reverse(self):
    prev = None
    current = self.head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    self.head = prev
```

Improvements:
- Reduces space complexity from O(n) to O(1)
- Avoids creating new nodes
- Single pass through the list
- Directly modifies the existing list structure
- Time complexity remains O(n)
