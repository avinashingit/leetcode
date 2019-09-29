class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        seen.add(n)
        num = n
        while num != 1:
            temp = 0
            while num:
                digit = num%10
                temp += digit**2
                num //= 10
            if temp in seen:
                return False
            seen.add(temp)
            num = temp
        return True
        
