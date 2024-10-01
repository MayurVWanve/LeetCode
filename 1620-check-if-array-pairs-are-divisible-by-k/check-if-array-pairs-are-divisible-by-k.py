class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = defaultdict(int)
        for ele in arr:
            temp = (k - (ele%k))%k
            if  temp in freq:
                if freq[temp] != 1:
                    freq[temp]-=1
                else:
                    del(freq[temp])
            
            else:
                freq[(ele%k)]+=1
        
        # print(freq)
        return True if len(freq) == 0 else False

        