class Solution:

    def getDigitSquareSum(self, num):
        total = 0
        while num != 0:
            digit = num % 10
            num = num//10
            total += digit**2
        return total

    def isHappy(self, n: int) -> bool:
        seen = set()
        num = n
        while num not in seen:
            seen.add(num)
            num = self.getDigitSquareSum(num)
            if num == 1:
                return True
        return False
