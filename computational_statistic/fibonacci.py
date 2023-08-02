from utils import measure_time
import sys

def fibonacci_recursive(number=0):
    if number in (0, 1):
        return 1

    return fibonacci_recursive(number-1) + fibonacci_recursive(number-2)

def fibonacci_memo(number=0, memo={}):
    if number in (0, 1):
        return 1
     
    try:
        return memo[number]
    except KeyError:

        result = fibonacci_memo(number-1, memo) + fibonacci_memo(number-2, memo)
        memo[number] = result
        return result


if __name__ == "__main__":
    sys.setrecursionlimit(int(1002))
    target = 40
    condition = target <= 30
    if condition: # O(2**n)
        print(f"Recursive: {fibonacci_recursive(target)}")
    print(f"Memo: {fibonacci_memo(target)}")

