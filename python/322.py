class Solution:

    def check(self, coins, remaining, counts):
        if remaining < 0:
            return -1
        if counts[remaining] is not None:
            return counts[remaining]
        min_val = float('inf')
        for coin in coins:
            value = self.check(coins, remaining-coin, counts)
            if value != -1 and value < min_val:
                min_val = value + 1
        counts[remaining] = min_val if min_val != float('inf') else -1
        return counts[remaining]

    def coinChange(self, coins: List[int], amount: int) -> int:
        counts = [None] * (amount+1)
        counts[0] = 0
        return self.check(coins, amount, counts)
