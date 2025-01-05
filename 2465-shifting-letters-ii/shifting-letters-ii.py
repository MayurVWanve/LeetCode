class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shift = [0] * (len(s)+1)
        s = list(s)

        for start, end, direction in shifts:
            if direction == 1:
                shift[start] +=1
                shift[end+1] -=1
            else:
                shift[start] -=1
                shift[end+1] +=1
        
        curr_shift = 0
        for i in range(len(s)):
            curr_shift+=shift[i]
            s[i] = chr(((ord(s[i]) - ord('a') + curr_shift)%26) + ord('a'))

        return ''.join(s)