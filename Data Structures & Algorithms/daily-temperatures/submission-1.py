class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = []

        for i, curr_temp in enumerate(temperatures):
            while stack and curr_temp > temperatures[stack[-1]]:
                stack_idx = stack.pop()
                res[stack_idx] = i - stack_idx
                print(stack)
            stack.append(i)

        return res