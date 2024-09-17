from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r, s_map, t_map, n = 0,0, {}, Counter(t), len(s)
        need, found, soln = len(set(t)), 0, ''

        for key in t_map:
            s_map[key] = 0

        while r<n:
            ele = s[r]
            if ele in t_map:
                s_map[ele] +=1 
                if s_map[ele] == t_map[ele]:
                    found += 1
            
            # We will try to shrink the soln if a soln is found and shrinking will continue until we have a valid soln
            while found == need:
                if soln == '' or r-l+1 < len(soln):
                    soln = s[l:r+1]
                
                left_ele = s[l]
                if left_ele in t_map:
                    s_map[left_ele] -=1
                    if s_map[left_ele] < t_map[left_ele]:
                        found-=1
                
                l+=1

            r+=1


        return soln



            


        