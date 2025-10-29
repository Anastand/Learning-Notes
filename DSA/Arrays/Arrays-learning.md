- started - 26 Oct 25
- done with learingig arrays - 26 Oct 25
- End -
---
## Arrays
### Time Complexity
- **Access** → `O(1)`: You can directly access any element using its index in constant time.
- **Insert** → `O(n)` or `O(1)`: Inserting at the end of an array is `O(1)` (fast), but inserting elsewhere requires shifting elements, which takes `O(n)` time.
- **Delete** → `O(n)`: Removing an element may require shifting other elements or traversing the array, which takes linear time.
- **Traversal** → `O(n)`: Visiting each element one by one takes time proportional to the number of elements.
- **Search**:
		- **Linear Search** → `O(n)`: Check each element sequentially until a match is found.
		- **Binary Search** → `O(log n)`: Efficiently narrow down the search space by half each step (requires the array to be sorted).
- **Update** → `O(1)`: Modify an element at a known index directly in constant time.

### Benefits
- **Random Access**: Retrieve any element instantly using its index.
- **Cache Friendly**: Elements are stored contiguously in memory, improving performance.
- **Ease of Sorting**: Efficient sorting algorithms like binary search work well with arrays.
- **Implementation Friendly**: Arrays are foundational for building other data structures (e.g., stacks, queues).

### Limitations
- **Fixed Size**: Traditional arrays have a fixed size, though Python lists are dynamic.
- **O(n) Time Complexity**: Insertions/deletions in the middle can be slow due to shifting.

#### When to Use Arrays
1. **Implementation of Other Data Structures**: Arrays are used to build stacks, queues, heaps, etc.
2. **Caching**: Arrays are efficient for storing and accessing data in cache-friendly ways.
3. **Tree Structures**: Arrays can represent trees (e.g., heap) using index-based parent-child relationships.
4. **Mathematical Computations**: Ideal for matrices, grids, or tensors in linear algebra.
5. **Coding Patterns**:
			- **Two Pointer**: Useful for problems like finding pairs or subarrays.
			- **Sliding Window**: Efficient for subarray or substring problems with fixed window sizes.

___

### Multi-Dimensional Arrays
A multi-dimensional array is a collection of arrays, often visualized as rows and columns (e.g., 2D arrays) or higher dimensions. It’s great for structured data like matrices, grids, or tensors.

**Example:**
```python
# 2D array (matrix)
matrix = [
				[1, 2, 3],
				[4, 5, 6],
				[7, 8, 9]
]
print(matrix[1][2])  # Output: 6
```
- Accessing elements requires specifying multiple indices (e.g., `matrix[row][column]`).
- Inserting or deleting elements in a 2D array also involves shifting, but the complexity depends on the number of dimensions.

## Using Arrays in Python
> Video reference: [neetcode.io](https://youtu.be/0K_eZGS5NsU?t=520)

In Python, arrays are implemented using **lists**, which are dynamic (can grow or shrink). Here’s how they work:

### Key Features of Python Lists
- **Dynamic Size**: Unlike fixed-size arrays, you can add/remove elements anytime.
	```python
		arr = [1, 2, 3]
		arr.append(4)        # Add to end (O(1))
		arr.insert(1, 1.5)   # Insert in middle (O(n))
		arr.pop(2)           # Remove element (O(n))
		arr[0] = 100         # Update value (O(1))
		matrix = [[1, 2], [3, 4]]
		print(matrix[0][1])  # Output: 2
	```
- **Negative Indexing**: Use `-1` to access the last element.
	```python
		arr = [10, 20, 30]
		print(arr[-1])  # Output: 30
	```
- **Slicing**: Extract subarrays using `array[start:end:step]`
	```python
		arr = [1, 2, 3, 4, 5]
		print(arr[1:4])        # Output: [2, 3, 4]
		print(arr[::2])        # Output: [1, 3, 5] (every other element)
	```

### Useful Techniques
- **Unpacking**: Assign list elements to variables directly.
	```python
		a, b = [1, 2]
		print(a, b)  # Output: 1 2
	```

- **Enumerate**: Get both index and value during iteration.
	```python
		arr = ["apple", "banana", "cherry"]
		for index, fruit in enumerate(arr):
						print(f"Index {index}: {fruit}")
	```

- **Zip Function**: Pair elements from two or more lists.
	```python
		list1 = [1, 2, 3]
		list2 = ["a", "b", "c"]
		for num, letter in zip(list1, list2):
						print(num, letter)  # Output: 1 a, 2 b, 3 c
	```

- **Sorting with Lambda**: Use lambda functions for custom sorting.
	```python
		arr = ["banana", "apple", "cherry"]
		arr.sort(key=lambda x: len(x))  # Sort by string length
		print(arr)  # Output: ['apple', 'banana', 'cherry']
	```

- **List Comprehensions**: Create lists concisely.
	```python
		# Simple list comprehension
		arr = [i * 2 for i in range(5)]  # [0, 2, 4, 6, 8]

		# 2D array using list comprehension
		matrix = [[0] * 4 for i in range(4)]  # 4x4 grid of zeros
		print(matrix)
		# Output:
		# [
		#   [0, 0, 0, 0],
		#   [0, 0, 0, 0],
		#   [0, 0, 0, 0],
		#   [0, 0, 0, 0]
		# ]

		# Alternative method using nested list comprehension
		matrix = [[0 for _ in range(4)] for _ in range(4)]
		print(matrix)
		# Output:
		# [
		#   [0, 0, 0, 0],
		#   [0, 0, 0, 0],
		#   [0, 0, 0, 0],
		#   [0, 0, 0, 0]
		# ]
	```

### Notes
- Python lists are **flexible** but have **trade-offs**: inserting/deleting in the middle is slower (`O(n)`).
- Avoid using `[0] * 4` for mutable objects (e.g., lists) in comprehensions, as it creates references to the same object. Use it safely for immutable types like integers.
