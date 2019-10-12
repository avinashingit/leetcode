class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x%10 == 0 and x!=0):
            return False
        pal = 0
        while x > pal:
            digit = x%10
            pal = pal*10 + digit
            x //= 10
        return x == pal or x == pal//10
