class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortedStringS = "".join(sorted(s))
        sortedStringT = "".join(sorted(t))
        if sortedStringS == sortedStringT:
            return True
        return False

            