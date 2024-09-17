from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
    
        # Step 1: Count the characters in t
        t_count = Counter(t)
        required = len(t_count)  # Number of unique characters in t
        
        # Left and right pointers of the sliding window
        left, right = 0, 0
        
        # Keep track of the number of unique characters in the current window that match t's count
        formed = 0
        
        # Dictionary to count the characters in the current window
        window_counts = {}
        
        # (window length, left, right) tuple to keep track of the minimum window
        ans = float("inf"), None, None
        
        # Step 2: Expand the window by moving the right pointer
        while right < len(s):
            char = s[right]
            # Add the current character to the window's character count
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # If the current character's count matches the required count in t, increment `formed`
            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1
            
            # Step 3: Try to contract the window until it stops being valid
            while left <= right and formed == required:
                char = s[left]
                
                # Update the answer if this window is smaller
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                
                # Remove the character at the left pointer from the window's count
                window_counts[char] -= 1
                if char in t_count and window_counts[char] < t_count[char]:
                    formed -= 1
                
                # Move the left pointer forward to contract the window
                left += 1
            
            # Move the right pointer forward to expand the window
            right += 1
        
        # Step 4: Return the minimum window if found, otherwise return an empty string
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]

            


        