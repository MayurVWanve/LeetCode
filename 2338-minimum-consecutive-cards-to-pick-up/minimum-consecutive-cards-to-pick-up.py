class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        # l, lookup, soln, n, r = 0, {}, -1, len(cards), 0
        # lookup[cards[0]] = 0

        # for r in range(1, n):
        #     if cards[r] in lookup:
        #         l = lookup[cards[r]]
        #         soln = r-l+1
        #         for i in range(0,l+1):
        #             del(lookup[cards[i]])
        #         lookup[cards[r]] = r
        #         break
        #     else:
        #         lookup[cards[r]] = r

        # l, r = l+1, r+1
        # # print(l,r,soln, lookup)
        # while r < n:
        #     # print(f'l:{l}. r:{r}, lookup:{lookup}')
        #     if cards[r] in lookup:
        #         new_l = lookup[cards[r]]
        #         for i in range(l, new_l+1):
        #             del(lookup[cards[i]])
        #         soln = r-new_l+1
        #         l = new_l
        #         lookup[cards[r]] = r

        #     else:
        #         lookup[cards[r]] = r
        #         del(lookup[cards[l]])
            
        #     l,r = l+1, r+1

        # return soln

        l,n, soln, lookup = 0, len(cards), float('inf'), {}

        if n == 1:
            return -1
        lookup[cards[0]] = 0
        for r in range(1, n):
            if cards[r] in lookup:
                new_l = lookup[cards[r]]
                for i in range(l, new_l+1):
                    del(lookup[cards[i]])
                l = new_l+1
                soln = min(soln, r-l+2)
    
            lookup[cards[r]] = r


        return soln if soln != float('inf') else -1
        
