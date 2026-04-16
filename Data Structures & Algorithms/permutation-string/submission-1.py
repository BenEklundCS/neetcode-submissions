class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        def arraysEqual(arr1, arr2):
            if len(arr1) != len(arr2):
                return False
            for i in range(len(arr1)):
                if arr1[i] != arr2[i]:
                    return False
            return True

        if len(s1) > len(s2):
            return False

        # get a count of s1, for comparison IN s2
        count_of_s1 = [0] * 26
        for c in s1:
            count_of_s1[ord(c) - ord('a')] += 1

        # fixed sliding window, we must be looking for something of length s1
        l = 0
        r = len(s1) - 1

        print(l)
        print(r)

        # initialize a count on the l->r range over s2
        count_of_range_over_s2 = [0] * 26
        for i in range(r + 1):
            count_of_range_over_s2[ord(s2[i]) - ord('a')] += 1

        print(count_of_range_over_s2)

        while not arraysEqual(count_of_s1, count_of_range_over_s2):
            count_of_range_over_s2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            if r < len(s2):
                count_of_range_over_s2[ord(s2[r]) - ord('a')] += 1
            else:
                return False
        return True
        

        

        

        

        