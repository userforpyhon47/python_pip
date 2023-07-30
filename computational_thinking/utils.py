import random
import time

def measure_time(func):
    def wrapper(*args):
        tic = time.time()
        result = func(*args)
        toc = time.time()
        print(f" └->Elapsed time: {toc-tic}")
        return result
    return wrapper

def gen_data(lenght=0, lower_limit=0, upper_limit=1000) -> list:
    """Function to generate a random integer list between lower and upper limits of lenght 'length'"""
    return [random.randint(lower_limit, upper_limit) for x in range(lenght)]