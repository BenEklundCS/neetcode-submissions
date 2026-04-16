class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combos = {}

        def backtrack(chosen, remaining):
            s = sum(chosen)
            print(str(chosen))
            if s == target and str(chosen) not in combos:
                chosen.sort() # avoid different chosen order-conflicts
                combos[str(chosen[:])] = 1
            elif s > target:
                chosen = []
            else:
                for i in range(len(remaining)):
                    chosen.append(remaining[i])
                    backtrack(chosen, remaining[i+1:])
                    chosen.pop()

        backtrack([], candidates)
        res = [eval(key) for key in combos]
        return res
