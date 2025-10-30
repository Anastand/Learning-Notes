# Move Zeroes 

## **Logic Recap**
- Use **two pointers**:
    - `i`: tracks the next position to place a non-zero
    - `j`: scans all elements
- For each `j`, if `nums[j]` is not zero, put its value at `nums[i]`, then increment `i`.
- Once all non-zeros have moved to the front, fill the rest of the array with zeros.

---

## **Code Pattern With Comments**

```py
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0  # Points to where the next non-zero should go

        # Move all non-zero numbers to the front
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1

        # Fill the remaining slots with zeros
        for k in range(i, len(nums)):
            nums[k] = 0
```

- **First loop preserves order**: Non-zero elements keep their relative position.
- **Second loop ensures all zeros are at the end.**

---

## **Key Edge Cases & Tips**
- All zeros: The entire array becomes zeros, as expected.
- All non-zeros: No zeros to move; the order is unchanged.
- Zeros at the end: Second loop redundantly overwrites zeros, which is fine.

**Now you’re ready to tackle similar in-place “shifting” or “partitioning” array problems!**
