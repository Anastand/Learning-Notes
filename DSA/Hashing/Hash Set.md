# some basic information
  
  - no duplicates
  - fast existence check
  - in python = set

___
## hashset 
  - it is a collection of unique items
  
    ### common operataions
      - Add: myset.add(x) — Add value x to the set

      - Remove: myset.remove(x) — Remove x from the set (error if x not present)

      - Discard: myset.discard(x) — Remove x if present, otherwise do nothing (no error!)

      - Check existence: x in myset — Return True if x is present

      - Length: len(myset) — Number of elements in the set

      - Iterate: for x in myset: — Go through each element

  - Union, Intersection, Difference:

    - A | B — union (all elements from both sets)

    - A & B — intersection (only elements present in both sets)

    - A - B — difference (elements in A but not in B)

    - Clear: myset.clear() — Remove all elements
### Q solved knowledge

#### Intersection of Two Arrays (LeetCode):
  - Sets are ideal for removing duplicates and fast membership checking.

  - Converting lists to sets lets you discover unique elements shared between lists (intersection).

  - Standard set operations like membership if i in s2: or set1 & set2 are much faster than nested loops.

  - Hashmap/set-based approaches turn otherwise O(n*m) solutions into O(n+m).

  - When solving intersection, think in terms of unique elements, not positions or frequencies.

  - Writing logic using set conversion and then checking intersection is highly efficient in Python.
