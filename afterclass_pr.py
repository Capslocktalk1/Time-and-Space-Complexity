def multiply_one_iteration(a, b):
    return a * b

def multiply_n_iterations(a, b, n):
    result = 0
    for _ in range(n):
        result += a
    return result


a = int(input("Enter 'a': "))
b = int(input("Enter 'b': "))
n = int(input("enter number of iterations for N: "))

result_one = multiply_one_iteration(a, b)
print("result using 1 iteration:", result_one)

result_n = multiply_n_iterations(a, b, n)
print("Result using", n, "iterations:", result_n)
