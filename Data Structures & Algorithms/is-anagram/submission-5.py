class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        if length of s & t and occurance of each char in s & t are same hence anagram
        '''
        if len(s) != len(t):
            return False
       
        map_of_s = {} #hashtable for each char with their ocuurance 
        for char in s:
            map_of_s[char] = map_of_s.get(char, 0) + 1

        #check count of next string exist in stirng s if yes then substract by 1 if its 0 or lesser hence occurance of char in s is lesser than string t
        for char in t:
            if char not in map_of_s:
                return False
       
            map_of_s[char] -= 1

            if map_of_s[char] < 0:
                return False
        
        #hence all is ok
        return True

            



        
        
        