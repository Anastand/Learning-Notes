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
