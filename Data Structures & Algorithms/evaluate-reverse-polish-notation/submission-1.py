import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operatoren = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        for t in tokens:
            if t not in operatoren:
                stack.append(t)
            else:
                first = int(stack.pop())
                second = int(stack.pop())
                zwr = operatoren[t](second, first)
                stack.append(zwr)
        return int(stack.pop())
            