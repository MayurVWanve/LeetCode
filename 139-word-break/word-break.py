class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Base case
        # flag, cache = False, {}

        # if s == '':
        #     return True
        
        # for word in wordDict:
        #     n = len(word)
        #     if s[:n] == word:
        #         flag = self.wordBreak(s[n:], wordDict)
        #         cache[n]
        #         if flag == True:
        #             return flag
        
        # return flag

        cache, n = {}, len(s)

        def helper(pos):
            flag = False

            if pos in cache:
                return cache[pos]

            if pos == n:
                return True

            for word in wordDict:
                m = len(word)
                if s[pos: pos + m] == word:
                    flag = helper(pos+m)
                    cache[pos+m] = flag
                    if flag:
                        cache[pos] = flag
                        return flag

            return flag

        return helper(0)