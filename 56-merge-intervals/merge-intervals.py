class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        soln, n = [], len(intervals)

        #Base Case
        if n == 1:
            return intervals

        intervals.sort(key = lambda x: x[0])
        soln.append(intervals[0])

        for i in range(1,n):
            start, end = soln[-1]
            # print(f'Before Merge : {soln}')
            if intervals[i][0] <= end:
                soln[-1][1] = max(intervals[i][1], soln[-1][1])
            else:
                soln.append(intervals[i])
            
            # print(f'After Merge : {soln}')

        return soln

        
        