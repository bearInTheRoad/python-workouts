"""LeetCode 134 — Gas Station.

Circular route of n stations: gas[i] is fuel collected at station i, cost[i] is
fuel burned driving from i to i+1 (wrapping around). Start with an empty tank and
return any station index from which a full lap is possible, else -1.

Correctness rests on one theorem: if sum(gas) >= sum(cost), a valid start always
exists. Both methods below lean on that for their skip/early-exit logic.
"""

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """Dispatcher; currently routes to the O(n) one-pass variant."""
        return self.canCompleteCircuit_OnePass(gas, cost)

    def canCompleteCircuit_BrutForce(self, gas: List[int], cost: List[int]) -> int:
        """Brute-force baseline: try every station as a start and simulate a full lap.

        O(n^2) time, O(1) space. Kept as the reference implementation to cross-check
        canCompleteCircuit_OnePass against identical inputs — correct, but too slow
        once n grows. (Method name has a typo, "BrutForce"; left as-is so existing
        callers and grep patterns keep matching.)
        """
        for startPoint in range(len(gas)):
            # Can't start where you can't even fuel the first outgoing edge.
            if gas[startPoint] < cost[startPoint]:
                continue
            else:
                step = 0
                currentPos = startPoint
                leftGas = 0
                # Edge cost for the hop we're about to attempt: leaving currentPos.
                nextPosCost = cost[startPoint]
                while step < len(gas):
                    leftGas = leftGas + gas[currentPos]
                    if leftGas < nextPosCost:
                        break  # tank ran dry before reaching the next station
                    # Commit one hop: pay the edge, land on the next station, and
                    # queue that station's outgoing edge as the next cost to beat.
                    currentPos = (currentPos + 1) % len(gas)
                    step += 1
                    leftGas = leftGas - nextPosCost
                    nextPosCost = cost[currentPos]
                if step == len(gas):
                    return startPoint
        return -1

    def canCompleteCircuit_OnePass(self, gas: List[int], cost: List[int]) -> int:
        """Greedy one-pass: O(n) time, O(1) space.

        Difference from canCompleteCircuit_BrutForce: on failure we don't restart at
        start+1. If a run started at `start` survives `step` hops and then fails,
        every station in [start, start+step) would also fail — starting later in that
        window leaves you with no more (and usually less) gas by the time you reach
        the failure point. So `start` jumps forward by `step`, collapsing the O(n^2)
        restart cost into a single linear scan.

        Known gap: the `<= 0` start guard below assumes some station has strictly
        positive net (gas[i] > cost[i]). Inputs where every net is 0 — e.g.
        gas=[2,2], cost=[2,2] — are solvable but this returns -1.
        """
        start = 0
        while start < len(gas):
            # Single-station lap is solvable iff gas[0] >= cost[0]. The ==0 sub-case
            # would be skipped by the `<= 0` guard below, so rescue it here first.
            if gas[start] - cost[start] == 0 and len(gas) == 1:
                return 0
            # A non-positive net can't seed a run: 0 net is equivalent to starting
            # one station later (you arrive there with the same 0 tank), and negative
            # net is hopeless. Advance and look for a strictly positive start.
            if gas[start] - cost[start] <= 0:
                start += 1
                continue
            leftGas = 0
            step = 0
            # Tank after paying the first edge (start -> start+1); the inner loop
            # layers each subsequent station's net on top of this seed.
            leftGas = gas[start] - cost[start]
            # Invariant: when step == k after the body, leftGas is the tank after
            # completing k+1 hops from `start` (indices wrap modulo n).
            # The bound is loose (`<= n` not `< n`): a valid circuit keeps the tank
            # non-negative around the loop, so the trailing wrap iteration is wasted
            # work but can't manufacture a false success.
            while leftGas >= 0 and step <= len(gas):
                step += 1
                # Refuel at the station just landed on, then pay its outgoing edge.
                leftGas = (
                    leftGas
                    + gas[(start + step) % len(gas)]
                    - cost[(start + step) % len(gas)]
                )
            if step >= len(gas):
                return start
            # Skip the entire window that provably can't contain a valid start.
            start += step
        return -1

    def canCompleteCircuit_prefix(self, gas: list[int], cost: list[int]) -> int:
        """Canonical prefix-sum solution: O(n) time, O(1) space, single pass.

        The cleanest of the three variants. Two ideas:
        1. Feasibility gate: if total gas < total cost, no circuit is possible.
        2. Restart on deficit: scan left to right accumulating net into `tank`.
           The moment `tank` goes negative, no station in [idx, i] can be a valid
           start (same window-skip argument as canCompleteCircuit_OnePass), so
           reset the candidate to i+1 and zero the tank. The feasibility gate
           guarantees a start exists, so the last reset wins.

        Unlike canCompleteCircuit_OnePass: no modulo, no single-station special
        case, no `<= 0` start guard — the deficit-reset handles every case,
        including the all-zero-net input (e.g. gas=[2,2], cost=[2,2]) that
        OnePass gets wrong.
        """

        if sum(gas) < sum(cost):
            return -1

        tank = idx = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                # Window [idx, i] is hopeless as a start region; restart just after it.
                tank, idx = 0, i + 1

        return idx


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
