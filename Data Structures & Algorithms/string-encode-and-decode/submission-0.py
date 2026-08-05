class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            # Format: <length>#<word>
            # Example: "cat" -> "3#cat"
            encoded += str(len(word)) + "#" + word

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):

            # Find the '#' that separates the length from the word
            j = i
            while s[j] != "#":
                j += 1

            # Read the length
            length = int(s[i:j])

            # Move past '#'
            j += 1

            # Extract the word
            decoded.append(s[j:j + length])

            # Move to the next encoded string
            i = j + length

        return decoded
