# Merge Sorted Array - Revision Note

## **Logic Recap:**
- You have two sorted arrays, `nums1` and `nums2`. `nums1` has extra space at the end to fit all elements.
- You need to merge all elements of `nums2` into `nums1`, keeping everything sorted and doing it IN-PLACE (no extra array allowed).
- To avoid overwriting, work backwards from the end, filling from the last slot.
- Always put the biggest value available (from `nums1` or `nums2`) into the next unused slot at the end of `nums1`.
- If you run out of `nums1` elements first, just copy leftover `nums2` elements to the front of `nums1`.

---

## **Code Explained with Comments**

```py
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        f = m - 1      # Pointer: last real element in nums1
        s = n - 1      # Pointer: last element of nums2
        k = m + n - 1  # Pointer: last slot of nums1 buffer

        # Merge by comparing from the end
        while s >= 0 and f >= 0:
            # If nums1 value is less, take nums2 value
            if nums1[f] < nums2[s]:
                nums1[k] = nums2[s]
                s -= 1
            else:
                nums1[k] = nums1[f]
                f -= 1
            k -= 1

        # If nums2 has leftovers, copy them over
        while s >= 0:
            nums1[k] = nums2[s]
            s -= 1
            k -= 1
```

**Key points in comments:**
- Start pointers at the end to avoid overwriting.
- Use three pointers for current positions in each array and the merge slot.
- Only decrement the pointer of the value you just used.
- Any leftover nums2 elements can be copied straight in.

---