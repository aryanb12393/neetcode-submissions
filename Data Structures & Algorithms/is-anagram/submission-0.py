class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if (len(s) != len(t)):
            return False

        the_dict = {}

        for character in s:
            if (character not in the_dict):
                the_dict[character] = 1
            else:
                the_dict[character] += 1
        
        
        for character in t:

            if (character not in the_dict):
                return False
            
            the_dict[character] -= 1

            if (the_dict[character] < 0):
                return False

        return True