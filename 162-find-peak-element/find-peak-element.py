class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # I think divide and conquer approach should work.
        n, soln = len(nums), 0

        def findPeak(i,j):
            nonlocal soln
            
            if j > n-1 or i<0 or i>j:
                return 

            m = (i+j)//2
            left  = nums[m-1] if m != 0 else float("-inf")
            right = nums[m+1] if m != n-1 else float("-inf")
            # print(f'i:{i}, j:{j}, left:{left}, right:{right}, m:{nums[m]}')
            
            if nums[m] > left and nums[m] > right:
                # print("In soln, ", soln)
                soln = m
                return 
            
            findPeak(i, m-1)
            findPeak(m+1, j)

        findPeak(0, n-1)
        # print(soln)
        return soln
        