class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary_search(l, r):
            while l <= r:
                m = (l+r)//2
                if nums[m] == target:
                    return m

                if nums[r] >= nums[m]: #Right Sorted array
                    if target < nums[m] or target >nums[r]:
                        r = m-1
                    else:
                        l = m+1


                else: # Left Sorted Array
                    if target < nums[l] or target > nums[m]:
                        l = m+1
                    else:
                        r = m-1
            
            return -1
        
        return binary_search(0, len(nums)-1)


        