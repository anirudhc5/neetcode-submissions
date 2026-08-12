class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        indices = {}
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            # print(i, stack)
            val = temperatures[i]
            if val not in indices:
                indices[val] = [i]
            else:
                indices[val].append(i)
            while stack and val > stack[-1]:
                top = stack.pop()
                topidx = indices[top].pop()
                ans[topidx] = i - topidx
            stack.append(val)
        return ans
