"""
20. Valid Parentheses
Difficulty: Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        for i in range(len(s)):
            if s[i] in pairs.values():
                stack.append(s[i])
                continue

            if len(stack) == 0 or stack.pop() != pairs[s[i]]:
                return False

        return len(stack) == 0
