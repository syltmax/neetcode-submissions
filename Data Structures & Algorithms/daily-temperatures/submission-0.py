class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                firstelem = stack.pop()
                dif = i - firstelem[1]
                res[firstelem[1]] = dif
            stack.append([temperatures[i], i])
        
        return res
