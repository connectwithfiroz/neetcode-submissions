class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #------------   (1 - Failed) ------------ #
        #if lenght is diff then definataly not anagram
        # if len(s) != len(t):
        #     return False;
        # #loop on first or second word
        # for char in s:
        #     if char not in t:
        #         return False
        # return True

        #------------   (2) ------------ #
        if len(s) != len(t):
            return False
        
        #Create a frequency table of each character
        count = {}
        for c in s:
            count[c] = count.get(c,0) + 1#if count available increase by 1 or initialize with 0 and increment 0
            
        #Loop for each char of second word
        for c in t:
            #if charter not available in first word then no need to check futher
            if c not in count:
                return False
            #else decrease count
            count[c] -= 1;
            #if count of a char become less than 0 hence t has more character than string t
            if count[c] < 0:
                return False

        #Hence both word is Anagram
        return True;

