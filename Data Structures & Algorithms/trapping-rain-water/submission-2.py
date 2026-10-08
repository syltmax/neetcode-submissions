class Solution:
    def trap(self, height: List[int]) -> int:
        arr1 = []
        num1 = 0
        for i in range(len(height)-1, -1, -1):
            num1 = max(num1, height[i])
            arr1.append(num1)
        arr1.reverse()
        arr2 = []
        num2 = 0
        for i in range(len(height)-1):
            num2 = max(num2, height[i])
            arr2.append(num2)
        res = 0
        for i in range(len(height) - 1):
            res += min(arr1[i], arr2[i]) - height[i]
        return res