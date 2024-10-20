#Now, write a function for evaluating the acceleration at  t=16

import numpy as np

# Known data points (time t, and corresponding velocity v)
t_values = np.array([10, 15, 20])
v_values = np.array([100.0, 362.78, 200.0])

def interpolate_acceleration(t_new, t_values, v_values, n):


    if n == 0:
        nearest_idx = np.abs(t_values - t_new).argmin()
        v_nearest = v_values[nearest_idx]
        return f"Cannot calculate acceleration for n=0 with a single point."


    elif n == 1:
        indices = np.argsort(np.abs(t_values - t_new))[:2]
        t_nearest = t_values[indices]
        v_nearest = v_values[indices]


        delta_v = v_nearest[1] - v_nearest[0]
        delta_t = t_nearest[1] - t_nearest[0]
        a_new = delta_v / delta_t
        return a_new


    elif n == 2:
        indices = np.argsort(np.abs(t_values - t_new))[:3]
        t_nearest = t_values[indices]
        v_nearest = v_values[indices]


        coeffs = np.polyfit(t_nearest, v_nearest, 2)


        a_new = 2 * coeffs[0] * t_new + coeffs[1]
        return a_new

    else:
        raise ValueError("Unsupported interpolation degree")


t_new = 16


n = 1
acceleration_n1 = interpolate_acceleration(t_new, t_values, v_values, n)
print(f"Linear interpolation (n=1), acceleration at t={t_new}: {acceleration_n1:.2f}")


n = 2
acceleration_n2 = interpolate_acceleration(t_new, t_values, v_values, n)
print(f"Quadratic interpolation (n=2), acceleration at t={t_new}: {acceleration_n2:.2f}")

