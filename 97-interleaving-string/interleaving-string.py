class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2,l3, i,j,k, dp = len(s1), len(s2), len(s3), 0,0,0, {}

        if l1 + l2 != l3:
            return False

        def helper(i,j,k):
            if i == (l1) and j == (l2) and k == (l3):
                return True

            if (i,j) in dp:
                return dp[i,j]

            dp[i,j] = False

            if i > l1 or j> l2 or k > l3 or (i< l1 and s1[i] != s3[k] and j<l2 and s2[j] != s3[k]):
                return False
            
            if i<l1 and s1[i] == s3[k] and j<l2 and s2[j] == s3[k]:
                dp[i,j] = helper(i+1,j,k+1) or helper(i,j+1,k+1)

            elif j<l2 and s2[j] == s3[k]:
                dp[i,j] = helper(i,j+1,k+1)

            elif i<l1 and s1[i] == s3[k]:
                dp[i,j] = helper(i+1,j,k+1)

            return dp[i,j]



        return helper(0,0,0)

        