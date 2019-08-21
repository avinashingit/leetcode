class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        str_sum = ""
        l, m = len(num1) - 1, len(num2) - 1
        carry = 0
        while l >= 0 and m >= 0:
            total = ord(num1[l]) - 48 + ord(num2[m]) - 48
            total += carry
            digit = total % 10
            carry = total//10
            str_sum = str(digit) + str_sum
            l -= 1
            m -= 1

        if l != -1:
            for i in range(l, -1, -1):
                total = carry + ord(num1[i]) - 48
                digit = total % 10
                carry = total // 10
                str_sum = str(digit) + str_sum
        if m != -1:
            for i in range(m, -1, -1):
                total = carry + ord(num2[i]) - 48
                digit = total % 10
                carry = total // 10
                str_sum = str(digit) + str_sum
        if carry != 0:
            str_sum = str(carry) + str_sum
        return str_sum
