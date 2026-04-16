class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            if tuple(count) in hashMap:
                hashMap[tuple(count)].append(s)
            else:
                hashMap[tuple(count)] = [s]
        
        return list(hashMap.values())