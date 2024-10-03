class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        remainder = total_sum % p

        # If the total sum is already divisible by p, return 0
        if remainder == 0:
            return 0

        prefix_sum_mod = 0
        min_length = len(nums)
        prefix_mod_index = {0: -1}  # To handle edge cases where prefix itself gives remainder

        for i, num in enumerate(nums):
            prefix_sum_mod = (prefix_sum_mod + num) % p
            target_mod = (prefix_sum_mod - remainder + p) % p

            # If we find a previous prefix sum with the required mod, we calculate the subarray length
            if target_mod in prefix_mod_index:
                min_length = min(min_length, i - prefix_mod_index[target_mod])

            # Update the hash map with the current prefix sum modulo and its index
            prefix_mod_index[prefix_sum_mod] = i

        # If we never found a valid subarray, return -1
        return min_length if min_length < len(nums) else -1
        
                

            
        