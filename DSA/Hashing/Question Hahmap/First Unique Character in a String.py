class Solution:
    def firstUniqChar(self, s: str) -> int:
        m={}
        for i in s:
            if i in m:
                m[i]=m.get(i,0)+1
            else:
                m[i]=m.get(i,0)+1
        # for i in s:
        for idx,i in enumerate(s):
            if m[i]==1:
                return idx
        else: return -1