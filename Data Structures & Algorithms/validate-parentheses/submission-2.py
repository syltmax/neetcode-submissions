class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = { '(':')',
                '{':'}',
                '[':']'}
        for p in s:
            if p in dic.keys():
                stack.append(p)
            else:
                if stack:
                    k = stack.pop()
                    if dic[k] != p:
                        return False
                else:
                    return False
        return True if not stack else False