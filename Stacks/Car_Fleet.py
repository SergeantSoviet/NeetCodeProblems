class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(pos,sp) for pos,sp in zip(position, speed)]
        pairs.sort(reverse=True)

        stack = []
        for pos,sp in pairs:
            stack.append((target - pos) / sp)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)