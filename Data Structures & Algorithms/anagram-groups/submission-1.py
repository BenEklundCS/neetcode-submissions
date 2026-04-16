class Solution:
    def isAnagram(self, str1, str2) -> bool:
        counter = {}
        for s in str1:
            if s not in counter:
                counter[s] = 1
            else:
                counter[s] += 1
        for s in str2:
            if s not in counter:
                return False
            else:
                counter[s] -= 1
        return all(i == 0 for i in counter.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = []
        for s in strs:
            if len(anagram_groups) == 0:
                anagram_groups.append([s])
            else:
                appended = False
                for i, val in enumerate(anagram_groups):
                    if self.isAnagram(s, val[0]):
                        anagram_groups[i].append(s)
                        appended = True
                if appended == False:
                    anagram_groups.append([s])
                        
        return anagram_groups
            
        