class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        i,ans,n, set1, set2, comp = 0,0,len(s1), set(), set(),0


        for i in range(n):
            if s1[i] != s2[i]:
                comp+=1
                set1.add(s1[i])
                set2.add(s2[i])
            
        
        return True if (comp == 0 or (comp == 2 and (set1 == set2))) else False
        