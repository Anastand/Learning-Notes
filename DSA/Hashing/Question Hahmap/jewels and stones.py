class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c=0
        m={}
        for i in stones:
            if i in m:
                m[i]=m.get(i,0)+1
            else:
                m[i]=m.get(i,0)+1
        print(m)
        for i in jewels:
            if i in m:
                c +=m.get(i)
                print(i)
        return c