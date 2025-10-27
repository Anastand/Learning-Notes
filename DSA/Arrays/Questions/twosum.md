## [question link](https://neetcode.io/problems/two-integer-sum?list=neetcode150)
___
## learning
 - **Algorithm approach**: Used nested loops to check all possible pairs of indices - outer loop for first number, inner loop for second number
  - **Index manipulation**: Utilized `enumerate()` to understand the relationship between indices and values in the array
  - **Avoiding duplicates**: Started inner loop from `i + 1` to prevent checking the same pair in reverse order and ensure each pair is only checked once
  - **Brute force method**: This is a brute force approach with O(n²) time complexity - checks every possible combination
  - **Debugging strategy**: Printed detailed debugging information (`index i -> val i`) to understand how the nested loops work and verify the algorithm logic
  - **Target comparison**: Simple equality check `nums[i] + nums[j] == target` to find the matching pair
  - **Early termination potential**: Current implementation continues checking after finding a match - could be optimized to break early
  - **Array traversal**: Used both `enumerate()` for inspection and `range(len())` for systematic index-based iteration
  - **Pair identification**: Successfully identified and printed the solution `[0, 1]` when `nums[0] + nums[1] = 3 + 4 = 7`

___
## CODE
```py
  # Input:
target = 7
# Output: [0,1]


nums = [3, 4, 5, 6]

for idx, val in enumerate(nums):
    print(f"id:{idx} val:{val} ")

print("\n")
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            # print(f"sum:{nums[i] + nums[j]}\nwe have the index -> i:{i} ,j:{j}") for debugging
            return[i,j]

"""
old logic to figure out how to do what
for idx, val in enumerate(nums):
    print(f"id:{idx} val:{val} ")

print("\n")
for i in range(len(nums)):
    print(f"index i ->{i} val i-> {nums[i]} \n")
    for j in range(i + 1, len(nums)):
        print(f"index j ->{j} val j-> {nums[j]} ")
        print(f" {nums[i]+nums[j]} idx:i{i},j{j}")
"""

```
