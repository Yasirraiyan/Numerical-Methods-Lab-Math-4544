def evaluate_polynomial(coefficients, x):
    result = 0
    degree = len(coefficients) - 1
    for i, coeff in enumerate(coefficients):
        result += coeff * (x ** (degree - i))
    return result

def bisection_method(coefficients, a, b, tol):
    if evaluate_polynomial(coefficients, a) * evaluate_polynomial(coefficients, b) >= 0:
        print("Bisection Method Fails")
        return None
    
    mid = (a + b) / 2

    while (b - a) / 2 > tol:
        mid = (a + b) / 2
        poly_mid = evaluate_polynomial(coefficients, mid)

        if poly_mid == 0:
            return mid  
        elif evaluate_polynomial(coefficients, a) * poly_mid < 0:
            b = mid
        else:
            a = mid
    
    return (a + b) / 2

coefficients = [1, -2, 0, 4]
a = -3
b = 3
tolerance = 1e-6
root = bisection_method(coefficients, a, b, tolerance)

if root is not None:
    print(f"Root found at: {root}")
else:
    print("No root found within the given interval.")
