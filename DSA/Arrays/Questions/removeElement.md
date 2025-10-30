# Remove Element - LeetCode

**Prompt Summary:**
  - Given an integer array `nums` and a value `val`, remove all instances of `val` “in-place” so that the remaining elements are all not equal to `val`.
  - Return the new length `k`.
  - The first `k` elements of `nums` should contain the elements you kept; the rest can be ignored.

---

## **Key Concepts & Patterns**

- **In-place:**  
  Overwrite values in the original array `nums`; do not create extra arrays.

- **Two Pointer Pattern:**  
  - `write` pointer starts at 0 and marks the position to fill with a value to keep.
  - `i` pointer goes through every position in `nums`.

- **Overwrite (Not Remove):**  
  For every value not equal to `val`, write it to `nums[write]` and increment `write`.

- **Return Count, Not Array:**  
  The solution returns how many elements were kept (`k`), not the modified list.
  - Only `nums[0:k]` are valid.

---

## **Step-by-Step Explanation**

1. **Initialize `write = 0`**
   - This pointer marks the next available slot for a value you want to keep.

2. **Loop over `nums` with index `i`**
   - For each `nums[i]`:
     - If it's not equal to `val`:
       - Set `nums[write] = nums[i]`
       - Move `write` forward (`write += 1`)

3. **After loop:**
   - The first `write` elements of `nums` are the ones you kept (the answer).
   - The rest can be ignored.

4. **Return `write` as the new length.**

---

## **Example Walk-through**

Input:  
`nums = [3, 2, 2, 3]`, `val = 3`

Process:
- `write = 0`
- Loop:
  - `i=0`: `nums[0]=3` (equals `val`) → skip
  - `i=1`: `nums[1]=2` (not `val`) → `nums[write]=2`, `write=1`
  - `i=2`: `nums[2]=2` (not `val`) → `nums[write]=2`, `write=2`
  - `i=3`: `nums[3]=3` (equals `val`) → skip
- Result:  
  - Array: `[2, 2, 2, 3]`
  - Return: `write = 2`  
  - Kept elements: `[2, 2]` (`nums[0:write]`)

---

## **Python Snippet**
```py
write = 0
for i in range(len(nums)):
    if nums[i] != val:
        nums[write] = nums[i]
        write += 1
return write
```

---

## **Common Pitfalls**
- Returning the array instead of the count.
- Creating a new list (not allowed).
- Confusing “for i in nums” (gets values, not indexes) vs “for i in range(len(nums))” (lets you overwrite).

---

## **How to Build Intuition**

- Practice tracing with actual data.
- Recognize “in-place” triggers: Overwrite, not create new.
- Internalize the two pointer “read/write” trick for removing or keeping elements in arrays.
- Focus on what part of the array contains the answer (usually first k elements).
