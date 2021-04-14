"""
14. Longest Common Prefix
Find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

# Example
Input: ["flower","flow","flight"]
Output: "fl"

Input: ["dog","racecar","car"]
Output: ""

Result: 20 ms
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]

        # Sort strings by length
        strs.sort(key=lambda x: len(x))

        # Compare the first two strings
        common = ""
        index = 0
        for char in strs[0]:
            # Store char if the char is in the both strings
            if char == strs[1][index]:
                common += char
                index += 1
            else:
                break

        # Compare current common prefix with other string in the list
        for i in range(2, len(strs)):
            # Only compare the length of common prefix
            while common != strs[i][0:len(common)]:
                # If current common prefix is empty, return it
                if common == "":
                    return ""
                # Reduce common prefix from the end
                common = common[0:-1]

        return common
