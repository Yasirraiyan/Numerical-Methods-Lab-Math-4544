#Design a utility function that will be called in the DirectInterpolation function. The purpose of this function will be to find the  n+1  closest points to the unknown value  tnew  where we want to interpolate the data, where  n  is the order of the interpolating polynomial. Understand that the nearest points should be selected such that they bracket the  tnew . The function to be implemented is as follows://
#For n = 0 and t_new = 16
#t_nearest: [15]
#v_nearest: [362.78]
#n = 0, t_new = 16:
#t_nearest: [15]
#v_nearest: [362.78]

#n = 1, t_new = 16:
#t_nearest: [15, 20]
#v_nearest: [362.78, 200.0]

#n = 2, t_new = 16:
#t_nearest: [10, 15, 20]
#v_nearest: [100.0, 362.78, 200.0]

import numpy as np

import numpy as np

def NearestPoints(t, v, n, t_new):
    t = np.array(t)
    v = np.array(v)

    # Ensure t is sorted along with v
    sorted_indices = np.argsort(t)
    t = t[sorted_indices]
    v = v[sorted_indices]

    # If t_new is outside the range of t, pick the first or last n+1 points
    if t_new <= t[0]:
        indices = np.arange(n + 1)
    elif t_new >= t[-1]:
        indices = np.arange(len(t) - n - 1, len(t))
    else:
        # Find the index where t_new would be inserted to keep t sorted
        idx = np.searchsorted(t, t_new)
        left = idx - 1
        right = idx

        indices = []

        # Collect n+1 nearest points while ensuring they bracket t_new
        while len(indices) < n + 1:
            if left >= 0 and right < len(t):
                # Choose the closer point between left and right
                if t_new - t[left] <= t[right] - t_new:
                    indices.append(left)
                    left -= 1
                else:
                    indices.append(right)
                    right += 1
            elif left >= 0:
                indices.append(left)
                left -= 1
            elif right < len(t):
                indices.append(right)
                right += 1
            else:
                break

    # Get t_nearest and v_nearest
    indices = sorted(indices)
    t_nearest = t[indices].tolist()
    v_nearest = v[indices].tolist()

    return t_nearest, v_nearest

# Sample data for testing
t = [10, 15, 20, 25, 30]
v = [100, 362.78, 200, 150, 120]

# Test for n = 0
n = 0
t_new = 16
t_nearest, v_nearest = NearestPoints(t, v, n, t_new)
print("For n =", n, "and t_new =", t_new)
print("t_nearest:", t_nearest)
print("v_nearest:", v_nearest)


# Test cases
t = [10, 15, 20, 25, 30]
v = [100, 362.78, 200, 150, 120]

# Test for n = 0
n = 0
t_new = 16
t_nearest, v_nearest = NearestPoints(t, v, n, t_new)
print(f"n = {n}, t_new = {t_new}:")
print("t_nearest:", t_nearest)
print("v_nearest:", v_nearest)

# Test for n = 1
n = 1
t_new = 16
t_nearest, v_nearest = NearestPoints(t, v, n, t_new)
print(f"\nn = {n}, t_new = {t_new}:")
print("t_nearest:", t_nearest)
print("v_nearest:", v_nearest)

# Test for n = 2
n = 2
t_new = 16
t_nearest, v_nearest = NearestPoints(t, v, n, t_new)
print(f"\nn = {n}, t_new = {t_new}:")
print("t_nearest:", t_nearest)
print("v_nearest:", v_nearest)
