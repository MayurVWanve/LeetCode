class Solution:
    def numDecodings(self, s: str) -> int:
        table, n = {}, len(s) 

        def helper(pos):

            if pos in table:
                return table[pos]
        
            
            if pos == n:
                return 1

            if pos > n or s[pos] == '0':
                return 0

            if s[pos] == '1' or (s[pos] == '2' and pos<n-1 and s[pos+1] in ('0','1','2','3','4','5','6')):
                table[pos] = helper(pos+2)

            table[pos] = table.get(pos, 0) + helper(pos+1)
            
            return table[pos]


        return helper(0)


        

        