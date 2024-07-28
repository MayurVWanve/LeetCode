class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lookup, n, i, soln, end, count = {}, len(s), 0, [], 0, 0
        for pos, ele in enumerate(s):
            lookup[ele] = pos
        
        while i < n:
            end = max(end, lookup[s[i]])
            count+=1
            if end == i:
                soln.append(count)
                count = 0
            i+=1    
            

        return soln
            
        