# Exercise 4.1 - Complexity Analysis

# Question 1: Time Complexity Analysis
"""
Best Case Complexity: O(n)
- Occurs when no element in the list is > 5
- Only the outer loop runs

Worst Case Complexity: O(n^2)
- Occurs when most/all elements are > 5
- Outer loop runs n times
- Inner loop also runs n times for each iteration
- Total operations: n * n = n^2

Average Case Complexity: O(n^2)
- Similar to worst case, as inner loop runs frequently
"""

def processdata(li):
    for i in range(len(li)):
        if li[i] > 5:
            for j in range(len(li)):
                li[i] *= 2

# Question 2: Modifying Code for Equivalent Complexity
def processdata_optimized(li):
    for i in range(len(li)):
        if li[i] > 5:
            li[i] *= 2**len(li)

# Explanation for Question 2:
"""
This version ensures that:
- Minimum complexity is O(n)
- Best, worst, and average case complexities are equivalent
- Multiplies the element by 2^n instead of nested loop
- Maintains the spirit of scaling based on list size
"""
