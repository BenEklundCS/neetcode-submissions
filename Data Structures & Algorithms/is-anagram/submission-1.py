class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = {}
        for c in s:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1
        
        for c in t:
            if c in counter:
                counter[c] -= 1
            else:
                return False
        
        return all(value == 0 for value in counter.values())