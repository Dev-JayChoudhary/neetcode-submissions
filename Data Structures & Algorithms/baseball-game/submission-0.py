class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "+":
                tmp1=stack[-1]
                tmp2=stack[-2]
                stack.append(tmp1+tmp2)
            elif op =="C":
                stack.pop()
            elif op=="D":
                stack.append(stack[-1]*2)
            else:
                stack.append(int(op))
        return sum(stack)