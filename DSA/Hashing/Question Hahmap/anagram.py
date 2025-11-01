class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1={}
        d2={}
        for i in s:
            if i in d1:
                d1[i]=d1.get(i,0)+1
            else:
                d1[i]=d1.get(i,0)+1
        for i in t:
            if i in d1:
                d2[i]=d2.get(i,0)+1
            else:
                d2[i]=d2.get(i,0)+1
        if d1==d2:
            return True
        return False