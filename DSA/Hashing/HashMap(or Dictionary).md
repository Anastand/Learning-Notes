## **Hashmaps (Dictionaries) in Python: Full Guide**

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

## **Advantages of Hashmaps**
- **O(1) time** for insert, update, and retrieve.
- Powerful for problems needing fast checks, counting, uniqueness, grouping, mapping, and more.
