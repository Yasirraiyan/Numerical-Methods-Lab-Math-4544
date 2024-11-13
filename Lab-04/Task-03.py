def predict(A,_lambda,t):
    import numpy as np

data = [(0, 1), (1, 0.891), (3, 0.708), (5, 0.562), (7, 0.447), (9, 0.355)]da
def calculate_A(lambda_val):
    y_values = np.array([y for _, y in data])
    t_values = np.array([t for t, _ in data])
    A = np.mean(y_values * np.exp(-lambda_val * t_values))
    return A


def residual(lambda_val):
    A = calculate_A(lambda_val)
    sum_of_squares = sum((y - A * np.exp(lambda_val * t))**2 for t, y in data)
    return sum_of_squares

def bisection_method(lambda_l, lambda_u, iterations=20):
    for _ in range(iterations):
        lambda_m = (lambda_l + lambda_u) / 2
        if residual(lambda_m) < residual(lambda_l):
            lambda_u = lambda_m
        else:
            lambda_l = lambda_m
    return (lambda_l + lambda_u) / 2

def find_parameters():
    lambda_l = -0.120
    lambda_u = -0.110
    lambda_final = bisection_method(lambda_l, lambda_u)
    A_final = calculate_A(lambda_final)
    return A_final, lambda_final

def predict_gamma(t, A, lambda_val):
    return A * np.exp(lambda_val * t)


A, lambda_val = find_parameters()

# Display results
print(f"A ≈ {A:.5f}")
print(f"λ ≈ {lambda_val:.5f}")
rary t
t = 4
gamma_prediction = predict_gamma(t, A, lambda_val)
print(f"γ({t}) ≈ {gamma_prediction:.5f}")


print(f"The exponential model is γ = {A:.5f} * e^({lambda_val:.5f} * t)")
    return res
