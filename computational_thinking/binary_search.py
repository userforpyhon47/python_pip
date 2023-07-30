from utils import measure_time


@measure_time
def exaustive_search(target: float=0) -> float:
    steps = 0
    answer = None
    for index in range(int(target)//2):
        steps += 1
        if index**2 == target:
            answer = index
            break
    print(f"Exaustive Search: taken {steps} steps")
    print(f" Exact square root of {target} is {answer}")
    return answer


@measure_time
def binary_search(target: float=0) -> float:
    steps = 0
    low = 0
    high = target
    answer = (low + high) // 2

    while abs(answer ** 2 - target) != 0:
        steps += 1
        if low == answer:
            answer = None
            break

        if answer ** 2 < target:
            low = answer
        else:
            high = answer
        
        answer = (low + high) // 2
        
    print(f"Binary Search: taken {steps} steps!")
    print(f" Exact square root of {target} is {answer}")
    return answer

@measure_time
def aprox_sqr_search(target: float = 0) -> float:
    """Funtcion to serch the aprox sqr of a given number by target"""
    low = 0
    high = target
    epsilon = 0.01
    answer = (low + high) / 2
    steps = 0
    
    while abs(answer**2 - target) > epsilon:
        steps += 1
        if answer**2 < target:
            low = answer
        else:
            high = answer
        
        answer = (low + high) / 2
        
    print(f"Approx search: taken {steps} steps")
    print(f" Approx square root of {target} is {answer}")

    return answer

if __name__ == "__main__":
    target = 256
    condition_1 = target < 1e8
    condition_2 = target < 1e15
    if condition_1:
        result_exhaustive = exaustive_search(target)
    result_binary = binary_search(target)
    if condition_2:
        result_approx = aprox_sqr_search(target)
