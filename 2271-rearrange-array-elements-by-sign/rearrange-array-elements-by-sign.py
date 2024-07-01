class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg, soln,i,j = [], [], [], 0, 0

        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)

        while i<len(pos):
            soln.append(pos[i])
            soln.append(neg[i])
            i+=1


        return soln
        
        
        

