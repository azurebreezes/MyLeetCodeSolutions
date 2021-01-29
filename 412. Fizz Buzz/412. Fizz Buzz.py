class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        for i in range(1, n+1):
            if i % 15 == 0:
                yield "FizzBuzz"
            elif i % 5 == 0:
                yield "Buzz"
            elif i % 3 == 0:
                yield "Fizz"
            else:
                yield str(i)