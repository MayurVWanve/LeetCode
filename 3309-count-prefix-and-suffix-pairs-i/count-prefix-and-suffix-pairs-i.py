class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        c, n = 0, len(words)

        def check(str1, str2):
            return 1 if ((str1 == str2[0:len(str1)]) and (str1 == str2[len(str2)- len(str1):])) else 0

        for i in range(n):
            for j in range(i+1, n):
                c+=check(words[i], words[j])


        return c
        