class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Initialize character count dictionaries
        s_count = {}
        t_count = {}
        
        # Count characters in s
        for char in s:
            s_count[char] = s_count.get(char, 0) + 1
        
        # Count characters in t
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
        
        # Compare character counts
        for char in s_count:
            if char not in t_count or s_count[char] != t_count[char]:
                return False
        
        return True
