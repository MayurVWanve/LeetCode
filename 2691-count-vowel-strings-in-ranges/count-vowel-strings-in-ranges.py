class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        word_check, vowels, n, soln = [0] * len(words), set('aeiou'), len(words), []

        def check_vowels(s):
            if s[0] in vowels and s[-1] in vowels:
                return 1
            return 0 

        word_check[0] = check_vowels(words[0])
        for i in range(1,n):
            word_check[i] = word_check[i-1] + check_vowels(words[i])

        for query in queries:
            l, r = query
            if l == 0:
                soln.append(word_check[r])
            else:
                soln.append(word_check[r] - word_check[l-1])
        

        return soln
        