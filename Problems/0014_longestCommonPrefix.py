"""
14. Longest Common Prefix
Find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

# Example
Input: ["flower","flow","flight"]
Output: "fl"

Input: ["dog","racecar","car"]
Ouput: ""

Result:
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        if len(strs) == 1:
            return strs[0]

        strs.sort(key=lambda x: len(x))

        # Compare the first two strings
        common = ""
        index = 0
        for char in strs[0]:
            if char == strs[1][index]:
                common = common + char
                index += 1
            else:
                break

        count = 0
        for i in range(2, len(strs)):
            if common != strs[i][0:len(common)]:
                if common == "":
                    return ""
                common = common[0:-1]

        return common












