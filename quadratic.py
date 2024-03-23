import math

def quadratic_solver(a, b, c):
    x = (b**2) - (4 * a * c)
    if x >= 0:
        y = math.sqrt(x)
        result_1 = (-b + y) / (2 * a)
        result_2 = (-b - y) / (2 * a)
    else:
        x = -x
        y = math.sqrt(x)
        result_1 = f"{-b / (2 * a)} + {y / (2 * a)}i"
        result_2 = f"{-b / (2 * a)} - {y / (2 * a)}i"
    
    return result_1, result_2

a = float(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

result_1, result_2 = quadratic_solver(a, b, c)
print(f"The outputs are x1= {result_1} and x2={result_2}")