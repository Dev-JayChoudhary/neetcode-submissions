class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
          stack =[]
          for token in tokens:

            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))

            else:
                b = stack.pop()
                a = stack.pop()

                match token:
                    case "+":
                        stack.append(a + b)
                    case "-":
                        stack.append(a - b)
                    case "*":
                        stack.append(a * b)
                    case "/":
                        stack.append(int(a / b))   # truncate toward zero

          return stack[-1]