class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # check lengths
        if len(s) != len(t):
            return False

        count = {}
        
        # finding counts of each letter
        for char in t:
            count[char] = count.get(char, 0) + 1
        
        # going thru s
        for char in s:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
        
        return True