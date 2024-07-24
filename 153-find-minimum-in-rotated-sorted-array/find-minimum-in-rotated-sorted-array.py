class Solution:
    def findMin(self, nums: List[int]) -> int:
        i,j = 0, len(nums)-1

        if len(nums) == 1:
            return nums[0]

        def binSearch(i,j):

            while i<=j:
                mid = (i+j)//2

                #Found the Largest ele
                if nums[mid] >= nums[mid-1] and nums[mid] >= nums[mid+1]:
                    return nums[mid+1]

                #Found the Largest ele
                if nums[mid] <= nums[mid-1] and nums[mid] <= nums[mid+1]:
                    return nums[mid]

                #Normal Case
                if nums[mid] >= nums[i] and nums[mid] >= nums[j]:
                    i = mid + 1
                
                else:
                    j = mid - 1



        

        return binSearch(i,j)
        