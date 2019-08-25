class Solution:
    def fib(self, N: int) -> int:
        fibs = [0]*(N+1)
        for i in range(1, N+1):
            if i == 1:
                fibs[i] = 1
            else:
                fibs[i] = fibs[i-1] + fibs[i-2]
        return fibs[N]
