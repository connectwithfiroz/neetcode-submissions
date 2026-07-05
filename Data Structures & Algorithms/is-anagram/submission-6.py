class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #we need a dictionary to store first words character as key and count as value then we need to compare with second words if both counts equal hence anagram 
        #if both length of both string are not same hence not anagram
        if len(s) != len(t):
            return False
        
        #let map the char=>count
        map_of_s = dict()
        for c in s:
            # if current charcter in dict then get the count else assume 0 and increase by 1
            map_of_s[c] = map_of_s.get(c, 0) + 1

        #loop on second word and once we found character  we'll decrease by 1
        for c in t:
            map_of_s[c] = map_of_s.get(c, 0) - 1
            if map_of_s[c] < 0:
                #if not in map hence extra character
                return False
        
        return True
        


        