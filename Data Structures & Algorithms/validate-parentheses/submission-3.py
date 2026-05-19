class Solution:
    def isValid(self, s: str) -> bool:
        
        the_map = {"}":"{", ")":"(", "]":"["}

        stack = []

        for char in s:

            if char not in the_map:
                stack.append(char)

            else:
                
                if len(stack) == 0:
                    return False
                
                match = stack.pop()

                if the_map[char] != match:
                    return False
        
        return (len(stack) == 0)