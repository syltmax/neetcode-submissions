class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        res = []
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums) -1
            while l < r:
                summe = nums[i] + nums[l] + nums[r]
                if summe == 0:
                    if [nums[i],nums[l],nums[r]] in res:
                        l += 1
                        r -= 1
                        continue
                    else:
                        res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                elif summe > 0:
                    r -= 1
                else:
                    l += 1
        return res if res else []