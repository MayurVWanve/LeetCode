class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        #Odd Length Strings
        for i in range(len(s)):
            l,r = i,i
            while l>=0 and r < len(s) and s[l] == s[r]:
                # print("Palindrome Found: ",s[l:r+1] )
                count+=1
                l-=1
                r+=1

        # Even Length Strings
        for i in range(len(s)):
            l,r = i,i+1
            while l>=0 and r < len(s) and s[l] == s[r]:
                # print("Palindrome Found: ",s[l:r+1] )
                count+=1
                l-=1
                r+=1

        return count

        