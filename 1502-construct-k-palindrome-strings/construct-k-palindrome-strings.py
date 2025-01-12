from collections import Counter
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        s = list(s)
        count, extra = Counter(s), 0

        for key, value in count.items():
            if value%2 != 0:
                extra+=1

        return True if extra <= k and (n>=k) else False
        