class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            sorted_s = ''.join(sorted(s)) # sorting is more efficient than counting occurences
            if sorted_s in d:
                d[sorted_s].append(s)
            else:
                d[sorted_s] = [s]
        return list(d.values())