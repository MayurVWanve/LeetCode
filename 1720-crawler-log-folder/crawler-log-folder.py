class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for word in logs:
            if word == '../' :
                if count > 0:
                # print("In loop 1")
                    count-=1
            elif word == './':
                # print("In loop 2")
                continue
            else:
                # print("In loop 3")
                count+=1
        
        return max(0,count)
                

        