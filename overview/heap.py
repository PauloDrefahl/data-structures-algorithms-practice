"""
class MaxHeap:
    def __init__(self):
        # Initialize an empty list to store the heap elements
        self.heap = []

    def insert(self, value):
        self.heap.append(value)  # Add the new value to the end
        self._bubble_up(len(self.heap) - 1)  # Restore the heap property

    def extract_max(self):
        if len(self.heap) == 0:
            return None  # If the heap is empty, return None

        if len(self.heap) == 1:
            return self.heap.pop()  # If there's only one element, remove and return it

        max_value = self.heap[0]  # The root contains the maximum value
        self.heap[0] = self.heap.pop()  # Replace the root with the last element
        self._bubble_down(0)  # Restore the heap property
        return max_value

    def peek(self):
        return self.heap[0] if self.heap else None

    def _bubble_up(self, index):
        parent = (index - 1) // 2  # Calculate the parent's index

        while index > 0 and self.heap[index] > self.heap[parent]:
            # Swap the current node with its parent
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            # Update the index to the parent's position
            index = parent
            # Recalculate the parent's index
            parent = (index - 1) // 2

    def _bubble_down(self, index):
        largest = index  # Assume the current node is the largest
        left = 2 * index + 1  # Calculate the left child's index
        right = 2 * index + 2  # Calculate the right child's index

        # Check if the left child exists and is greater than the current node
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        # Check if the right child exists and is greater than the current largest
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        # If the largest is not the current node, swap and continue bubbling down
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._bubble_down(largest)

    def display(self):
        print("Heap:", self.heap)


# Create a max-heap
heap = MaxHeap()

# Insert elements
heap.insert(10)
heap.insert(20)
heap.insert(5)
heap.insert(30)
heap.insert(15)

# Display the heap
heap.display()  # Output: Heap: [30, 20, 5, 10, 15]

# Get the maximum value
print("Max value:", heap.peek())  # Output: 30

# Extract the maximum value
print("Extracted max:", heap.extract_max())  # Output: 30

# Display the heap after extraction
heap.display()  # Output: Heap: [20, 15, 5, 10]

# Extract more elements
print("Extracted max:", heap.extract_max())  # Output: 20
heap.display()  # Output: Heap: [15, 10, 5]

"""

import heapq

# Create an empty min-heap
heap = []

# Insert elements into the heap
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)
heapq.heappush(heap, 1)

# Display the heap
print("Heap after insertions:", heap)  # Output: [1, 5, 20, 10]

# Peek at the smallest element
print("Smallest element:", heap[0])  # Output: 1

# Extract the smallest element
print("Extracted smallest:", heapq.heappop(heap))  # Output: 1
print("Heap after extraction:", heap)  # Output: [5, 10, 20]

# Add a new element and extract the smallest in one step
print("Pushed 2, and extracted smallest:", heapq.heappushpop(heap, 2))  # Output: 2
print("Heap after pushpop:", heap)  # Output: [5, 10, 20]

# Replace the smallest element with a new value
print("Replaced smallest with 15:", heapq.heapreplace(heap, 15))  # Output: 5
print("Heap after replacement:", heap)  # Output: [10, 15, 20]

# Convert an unordered list into a heap
unordered = [40, 10, 30, 20, 50]
heapq.heapify(unordered)
print("Heapified list:", unordered)  # Output: [10, 20, 30, 40, 50]

# Find the three smallest elements
print("Three smallest elements:", heapq.nsmallest(3, unordered))  # Output: [10, 20, 30]

# Find the two largest elements
print("Two largest elements:", heapq.nlargest(2, unordered))  # Output: [50, 40]
