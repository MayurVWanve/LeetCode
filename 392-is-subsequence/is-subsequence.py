class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j, s_len, t_len = 0, 0, len(s), len(t)

        if t_len < s_len:
            return False
        
        if s_len == 0:
            return True
        
        for j in range(t_len):
            if s[i] == t[j]:
                i+=1
            if i == s_len:
                return True
            
        return False

        
        