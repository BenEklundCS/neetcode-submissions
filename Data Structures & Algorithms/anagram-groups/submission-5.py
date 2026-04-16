class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {} # map count arrays to lists of strings :)
        for s in strs:
            count = [0] * 26 # <--
            for c in s:
                count[ord(c) - ord('a')] += 1
            hashableCount = tuple(count)
            if hashableCount in hashMap:
                hashMap[hashableCount].append(s)
            else:
                hashMap[hashableCount] = [s]

        return list(hashMap.values())
