class Solution:
    def isFeasible(self, weight_limit: int, required_days: int, weights: list) -> bool:
        num_days = 0
        curr_weight = 0

        for weight in weights:
            if curr_weight + weight > weight_limit:
                num_days += 1
                curr_weight = 0

            curr_weight += weight

        if curr_weight != 0:
            num_days += 1

        return num_days <= required_days

    def shipWithinDays(self, weights: List[int], days: int) -> int:

        if not weights:
            return 0

        left = max(weights)
        right = sum(weights)

        min_weight = 0

        while left <= right:
            mid = (left + right) // 2

            if self.isFeasible(mid, days, weights):
                min_weight = mid
                right = mid - 1

            else:
                left = mid + 1

        return min_weight

        


        