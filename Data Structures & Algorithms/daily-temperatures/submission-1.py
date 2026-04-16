class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # store a pair, the value and index of each temp
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stackValue, stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append([t, i])
        return res




