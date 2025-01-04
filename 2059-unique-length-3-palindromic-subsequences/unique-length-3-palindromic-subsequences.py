from collections import Counter
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left, right, soln = set(), Counter(s), set()
        
        for i in range(len(s)):
            right[s[i]] -=1
            if right[s[i]] == 0:
                del(right[s[i]])
            
            for j in range(26):
                m = chr(ord('a') + j)
                if m in left and m in right:
                    soln.add((m, s[i]))
                
            left.add(s[i])

        return len(soln)

        # count = Counter(s)  # Count of each letter
        # total = 0
        # for letter in count.keys():
        #     if count[letter]>=2:
        #         first=s.find(letter)
        #         last=s.rfind(letter)
        #         uniquechars=set(s[first+1:last])
        #         total+=len(uniquechars)
        # return total