class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h1, h2, n1, n2, l = defaultdict(int), defaultdict(int), len(s1), len(s2), 0

        if n1 >  n2:
            return False 
            
        for ele in s1:
            h1[ele] = h1.get(ele,0) + 1

        for i in range(n1):
            h2[s2[i]] = h2.get(s2[i],0) + 1
        
        for i in range(n1, n2):
            # print(h1, h2)
            if h1 == h2:
                return True
            
            h2[s2[l]]-=1
            if h2[s2[l]] == 0:
                del(h2[s2[l]])
            l+=1
            h2[s2[i]] = h2.get(s2[i],0) + 1
        
        
        return True if h1==h2 else False


        


        