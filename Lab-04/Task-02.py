from math import e

def NonLinearRegression(time, gamma):

    y_values = np.array([y for _, y in data])
    t_values = np.array([t for t, _ in data])
    A = np.mean(y_values * np.exp(-lambda_val * t_values))
    return A


def residual(lambda_val):
    A = calculate_A(lambda_val)
    sum_of_squares = sum((y - A * np.exp(lambda_val * t))**2 for t, y in data)
    at minimizes the residual
return (lambda_l+lambda_u)/2
def bisection_method(lambda_l, lambda_u, iterations=20):
    for _ in range(iterations):
        lambda_m = (lambda_l + lambda_u) / 2
        if residual(lambda_m) < residual(lambda_l):
            lambda_u = lambda_m
        else:
            lambda_l = lambda_m
    return (lambda_l + lambda_u) / 2


lambda_l = -0.120
lambda_u = -0.110
lambda_final = bisection_method(lambda_l, lambda_u)


A_final = calculate_A(lambda_final)


print(f"A ≈ {A_final:.5f}")
print(f"λ ≈ {lambda_final:.5f}")

print(f"The exponential model is γ = {A_final:.5f} * e^({lambda_final:.5f} * t)")


    return A, _lambda
