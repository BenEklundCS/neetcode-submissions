class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        product = 1
        for n in nums:
            if n == 0:
                zero_count += 1
            else:
                product *= n
        if zero_count > 1:
            return [0 for i in range(len(nums))]
        elif zero_count == 1:
            res = []
            for n in nums:
                if n == 0:
                    res.append(product)
                else:
                    res.append(0)
            return res
        else:
            res = []
            for n in nums:
                res.append(product // n)
            return res

        

        