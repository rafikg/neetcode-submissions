class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)==1:
            return int(tokens[0])
        stack = []
        for x in tokens:
            if x not in ["+", "-", "*", "/"]:
                stack.append(x)
            else:
                right = int(stack.pop())
                left = int(stack.pop())
                match x:
                    case "+":
                        result = right + left
                    case "-":
                        result = left-right
                    case  "*":
                        result = left*right
                    case "/":
                        result = int(left/right)
                stack.append(result)
        return result



        