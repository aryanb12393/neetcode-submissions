class Solution:
    def isValid(self, s: str) -> bool:
        
        the_map = {"}":"{", ")":"(", "]":"["}

        stack = []

        for char in s:

            if char not in the_map:
                stack.append(char)

            else:

                match = stack.pop()

                if the_map[char] != match:
                    return False
        
        return True