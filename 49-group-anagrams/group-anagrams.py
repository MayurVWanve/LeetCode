class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        cache = defaultdict(list)
        def get_key(word):
            temp = [0] * 26
            for chr in word:
                temp[ord(chr) - ord('a')]+=1
            return tuple(temp)
        for word in strs:
            key = get_key(word)
            cache[key].append(word)
    

        return cache.values()
        