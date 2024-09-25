class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # soln = 0
        # arr1, arr2 = list(set(arr1)), list(set(arr2))
        # arr1.sort(), arr2.sort()

        # def prefix(x,y):
        #     count, i = 0, 0
        #     n = min(len(x), len(y))
        #     while i<n:
        #         if x[i] != y[i]:
        #             return count
        #         count+=1
        #         i+=1
        #     return count
                

        # for x in arr1:
        #     for y in arr2:
        #         x, y = str(x), str(y)
        #         n = prefix(x,y)
        #         # print(n, x, y)
        #         soln = max(soln, n)


        # return soln

        if len(arr2) < len(arr1):
            arr1, arr2 = arr2 , arr1 # We want the smaller list to be in hashset

        hashset, soln = set(), 0

        for ele in arr1:
            while ele and ele not in hashset:
                # print(ele)
                hashset.add(ele)
                ele//=10

        for ele in arr2:
            while ele:
                if ele in hashset:
                    soln = max(soln, len(str(ele)))
                    break
                ele//=10

        return soln
