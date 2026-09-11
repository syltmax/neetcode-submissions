class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        thisDict = {}
        for x in nums:
            thisDict[x] = 1 + thisDict.get(x, 0)

        arr = []
        for num, cnt in thisDict.items():
            arr.append([cnt, num])

        arr.sort()
        res = []
        for x in range(0, k):
            res.append(arr.pop()[1])
        
        return res


        
