# Exercise 6

In the lecture recordings, we discussed some of the main differences between arrays (or lists in python) and Linked Lists.

1. Compare advantages and disadvantages of arrays vs linked list (complexity of task completion).

> Operations at the head of a linked list has complexity $O(1)$ since you do not need to traverse through the entire list to perform inserting or deleting. On the other hand, operations at the front of an array has complexity of $O(n)$ because the positions of the other array elements need to be shifted to account for the operation. For example, head insertion requires the elements to shift to the right before the new element can be added, and may even need to move somewhere else in memory if there isn't enough space to increase capacity.
>
>Operations at the end of an array has complexity $O(1)$ since we can just go to the end of the array directly and perform inserting or deleting. If a linked list doesn't have a tail pointer, then operations at the tail of a linked list has complexity $O(n)$ because we have to traverse to the end of the list to do the operation.

2. For arrays, we are interested in implementing a replace function that acts as a deletion followed by insertion. How can this function be implemented to minimize the impact of each of the standalone tasks?

> We can delete the element in the position it's in but don't shift the elements on the right of it. Then we insert the new element in the same position as the deleted element.

3. Assuming you are tasked to implement a doubly linked list with a sort function, given the list of sort functions below, state the feasibility of using each one of them and elaborate why is it possible or not to use them.

- Insertion sort

> Insertion sort is possible on a doubly linked list. On each iteration, we compare the current node to the node before it, and if current is less than the previous, we can traverse backwards until we find the position where current should be.

- Merge sort

> Merge sort is better than insertion sort on a linked list. We can initilize two pointers and traverse through the list with one pointer moving twice as fast as the other. This way, when the faster pointer reaches the end, the slower one is pointing at the midpoint. We then split the list in half using the slower pointer and apply this recursively until we get sublists with one node. We can then merge these sublists by changing each of the node's pointers to where they have to point to and finally set the head pointer to the head of the newly sorted list.

4. Also show the expected complexity for each and how it differs from applying it to a regular array.

- Insertion sort

> In the worst case scenario complexity is $O(n^2)$. This is similar to insertion sort which also has a worst-case complexity of $O(n^2)$.

- Merge Sort

> The complexity of merge sort on a linked list is $O(n log n)$, which is the same is the complexity on an array and for similar reasons: there are $log_2 n$ steps to divide $n$ elements into halves.