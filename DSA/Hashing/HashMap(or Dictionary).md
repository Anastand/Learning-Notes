## **Hashmaps (Dictionaries): Full Guide**

- key value pair

### **1. Creation**
```python
d = {}              # empty dict
d = {'a': 1, 'b': 2}  # with initial keys/values
```

### **2. Insertion & Update**
```python
d['c'] = 10         # Insert new key 'c' with value 10
d['a'] = 42         # Update existing key 'a' to value 42
```

### **3. Access Value**
```python
x = d['a']          # Direct access (KeyError if missing)
x = d.get('a')      # Safe access (None if missing)
x = d.get('z', 0)   # Default value (0) if not found
```

### **4. Deletion**
```python
del d['a']          # Remove key 'a' (KeyError if not found)
d.pop('b')          # Remove key 'b' and return its value
d.pop('z', None)    # Remove 'z' if found; else return None
```

### **5. Check Existence**
```python
if 'a' in d:
    print('Exists')
if 'z' not in d:
    print('Not there')
```

### **6. Iteration**
```python
for key in d:        # keys only
    print(key)

for value in d.values():  # values only
    print(value)

for key, value in d.items():  # key-value pairs
    print(key, value)
```

### **7. Length, Keys, Values**
```python
length = len(d)           # Number of key-value pairs
keys = list(d.keys())     # List of keys
values = list(d.values()) # List of values
```

### **8. Clearing/Copying**
```python
d.clear()                 # Remove all items
d2 = d.copy()             # Shallow copy
```

### **9. Batch Update**
```python
d.update({'d': 55, 'e': 77})   # Add/update multiple keys in one go
```

***

## **Common Hashmap Patterns in Coding**

#### **A. Frequency Counting**
```python
freq = {}
for val in arr:
    freq[val] = freq.get(val, 0) + 1
```

#### **B. Fast Lookup (e.g. Two Sum)**
```python
lookup = {}
for i, val in enumerate(arr):
    if target - val in lookup:
        # Found a pair!
    lookup[val] = i
```

#### **C. Tracking Duplicates**
```python
seen = set()
for val in arr:
    if val in seen:
        print('Duplicate found')
    seen.add(val)
```

#### **D. Grouping by Key (e.g. Anagrams)**
```python
groups = {}
for word in words:
    key = "".join(sorted(word))
    groups.setdefault(key, []).append(word)
```

#### **E. Storing Complex Data**
```python
d = {'x': [1,2,3], 'y': {'inner': 99}}
```

***
### Q solved knowledge
  - A hashmap (dict) is a mapping from keys to values with fast O(1) access time.
  - Main operations:
      - Create: d = {}
      - Insert/Update: d[key] = value
      - Access: d[key] (KeyError if not found), d.get(key, default) (safe)
      - Check existence: if key in d:
      - Delete: del d[key] or d.pop(key)
      - Iterate: for k,v in d.items()
  - Use dictionaries to:
      - Count frequencies fast (frequency map)
      - Track duplicates or presence (use set or dict)
      - Group by category (e.g., anagrams)
      - Map elements to indices (Two Sum)
  - Interview patterns:
      - Frequency counting: 
          freq[c] = freq.get(c, 0) + 1
      - Fast lookup: 
          if target - n in d:
              # do something
      - Grouping:
          group.setdefault(key, []).append(value)
  - Hashmap-based problem examples:
      1. Two Sum: Use dict for complement lookup
      2. Contains Duplicate: Use set/dict for seen values
      3. Valid Anagram: Create letter-frequency dicts for both strings and compare
      4. Intersection: Use set/dict to find overlaps quickly
  - Keys for correct usage:
      - Always check membership before access (if k in d:)
      - To increment, always use get: d[k] = d.get(k, 0) + 1
      - For comparing content (anagrams): build frequency maps for each sequence

  Always think: Am I mapping, counting, grouping, or doing fast lookup? 
  Dictionaries and sets are your go-to tools for those tasks!

## **Advantages of Hashmaps**
- **O(1) time** for insert, update, and retrieve.
- Powerful for problems needing fast checks, counting, uniqueness, grouping, mapping, and more.
