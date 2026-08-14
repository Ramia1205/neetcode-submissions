class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        left = 0
        longest = 0

        for right in range(len(s)):
            # If we hit a duplicate, shrink from the left
            # until the duplicate is removed
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # Add the new character to the current window
            seen.add(s[right])

            # Window length = right - left + 1
            longest = max(longest, right - left + 1)

        return longest