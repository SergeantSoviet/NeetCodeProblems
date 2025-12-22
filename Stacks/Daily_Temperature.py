class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = []
        for i in range(len(temperatures)):
            for j in range(i+1,len(temperatures)):
                if temperatures[j] - temperatures[i] > 0:
                    output.append(j-i)
                    break
                elif j == len(temperatures) - 1:
                    output.append(0)
        output.append(0)

        return output