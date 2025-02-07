class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # A, B, soln = {},{},[]
        
        # for i,j in queries:
        #     if i not in A:
        #         A[i] = j
        #         if j in B:
        #             B[j].append(i)
        #         else:
        #             B[j] = [i]
        #     else:
        #         val = A[i]
        #         if len(B[val]) > 1:
        #             B[val] = [x for x in B[val] if x!= i]
        #         else:
        #             del(B[val])
                    
        #         A[i] = j
        #         if j in B:
        #             B[j].append(i)
        #         else:
        #             B[j] = [i]
            
        #     soln.append(min(len(A), len(B)))
            
        # return soln
            
        numColorMap, colorNumMap = {}, defaultdict(list)
        soln = []

        for num, color in queries:

            if num not in numColorMap:
                numColorMap[num] = color
                colorNumMap[color].append(num)
            
            else:
                temp_color = numColorMap[num]
                if len(colorNumMap[temp_color]) > 1:
                    colorNumMap[temp_color].remove(num)
                else:
                    del(colorNumMap[temp_color])

                colorNumMap[color].append(num)
                numColorMap[num] = color

            # print(f'Col-num: {colorNumMap}, Num-Col: {numColorMap}')
            soln.append(len(colorNumMap))


        return soln
                
                