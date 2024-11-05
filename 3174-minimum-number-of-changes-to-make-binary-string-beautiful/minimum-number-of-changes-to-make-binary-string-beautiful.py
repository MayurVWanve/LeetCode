from collections import Counter
class Solution:
    def minChanges(self, s: str) -> int:
        c = Counter(s)
        if len(s)%2 != 0:
            return min(c['0'], c['1'])

        else:
            count = 0
            for i in range(0, len(s),2):
                if s[i] != s[i+1]:
                    count+=1
            return count

        

        