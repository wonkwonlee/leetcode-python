"""
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.

Result: 48 ms
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Empty string is 0
        if not s:
            return 0

        sub = s[0]
        result = 1
        for i in range(1, len(s)):
            # Check if current char is a duplicate
            if s[i] in sub:
                # Reset substring and only store chars after duplicate
                sub = sub[sub.index(s[i]) + 1:] + s[i]
                continue
            # Add new char to substring and update max value
            else:
                sub = sub + s[i]
                result = max(len(sub), result)

        return result
