import time
import random
import matplotlib.pyplot as plt

# Inefficient Search (Linear Search)
def inefficient_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Efficient Search (Binary Search)
def efficient_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Performance Experiment
def performance_experiment(sizes=[1000, 2000, 3000, 4000, 5000]):
    results = {
        'inefficient': [],
        'efficient': []
    }
    
    for size in sizes:
        # Generate sorted array for binary search
        arr = sorted(random.sample(range(size*10), size))
        target = arr[random.randint(0, size-1)]
        
        # Timing inefficient search
        inefficient_times = []
        for _ in range(100):
            start = time.time()
            inefficient_search(arr, target)
            inefficient_times.append(time.time() - start)
        
        # Timing efficient search
        efficient_times = []
        for _ in range(100):
            start = time.time()
            efficient_search(arr, target)
            efficient_times.append(time.time() - start)
        
        results['inefficient'].append(sum(inefficient_times) / 100)
        results['efficient'].append(sum(efficient_times) / 100)
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.boxplot([results['inefficient'], results['efficient']], 
                labels=['Inefficient Search', 'Efficient Search'])
    plt.title('Search Algorithm Performance Comparison')
    plt.ylabel('Average Execution Time (seconds)')
    plt.savefig('search_performance.png')
    plt.close()
    
    return results

# Run the experiment
performance_experiment()

# Complexity Analysis
"""
Inefficient Search (Linear Search):
- Worst-case complexity: O(n)
- Searches by checking each element sequentially

Efficient Search (Binary Search):
- Worst-case complexity: O(log n)
- Works only on sorted arrays
- Repeatedly divides search interval in half
"""
