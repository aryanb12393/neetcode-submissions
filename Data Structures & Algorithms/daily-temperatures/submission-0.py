class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            curr_temp = temperatures[i]
            while stack and curr_temp > temperatures[stack[-1]]:
                stack_idx = stack.pop()
                res[stack_idx] = i - stack_idx
            stack.append(i)


        return res