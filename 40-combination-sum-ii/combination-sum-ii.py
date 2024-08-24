class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # l, soln = [], []
        # candidates = sorted(candidates)
        # def helper(l, pos, t):
        #     if t == 0:
        #         # l = sorted(l)
        #         if l not in soln:
        #             soln.append(l.copy())
        #         return 
            
        #     if t < 0 or pos>= len(candidates):
        #         return 
            
            
        #     l.append(candidates[pos])
        #     # print(l, pos + 1, t - candidates[pos])
        #     helper(l, pos+1, t - candidates[pos])
        #     l.pop()
        #     # print(l, pos + 1, t)
        #     helper(l, pos + 1, t)
            

        # helper([], 0, target)
        # return soln
        
        l, soln = [], []
        candidates = sorted(candidates)

        def helper(l,pos,target):
            if target == 0:
                soln.append(l.copy())
                return 
            
            if target < 0 or pos >= len(candidates):
                return 

            
            # include the ele and continue even if we get same element next
            l.append(candidates[pos])
            helper(l, pos + 1, target - candidates[pos])
            l.pop()

            # Disclude the repeated element completely and continue
            while pos+1 != len(candidates) and candidates[pos] == candidates[pos + 1]:
                pos +=1
            helper(l, pos + 1, target)

        helper([], 0, target)
        return soln