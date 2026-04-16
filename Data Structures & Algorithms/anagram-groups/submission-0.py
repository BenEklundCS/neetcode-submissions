class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a hash_map, the hash_map will use a
        # sorted string, s, from strs, as the key
        # allowing easy check of anagram status
        # because if sorted(x) == sorted(y) they are anagrams
        hash_map = {}
        # Loop over the string values in strs
        for s in strs:
            # Sort the string
            sorted_s = ''.join(sorted(s))
            # Check if the sorted string is a key in the hash_map
            if sorted_s not in hash_map:
                # If not, add it to the dict, and add its unsorted
                # version to the list
                hash_map[sorted_s] = [s]
            # Otherwise it is in hash_map, so we just append s
            else:
                hash_map[sorted_s].append(s)
        # Now we have a hash_map that contains keys we no longer need
        # and the values are each array we need to return from this function
        
        # Create a result array
        result = []
        # Get all sub arrays from hash_map
        for arr in hash_map.values():
            # Append to result
            result.append(arr)
        return result
        
