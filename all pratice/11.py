#509. Fibonacci Number
class Solution:
    def fib(self, n: int) -> int:
        fib=self.fib
        if n==0:
            return 0
        elif n==1:
            return 1
        return fib(n-1) + fib(n-2)
#递归，递：分解为最小条件，向下递；归：从底部向上返回结果