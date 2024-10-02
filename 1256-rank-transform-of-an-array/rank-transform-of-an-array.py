class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n,lookup,rank = len(arr), defaultdict(list), 1
        soln = [0] * len(arr)

        for i in range(n):
            lookup[arr[i]].append(i)

        temp = sorted(list(set(arr)))
        for ele in temp:

            for pos in lookup[ele]:
                soln[pos] = rank
            
            rank+=1
        

        return soln
            
        
