class Solution:
    def compressedString(self, word: str) -> str:

        comp, count, prev = "", 0, word[0]
        for i, curr in enumerate(word):
            if curr == prev:
                if count < 9:
                    count +=1
                else:
                    comp+= str(count)
                    comp+= curr
                    count = 1
                prev = curr
            else:
                comp+= str(count)
                comp+= prev
                count = 1
                prev = curr

        comp+= str(count)
        comp+= prev
        return comp
        