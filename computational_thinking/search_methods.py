import random
from utils import gen_data, measure_time

@measure_time
def lineal_search(data, target):
    steps = 0
    flag = False
    for item in data:
        steps += 1
        if item == target:
            flag = True
            break
    print(f"Lineal Search: Taken {steps} steps!")
    return flag


@measure_time
def binary_search(data, target):
    low = 0
    high = len(data)
    middle = (low + high) // 2
    steps = 0
    while True:
        steps += 1

        if low == middle:
            flag = False
            break
        
        if data[middle] < target:
            low = middle
        elif data[middle] > target:
            high = middle
        else:
            flag = True
            break
        
        middle = (low + high) // 2
    print(f"Binary Search: Taken {steps} steps!")
    
    return flag

if __name__ == "__main__":
    lenght = 1000
    target = random.randint(0, 1000)
    data = gen_data(lenght)
    result = binary_search(sorted(data), target)   
    print(f"{result}: {target} {'is in' if result else 'isnt in'} data") 
    result = lineal_search(data, target)   
    print(f"{result}: {target} {'is in' if result else 'isnt in'} data") 