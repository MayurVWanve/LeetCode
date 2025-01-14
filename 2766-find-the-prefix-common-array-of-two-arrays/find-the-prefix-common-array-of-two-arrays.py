class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        set_a, set_b, n,m, soln = set(), set(), len(A), len(B), [0] 
        i,j = 0,0

        while i<n and j<m: 
            c = 0
            set_a.add(A[i])
            set_b.add(B[j])

            if A[i] in set_b:
                c+=1
            
            if B[j] in set_a:
                c+=1

            if A[i] == B[j]:
                c-=1
            
            i,j = i+1, j+1

            soln.append(soln[-1] + c)

        while i<n:
            set_a.add(A[i])
            if A[i] in set_b:
                soln.append(soln[-1] + 1)
            else:
                soln.append(soln[-1])

            i+=1

        
        while j<m:
            set_b.add(B[j])
            if B[j] in set_a:
                soln.append(soln[-1] + 1)
            else:
                soln.append(soln[-1])
            
            j+=1

        return soln[1:]

        