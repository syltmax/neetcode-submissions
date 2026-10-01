class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1]
        right = [1]
        res = []

        for i in range(0, n-1):
            left.append(left[i] * nums[i])
            right.append(right[i] * nums[(-i-1)])
        for i in range(0, n):
            res.append(left[i] * right[-i-1])
        return res
