class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            #encode in formate [Length] + [#] + [string]
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            # Find the position of the length delimiter '#'
            j = i
            while s[j] != '#':
                j += 1
            
            # Extract the length and advance pointer
            length = int(s[i:j])
            i = j + 1
            
            # Extract the string based on length
            res.append(s[i : i + length])
            
            # Advance main pointer past the string
            i += length

        return res


            

