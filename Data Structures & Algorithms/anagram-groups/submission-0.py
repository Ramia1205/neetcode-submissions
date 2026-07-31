class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}

        for word in strs:

            # make alphabet count list
            count = [0]*26

            for char in word:
                count[ord(char) - ord('a')] += 1
            
            # list finished

            # add list to dictionary
            key = tuple(count)

            if key not in groups:
                groups[key] = []
            
            groups[key].append(word)

        return list(groups.values())
