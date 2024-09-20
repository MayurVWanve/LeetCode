class Codec:
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for ele in strs:
            n = len(ele)
            temp = str(n) + "#" + ele
            encoded_str += temp
        
        # print(encoded_str)
        return encoded_str
        

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i< len(s):
            t = ''
            while s[i] != '#':
                t += s[i]
                i+=1
            n = int(t)
            temp = s[i+1:i+1+n]
            res.append(temp)
            i = i+n+1
        return res

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))