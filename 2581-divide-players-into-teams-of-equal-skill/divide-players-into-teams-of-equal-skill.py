class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        need = (sum(skill) *2)//n
        table, soln= defaultdict(int), []

        for ele in skill:
            # print(f'ele:{ele}, table:{table}, soln:{soln}')
            num = need - ele
            if num in table:
                soln.append(num*ele)
                if table[num] != 1:
                    table[num]-=1
                else:
                    del(table[num])

            else:
                table[ele]+=1
            
        # print(soln)
        return -1 if len(soln) != n//2 else sum(soln)

        