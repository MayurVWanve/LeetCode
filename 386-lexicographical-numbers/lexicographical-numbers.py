class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        def dfs(curr):
            curr *=10
            if curr > n:
                return

            for i in range(10):
                new_curr = curr + i
                if new_curr > n:
                    return 
                res.append(new_curr)
                dfs(new_curr)


        for i in range(1, 10):
            num = i 
            # print(num)
            if num > n:
                return res
            res.append(num)
            # print(res)
            dfs(num)

        # print("Res before the return ", res)
        return res