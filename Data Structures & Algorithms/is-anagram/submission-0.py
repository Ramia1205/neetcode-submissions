class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        t_letters = {}

        for t_letter in t:
            if t_letter not in t_letters:
                t_letters[t_letter] = 1
            else:
                t_letters[t_letter] += 1
        
        for s_letter in s:
            if s_letter in t_letters and t_letter != 0:
                t_letters[t_letter] -= 1
            else:
                return False
        return True