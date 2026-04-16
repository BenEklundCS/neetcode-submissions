class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}

        for c in s:
            if c not in map:
                map[c] = 1
            else:
                map[c] += 1
        
        for c in t:
            if c not in map:
                return False
            else:
                map[c] -= 1

        for val in map.values():
            if val != 0:
                return False 

        return True