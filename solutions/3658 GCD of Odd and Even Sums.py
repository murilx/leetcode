"""
3658. GCD of Odd and Even Sums
Difficulty: Easy

You are given an integer n. Your task is to compute the GCD (greatest common divisor) of two values:

    sumOdd: the sum of the smallest n positive odd numbers.

    sumEven: the sum of the smallest n positive even numbers.

Return the GCD of sumOdd and sumEven.
"""


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumEven = 0
        sumOdd = 0

        for i in range(1, n + 1):
            sumEven += 2 * i
            sumOdd += 2 * i - 1

        # Euclid's algorithm for GCD
        a, b = sumOdd, sumEven
        while b != 0:
            t = b
            b = a % b
            a = t

        return a
