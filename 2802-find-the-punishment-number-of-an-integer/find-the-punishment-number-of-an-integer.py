class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 0

        def helper(pos, curr, target, temp):
            if pos == len(temp) and curr == target:
                return True

            for j in range(pos, len(temp)):
                if helper(j+1, curr + int(temp[pos:j+1]), target, temp):
                    return True
            return False

        for i in range(1,n+1):
            if helper(0, 0, i, str(i*i)):
                ans += (i*i)
        return ans
        