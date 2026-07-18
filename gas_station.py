from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        return self.canCompleteCircuit_OnePass(gas, cost)

    def canCompleteCircuit_BrutForce(self, gas: List[int], cost: List[int]) -> int:
        for startPoint in range(len(gas)):
            # if the gas at the point is smaller than cost
            # you can't start here
            if gas[startPoint] < cost[startPoint]:
                continue
            else:
                step = 0
                currentPos = startPoint
                leftGas = 0
                nextPosCost = cost[startPoint]
                while step < len(gas):
                    leftGas = leftGas + gas[currentPos]
                    if leftGas < nextPosCost:
                        break
                    currentPos = (currentPos + 1) % len(gas)
                    step += 1
                    leftGas = leftGas - nextPosCost
                    nextPosCost = cost[currentPos]
                if step == len(gas):
                    return startPoint
        return -1

    def canCompleteCircuit_OnePass(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        while start < len(gas):
            # print(start)
            if gas[start] - cost[start] == 0 and len(gas) == 1:
                return 0
            if gas[start] - cost[start] <= 0:
                start += 1
                continue
            leftGas = 0
            step = 0
            leftGas = gas[start] - cost[start]
            while leftGas >= 0 and step <= len(gas):
                step += 1
                leftGas = (
                    leftGas
                    + gas[(start + step) % len(gas)]
                    - cost[(start + step) % len(gas)]
                )
                # print("step ", step)
                # print("gas ", leftGas)
            if step >= len(gas):
                return start
            start += step
        return -1


solution = Solution()
gas = [1, 2, 3, 4, 5, 5, 70]
cost = [2, 3, 4, 3, 9, 6, 2]
print(solution.canCompleteCircuit(gas, cost))

print("-----------------------------")
solution = Solution()
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(solution.canCompleteCircuit(gas, cost))

print("-----------------------------")
solution = Solution()
gas = [2, 3, 4]
cost = [3, 4, 3]
print(solution.canCompleteCircuit(gas, cost))

print("-----------------------------")
solution = Solution()
gas = [3, 1, 1]
cost = [1, 2, 2]
print(solution.canCompleteCircuit(gas, cost))

print("-----------------------------")
solution = Solution()
gas = [3, 3, 4]
cost = [3, 4, 4]
print(solution.canCompleteCircuit(gas, cost))

print("-----------------------------")
solution = Solution()
gas = [4, 5, 2, 6, 5, 3]
cost = [3, 2, 7, 3, 2, 9]
print(solution.canCompleteCircuit(gas, cost))

print("-----------------------------")
solution = Solution()
gas = [2]
cost = [2]
print(solution.canCompleteCircuit(gas, cost))


print("-----------------------------")
solution = Solution()
gas = [4, 5, 3, 1, 4]
cost = [5, 4, 3, 4, 2]
print(solution.canCompleteCircuit(gas, cost))
