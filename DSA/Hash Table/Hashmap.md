# 🧠 Notes: Understanding Hash Maps (Dictionaries) and Anagram Problem in Python

---

## 🩵 1. What is a Hash (Dictionary)?

A **hash map** or **dictionary** in Python stores data as **key–value pairs**.

Example:

```python
my_dict = {"a": 1, "b": 2}
```

- `"a"` and `"b"` → **keys**
- `1` and `2` → **values**

You can access and update values instantly:

```python
my_dict["a"]  # returns 1
my_dict["b"] += 1  # increases value of 'b' by 1
my_dict["c"] = 5  # adds a new key-value pair
```

Hash maps are **fast** because they don’t search through the list —
they use a **hashing function** that jumps directly to where data is stored in memory.
This makes lookups almost **O(1)** (constant time).

---

## 💡 2. The Anagram Problem

**Question:**
Check if two strings are *anagrams* (same letters, same frequency, different order).

Example:

* `"listen"` and `"silent"` → ✅ Anagrams
* `"rat"` and `"car"` → ❌ Not anagrams

---

## ⚙️ 3. Solution Anagram problem

### ✅ Code:
 - using hash map

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        # Step 1: Count each letter in s
        for char in s:
            count[char] = count.get(char, 0) + 1

        # Step 2: Subtract for each letter in t
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] < 0:
                return False

        # Step 3: All counts must return to zero
        return True
```
- alt solution
 ```py
 class Solution:
     def isAnagram(self, s: str, t: str) -> bool:
         return sorted(s) == sorted(t)
 ```
---

## 🔍 4. How hashmap Works

Instead of sorting, we can count how many times each letter appears in the first string and compare with the second.

### Step 1 — Counting

For `"apple"`:

```
count = {'a': 1, 'p': 2, 'l': 1, 'e': 1}
```

This means:

* 'a' appears once
* 'p' appears twice
* 'l' and 'e' appear once

### Step 2 — Subtracting

For `"papel"`, subtract each letter:

| Letter | Before                    | After                     |
| ------ | ------------------------- | ------------------------- |
| 'p'    | {'a':1,'p':2,'l':1,'e':1} | {'a':1,'p':1,'l':1,'e':1} |
| 'a'    | {'a':1,...}               | {'a':0,...}               |
| 'p'    | {'p':1,...}               | {'p':0,...}               |
| 'e'    | {'e':1,...}               | {'e':0,...}               |
| 'l'    | {'l':1,...}               | {'l':0,...}               |

End result:

```
{'a': 0, 'p': 0, 'l': 0, 'e': 0}
```

✅ All counts are zero → strings are anagrams.

---

## 🧩 5. Understanding `.get(char, 0)`

Line:

```python
count[char] = count.get(char, 0) + 1
```

Means:

* Look for `char` in the dictionary.
* If found, use its value.
* If not found, use `0`.
* Add `1` and store back.

So instead of writing:

```python
if char in count:
    count[char] += 1
else:
    count[char] = 1
```

We can do it in one clean line with `.get()`.

---

## ⚔️ 6. Why Hash Map is Better than Sorting

| Method   | Time Complexity | Space                 | Notes                    |
| -------- | --------------- | --------------------- | ------------------------ |
| Sorting  | O(n log n)      | O(1)                  | Slower for large strings |
| Hash Map | O(n)            | O(1) (fixed alphabet) | Faster and direct        |

---

## 🚫 7. Why Your Code Using `set(sorted(...))` Was Wrong

### Your code:

```python
s1 = set(sorted(s))
t1 = set(sorted(t))
if s1 == t1:
    return True
else:
    return False
```

### Problem:

A **set** removes duplicates.

Example:

```python
set("aabb")  # gives {'a', 'b'}
set("ab")    # also gives {'a', 'b'}
```

Both sets look the same — even though `"aabb"` ≠ `"ab"` in letter count.
So your code checks **if both words have the same letters**, but **ignores how many times each appears**.

Anagrams require both:

1. Same letters ✅
2. Same frequency of each letter ✅

Your code only checks (1).

---

## ✅ Correct Concept Summary

| Concept                   | Meaning                                                     |
| ------------------------- | ----------------------------------------------------------- |
| **Dictionary (hash map)** | Stores key–value pairs                                      |
| **Key**                   | The thing you look up (e.g., a letter)                      |
| **Value**                 | Data attached to that key (e.g., how many times it appears) |
| **`.get(char, 0)`**       | Returns the value for a key, or 0 if key not found          |
| **Why use hash maps**     | Faster counting and comparison                              |
| **Common mistake**        | Using sets removes duplicates, breaking frequency checks    |

---

## 🧾 Final Takeaway

When checking anagrams:

* Always count **frequency** of each character.
* Don’t use `set()` for counting tasks — it loses information.
* Dictionaries (hash maps) let you store and adjust counts quickly.
* The optimized solution runs in **O(n)** time, perfect for large strings.

---

### 🔑 In Short

> A *hash map* (dictionary) lets you track how many times each letter appears, and comparing those counts is the most accurate way to detect anagrams.
