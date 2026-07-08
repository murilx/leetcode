"""
14. Longest Common Prefix
Difficulty: Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ceiling = len(min(strs, key=len))
        prefix = ""

        if ceiling == 0:
            return ""

        for i in range(ceiling):
            prefix += strs[0][i]
            for s in strs:
                if s[i] != prefix[i]:
                    return prefix[:i]

        return prefix
