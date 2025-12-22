class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def calculate(a,b,op):
            if op == '+':
                return a+b
            elif op == '-':
                return a-b
            elif op == '*':
                return a*b
            elif op == '/':
                return a/b

        nums = []
        ops = []

        for i in range(len(tokens)):
            if tokens[i] == '+' or tokens[i] == '-' or tokens[i] == '*' or tokens[i] == '/':
                output = calculate(int(nums[-2]), int(nums[-1]), tokens[i])
                nums.pop()
                nums.pop()
                nums.append(output)
            else:
                nums.append(tokens[i])

        return int(nums[0])