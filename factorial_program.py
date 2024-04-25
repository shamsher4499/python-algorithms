def factorial(n):
    result = 1
    for i in range(1, n + 1):
        print(f"i: {i}")
        result *= i
        print(f"result: {result}")
    print(f"Factorial of {n} is {result}")


factorial(4)