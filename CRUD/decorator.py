def decorator_with_args(*args, **kwargs):
    print("As decorator I received these arguments")
    print(" ", args, kwargs)

    def outer(func):
        print(f"As outer I received this func name: \"{func.__name__}\"")
        def wrapper(*args, **kwargs):
            print(f"As wrapper I received these arguments")
            print(" ",args, kwargs)
            print(f"Now executing received function with parameters")
            output = func(*args, **kwargs)
            print(f"Returning ouput")

            return output
        return wrapper
    return outer

@decorator_with_args(1,2,3, a=1, b=2, c=3)
def test_function(name, age=3):
    return f"{name} with age {age}"

if __name__ == "__main__":
    print(" ",test_function("Danny", age=27))