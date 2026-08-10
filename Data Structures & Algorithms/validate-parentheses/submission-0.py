class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s:

            # Opening bracket
            if char in "([{":
                stack.append(char)

            # Closing bracket
            else:
                # Stack is empty OR brackets don't match
                if not stack or stack[-1] != pairs[char]:
                    return False

                # Remove the matching opening bracket
                stack.pop()

        # Valid only if every opening bracket was matched
        return len(stack) == 0