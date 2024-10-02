class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n,lookup,rank = len(arr), defaultdict(list), 1
        soln = [0] * len(arr)

        for i in range(n):
            lookup[arr[i]].append(i)


        arr.sort()
        for ele in arr:
            if ele not in lookup:
                continue

            for pos in lookup[ele]:
                soln[pos] = rank
            del(lookup[ele])
            
            rank+=1
        

        return soln
            
        
