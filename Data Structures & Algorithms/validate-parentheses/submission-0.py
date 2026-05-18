class Solution:
    def isValid(self, s: str) -> bool:
        
        the_map = {"}":"{", ")":"(", "]":"["}

        stack = []

        for char in s:

            if char not in the_map:
                stack.append(char)
            
            else:
                if not stack:
                    return False

                compare_char = stack.pop()

                if compare_char != the_map[char]:
                    return False

        
        return not stack