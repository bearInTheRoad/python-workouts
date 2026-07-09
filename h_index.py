from typing import List, Tuple


class Solution:
    def hIndex(self, citations: List[int]) -> Tuple[int, int, int]:
        return (
            self.hIndex_timsort(citations),
            self.hindex_bucketsort(citations),
            self.hindex_bucketsort_linear(citations),
        )

    def hIndex_timsort(self, citations: List[int]) -> int:
        """
        h-index via Python's built-in sort (Timsort). O(n log n) time, O(n) space.

        IDEA: sort citations descending, then scan. After sorting, citations[i]
        is the citation count of the (i+1)-th most-cited paper. The h-index is
        the largest h such that the top h papers each have >= h citations.

        SCAN RULE: walk i from 0. At each i we ask "is paper i+1 (the (i+1)-th
        best) still strong enough to support h = i+1?". If citations[i] >= i+1,
        it qualifies and we keep going. The FIRST i where i+1 > citations[i]
        is the point where the (i+1)-th paper is too weak -> the answer is i
        (the count of papers that DID qualify before this one failed).

        Despite the name, Python's list.sort() is Timsort (a stable hybrid of
        mergesort + insertion sort, O(n log n) worst/avg, O(n) best on already-
        sorted runs) — NOT quicksort. Its C implementation has a very low
        constant factor, so it beats the O(n) bucket version in practice for
        all but the largest inputs (see hindex_bucketsort_linear benchmark).
        """
        # Sort descending so position i holds the (i+1)-th most-cited paper.
        # Mutates the input list in place (caller passes a copy if needed).
        citations.sort(reverse=True)

        # Edge case: a single paper with 0 citations -> h-index 0.
        # (Without this guard, the loop below would return 0 anyway via the
        # i+1 > citations[i] check, so this is arguably redundant — kept for
        # clarity / early exit.)
        if len(citations) == 1 and citations[0] == 0:
            return 0

        # Walk top-down. i is 0-indexed, so h = i+1 papers considered so far.
        # The first i where the (i+1)-th paper's count is below i+1 means paper
        # i+1 can't be part of an h=i+1 set -> h-index is i (papers 0..i-1
        # qualified, i.e. i papers each with >= i citations).
        for i in range(len(citations)):
            if i + 1 > citations[i]:
                return i
        # Every paper qualified: h-index equals the total number of papers.
        return len(citations)

    def hindex_bucketsort_linear(self, citations: List[int]) -> int:
        """
        Canonical O(n) h-index via counting sort with n+1 buckets.

        Two key improvements over hindex_bucketsort:

        1. CAP AT n: use n+1 buckets indexed 0..n. Any citation count >= n
           goes into bucket n (you can never have an h-index > n, so a count
           of n and a count of 1,000,000 are equivalent for this problem).
           This makes memory O(n) regardless of how large citation values get
           — no more million-element bucket array when one paper has a huge
           citation count.

        2. DON'T RECONSTRUCT THE ARRAY: the old version rebuilt a sorted copy
           of `citations` from the buckets, then re-ran the same scan as the
           sort-based solution. That reconstruction is pure overhead. Instead,
           walk the buckets high -> low, accumulating how many papers we've
           seen. The h-index is the largest k where we've seen >= k papers with
           at least k citations each — i.e. the loop directly answers the
           question without ever producing a sorted array.

        Result: O(n) time, O(n) space, one pass to fill + one pass to scan.
        Beats Timsort's O(n log n) in theory; in practice it can also win
        because it avoids the comparison sort entirely.
        """
        n = len(citations)
        buckets = [0] * (n + 1)  # indices 0..n; bucket n = ">= n"
        for c in citations:
            buckets[min(c, n)] += 1

        # Walk high -> low, accumulating papers with >= k citations.
        # h-index = largest k such that at least k papers have >= k citations.
        papers = 0
        for k in range(n, -1, -1):
            papers += buckets[k]  # all papers in bucket k have >= k citations
            if papers >= k:
                return k
        return 0

    def hindex_bucketsort(self, citations: List[int]) -> int:
        max_c = max(citations)
        buckets = [0] * (max_c + 1)
        for i in citations:
            buckets[i] += 1

        j = len(buckets) - 1
        ptr = 0
        while j >= 0:
            if buckets[j] > 0:
                citations[ptr] = j
                ptr += 1
                buckets[j] -= 1

            if buckets[j] == 0:
                j -= 1

        print(citations)

        if len(citations) == 1 and citations[0] == 0:
            return 0
        for i in range(len(citations)):
            if i + 1 > citations[i]:
                return i
        return len(citations)


# citations = [1, 2, 2]
# solution = Solution()
# print(solution.hindex_bucketsort_insertionsort(citations))

citations = [3, 0, 6, 1, 5]
solution = Solution()
print(solution.hIndex(citations))

citations = [1, 3, 1]
solution = Solution()
print(solution.hIndex(citations))

citations = [0, 1]
solution = Solution()
print(solution.hIndex(citations))

citations = [1, 2, 2]
solution = Solution()
print(solution.hIndex(citations))
