class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        thisDict = {}
        for x in strs:
            xsorted = "".join(sorted(x))
            if xsorted not in thisDict:
                thisDict[xsorted] = []
            thisDict[xsorted].append(x)
        return list(thisDict.values())