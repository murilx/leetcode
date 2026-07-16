"""
3867. Sum of GCD of Formed Pairs
Difficulty: Medium

You are given an integer array nums of length n.

Construct an array prefixGcd where for each index i:

    Let mxi = max(nums[0], nums[1], ..., nums[i]).
    prefixGcd[i] = gcd(nums[i], mxi).

After constructing prefixGcd:

    Sort prefixGcd in non-decreasing order.
    Form pairs by taking the smallest unpaired element and the largest unpaired element.
    Repeat this process until no more pairs can be formed.
    For each formed pair, compute the gcd of the two elements.
    If n is odd, the middle element in the prefixGcd array remains unpaired and should be ignored.

Return an integer denoting the sum of the GCD values of all formed pairs.
The term gcd(a, b) denotes the greatest common divisor of a and b
"""


class Solution:
    # Euclid's algorithm implementation for GCD
    def gcd(self, a: int, b: int) -> int:
        while b != 0:
            t = b
            b = a % b
            a = t
        return a

    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []
        mx = nums[0]

        # Populate prefixGcd
        for i in range(len(nums)):
            mx = max(mx, nums[i])
            prefixGcd.append(self.gcd(nums[i], mx))

        # Calculate final answer
        prefixGcd.sort()
        answer = 0
        upperBound = len(prefixGcd) - 1
        for i in range(len(prefixGcd) // 2):
            answer += self.gcd(prefixGcd[i], prefixGcd[upperBound - i])

        return answer
