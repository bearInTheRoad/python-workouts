from typing import List, Tuple


class Solution:
    """
    Jump Game II — the greedy here is BFS in disguise.

    TRAVERSAL vs SELECTION — don't conflate them:
      * Selection rule: "keep the farthest, ignore the rest" -> feels greedy.
      * Traversal shape: i walks 0 -> n-2 monotonically, no recursion, no
        backtracking. That monotonic sweep is the defining trait of BFS.
    i never actually jumps anywhere; it SCOUTS. At each index it records the
    farthest reachable distance; only when i catches up to `current` (the ring
    boundary) does it commit to the next ring. That is BFS layer-bounding.

    WHY LOOP TO n-1 (i.e. i in 0..n-2), NOT n:
      The last index is the DESTINATION, never a takeoff point. Two reasons:
        1. You never jump FROM the goal — processing nums[n-1] is wasted.
        2. It prevents a phantom jump: if i == current were true AT the last
           index, you've already arrived, yet jump += 1 would overcount by one.
           e.g. nums=[1,2]: with range(n) you'd do i=0 (jump=1, current=1)
           then i=1 hits i==current -> jump=2 (wrong, answer is 1).
      jump_greedy_n2 avoids this differently via explicit `>= end_pos` returns.

    WHY GREEDY IS OPTIMAL (not just "good enough"):
      It's BFS, and BFS reaches each node via a shortest path (equal edge
      cost = 1 jump). Min jumps = which ring the goal sits in.

    WHY YOU NEVER GET STUCK — only because the problem GUARANTEES the end is
    reachable. The algorithm relies on furthest > current at every forced jump.
      * furthest == current means NO takeoff in the ring extended reach -> dead
        end -> end is unreachable. Under the guarantee this cannot happen while
        current < end.
      * If the guarantee is broken (e.g. nums=[1,0,0,1]), the code silently
        returns a bogus jump count for an impossible journey. It never detects
        stuck. A self-defensive version needs one guard at the jump point:
            if furthest <= current: return -1   # dead end, unreachable

    THE GREEDY IS A COMPRESSION OF BFS:
      Textbook BFS: ring1={0}, ring2={1,2}, ring3={3,4,5}, goal in ring4 -> 4.
      This code collapses each ring to one int (its right edge, `furthest`).
      Valid because every index in a ring shares the same min-jump count, so
      storing only the boundary loses nothing. Feels greedy because of WHAT you
      store (the farthest); IS BFS because of HOW you walk (left-to-right rings).
    """

    def jump(self, nums: List[int]) -> Tuple[int, int, int]:
        return (
            self.jump_greedy_n_elegant(nums),
            self.jump_greedy_n(nums),
            self.jump_greedy_n2(nums),
        )

    def jump_greedy_n_elegant(self, nums: List[int]) -> int:
        # This is a solution coming from leetcode solution area
        # I wrote the function below but it was initially very cluncky
        # I wanna know how they differ and why I didn't come up with this solution
        #
        # start with n to reduce the computing time
        n = len(nums)
        # better naming - last_furthest is the same as current
        current = 0
        furthest = 0
        jump = 0
        # no need early return
        # but why both of us have to use n - 1 as end?
        for i in range(n - 1):
            furthest = max(furthest, i + nums[i])
            if i == current:
                jump += 1
                current = furthest
        return jump

    def jump_greedy_n(self, nums: List[int]) -> int:
        jump_count = 0
        last_furthest = 0
        new_furthest = 0
        if len(nums) == 1:
            return 0
        if last_furthest >= len(nums):
            return 1
        for i in range(len(nums) - 1):
            new_furthest = max(new_furthest, i + nums[i])
            if i == last_furthest:
                jump_count += 1
                last_furthest = new_furthest

        return jump_count

    def jump_greedy_n2(self, nums: List[int]) -> int:
        # time complexity: O(n^2)
        # also it's considering two steps ahead scenario and use greedy to find next step
        jump_count = 0
        pos = 0
        end_pos = len(nums) - 1
        while pos < end_pos:
            if pos + nums[pos] >= end_pos:
                return jump_count + 1
            furtherest = 0
            furtherest_index = 0
            for i in range(pos + 1, pos + nums[pos] + 1):
                if i + nums[i] >= end_pos:
                    return jump_count + 2
                if i + nums[i] > furtherest:
                    furtherest = i + nums[i]
                    furtherest_index = i
            jump_count += 1
            pos = furtherest_index
        return jump_count


nums = [1, 2]
print(Solution().jump(nums))

nums = [2, 3, 1]
print(Solution().jump(nums))

nums = [4, 1, 1, 3, 1, 1, 1]
print(Solution().jump(nums))

nums = [1, 2, 3]
print(Solution().jump(nums))

nums = [1, 1, 1, 1]
print(Solution().jump(nums))

nums = [7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]
print(Solution().jump(nums))

nums = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]
print(Solution().jump(nums))

nums = [2, 1]
print(Solution().jump(nums))

nums = [1, 2, 0, 1]
print(Solution().jump(nums))
