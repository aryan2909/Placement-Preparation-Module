class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = {}
        magazine_count = {}
        
        # Count the occurrences of each letter in ransomNote
        for char in ransomNote:
            ransom_count[char] = ransom_count.get(char, 0) + 1
        
        # Count the occurrences of each letter in magazine
        for char in magazine:
            magazine_count[char] = magazine_count.get(char, 0) + 1
        
        # Check if ransomNote can be constructed
        for char, count in ransom_count.items():
            if char not in magazine_count or count > magazine_count[char]:
                return False
        
        return True
