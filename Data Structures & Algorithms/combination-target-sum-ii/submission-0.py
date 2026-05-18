class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()

        def backtrack(index, current, total):

            if total == target:
                res.append(current[:])
                return

            for i in range(index, len(candidates)):

                if i > index and candidates[i] == candidates[i-1]:
                    continue
                
                if total + candidates[i] <= target:
                    current.append(candidates[i])
                    backtrack(i+1, current, total + candidates[i])
                    current.pop()
                
                else:
                    return
        
        backtrack(0, [], 0)
        return res

        