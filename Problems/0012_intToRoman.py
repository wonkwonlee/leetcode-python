"""
12. Integer to Roman
Given an integer, convert it to a roman numeral.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Result: 40 ms
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""

        while num:
            if num >= 1000:
                count = num // 1000
                result = result + 'M' * count
                num -= count * 1000
            elif num >= 900:
                result = result + 'CM'
                num -= 900
            elif num >= 500:
                result = result + 'D'
                num -= 500
            elif num >= 400:
                result = result + 'CD'
                num -= 400
            elif num >= 100:
                count = num // 100
                result = result + 'C' * count
                num -= count * 100
            elif num >= 90:
                result = result + 'XC'
                num -= 90
            elif num >= 50:
                result = result + 'L'
                num -= 50
            elif num >= 40:
                result = result + 'XL'
                num -= 40
            elif num >= 10:
                count = num // 10
                result = result + 'X' * count
                num -= count * 10
            elif num >= 9:
                result = result + 'IX'
                num -= 9
            elif num >= 5:
                result = result + 'V'
                num -= 5
            elif num >= 4:
                result = result + 'IV'
                num -= 4
            else:
                count = num // 1
                result = result + 'I' * count
                num -= count

        return result


    # Example
    def intToRoman1(self, num):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        result, i = "", 0
        while num:
            result += (num//values[i]) * numerals[i]
            num %= values[i]
            i += 1
        return result
