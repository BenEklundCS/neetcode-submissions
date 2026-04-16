class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in hash_map:
                hash_map[sorted_s] = [s]
            else:
                hash_map[sorted_s].append(s)
        result = []
        # Get all sub arrays from hash_map
        for arr in hash_map.values():
            # Append to result
            result.append(arr)
        return result
        

            
        