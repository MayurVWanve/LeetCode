class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        s, count  = list(s), 0
        s_cpy = sorted(s,reverse = True)

        while s != s_cpy:
            i = 0
            count+=1
            while i < len(s)-1:
                if s[i] == '0' and s[i+1] == '1':
                    s[i], s[i+1] = '1', '0'
                    i+=2
                else:
                    i+=1
            
            # print(s,s_cpy)
        
        return count
                

        