class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            hashable = tuple(count)
            if hashable in hashmap:
                hashmap[hashable].append(s)
            else:
                hashmap[hashable] = [s]
        return list(hashmap.values())