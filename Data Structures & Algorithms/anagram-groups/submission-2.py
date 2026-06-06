from collections import defaultdict
class Solution:
    # def isAnagram(s1, s2):
    #     if len(s1) != len(s2):
    #         return False
    #     #hashmap to count frequence of each character in first string
    #     count = {}
    #     for c in s1:
    #         count[c] = count.get(c, 0) + 1
    #     #now with hashmap (count) check occurace of each character is same in string2
    #     for c in s2:
    #         if c not in count:
    #             return False
    #         #else decrease count
    #         count[c] -= 1
    #         #if count become < 0 hence occurance of character in string1 is less than string2
    #         if count[c] < 0:
    #             return False
            
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagrams = []
        # for i, s1 in enumerate(strs):
        #     temp_anagrams = [s1]
        #     for s2 in len(i+1,strs):
        #         if isAnagram(s1, s2):
        #             temp_anagrams.add(s2)
        #     if temp_anagram is not empty:
        #         anagram.add(temp_anagram)
        # return anagrams
        #------ NEW APPROACH ----#
        anagrams = defaultdict(list) #automatically create a [] list

        for s in strs:
            key = "".join(sorted(s)); #sorted return sorted string so cat and tac become same key
            anagrams[key].append(s) #if key is not in the anagram automatically created and assigend

        return list(anagrams.values()) #now returning only values of dictionary(dict) in list after typecast

        # -------- another approach can be c - 'a' = some digit means it will create uniqe kye
        





        