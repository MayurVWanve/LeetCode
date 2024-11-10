class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {} # {postion -> bool}

        def backtrack(pos):
            if pos >= len(s):
                return True

            if pos in cache:
                return cache[pos]

            for word in wordDict:
                if word == s[pos:pos + len(word)]:
                    if backtrack(pos+len(word)):
                        cache[pos+len(word)] = True
                        return True
            
            cache[pos] = False
            return cache[pos]

        return (backtrack(0))

        