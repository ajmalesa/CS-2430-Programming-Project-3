import random


def my_rand_funct(percentage):
    if random.randrange(1, 101) <= percentage:
        return True


# NumberOfTimesToRunOuterLoop = 500000
# NumberOfTimesReturnedTrue = 0
# for i in range(NumberOfTimesToRunOuterLoop):
#     if my_rand_funct(70) and my_rand_funct(40):
#         NumberOfTimesReturnedTrue += 1
#
# print('Percentage of times returned true: ' + str(NumberOfTimesReturnedTrue / NumberOfTimesToRunOuterLoop * 100))


NumberOfTimesToRunOuterLoop = 700000
NumberOfTimesReturnedTrue = 0
for i in range(NumberOfTimesToRunOuterLoop):
    if my_rand_funct(70) or my_rand_funct(40):
        NumberOfTimesReturnedTrue += 1

print('Percentage of times returned true: ' + str(NumberOfTimesReturnedTrue / NumberOfTimesToRunOuterLoop * 100))
