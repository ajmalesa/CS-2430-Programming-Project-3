# import random
import numpy


def my_rand(mean, deviation):
    x = numpy.random.normal(mean, deviation, 2500)
    # if 70.5 <= x >= 69.5:
    #     return True
    print(numpy.mean(x))
    print(abs(deviation - numpy.std(x, ddof=1)))


print(my_rand(70, 2))


# My slightly modified version of the built in random.gauss function
# def my_gauss_function(mean, deviation):
#     x = random.gauss(mean, deviation)
#     if (x <= 70.5) and (x >= 69.5):
#         return True
#     else:
#         return False


# Function driver
# Nus

# Display results
# print("Returned true: " + str(NumberOfTimesReturnedTrue) + " times")
# print("Returned False: " + str(NumberOfTimesReturnedFalse) + " times")
# print(str((NumberOfTimesReturnedTrue / NumberOfTimesToRunOuterLoop) * 100) + " percent")
