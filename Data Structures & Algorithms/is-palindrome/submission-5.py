class Solution:
    def isPalindrome(self, s: str) -> bool:
        first = 0
        last = len(s)-1
        while first < last:
            while first < last and not s[first].isalnum():
                first += 1
            while first < last and not s[last].isalnum():
                last -= 1
            if s[first].lower() == s[last].lower():
                first += 1
                last -= 1
            else:
                return False
        return True