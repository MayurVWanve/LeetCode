class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        # print(f'Intervals: {intervals}')

        s1, e1, soln, n = intervals[0][0], intervals[0][1], [], len(intervals)
        soln.append([s1,e1])

        for i in range(1,n):
            s2,e2 = intervals[i][0], intervals[i][1]
            # print(f'i, start end: {i, s2,e2}')
            flag = False
            for j in range(len(soln)):
                s1,e1 = soln[j][0], soln[j][1]
                if s2 >= e1:
                    soln[j][1] = e2
                    flag = True
                    # print(f'Merged with {s1,e1}. Current soln : {soln}')
                    break
            
            if not flag:
                # print(f'Not able to merge. Creating new Room. Current soln: {soln}')
                soln.append([s2,e2])
            
        return len(soln)