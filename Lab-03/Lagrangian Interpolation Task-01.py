#t = [0, 10, 15, 20, 22.5, 30]
#v = [0, 227.04, 362.78, 517.35, 602.97, 901.67]
#If you can implement the  O(nlog2n)  algorithm, then you'll receive a lot of bonus marks.
Codeforces blog on optimizing Lagrangian Interpolation: 
#Task 1
Design a utility function that will be called in the Lagrangian function. The purpose of this function will be to find the  n+1  closest points to the unknown value  tnew  that also bracket the  tnew  value. Here,  tnew  is where we want to interpolate the data, where  n  is the order of the interpolating polynomial. Understand that the nearest points should be selected such that they bracket the  tnew .

#Note: Make sure your nearest points also bracket the  tnew  point.

#The function to be implemented is as follows:

  def NearestPoints(t, v, n, t_new):

  points = sorted(zip(t, v), key=lambda p: abs(p[0] - t_new))
  t_nearest, v_nearest = [],[]


  for p in points:
        t_nearest.append(p[0])
        v_nearest.append(p[1])
        if len(t_nearest) > n + 1:
            break


  t_nearest, v_nearest = zip(*sorted(zip(t_nearest, v_nearest)))

  return list(t_nearest), list(v_nearest)


  return t_nearest, v_nearest
