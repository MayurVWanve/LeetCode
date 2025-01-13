from collections import Counter
class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        s = list(s)

        lookup, count = Counter(s), 0

        for key, value in lookup.items():
            count +=2 if (value%2 == 0) else 1

        return count
        