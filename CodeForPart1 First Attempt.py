import random


# Function definition
def true_percentage_of_time(percentage):
    x = random.randrange(0, 101)

    if x <= percentage:
        return True


# Driver function
NumberOfTimesUnreliable = 0
NumberOfTimesToRunOuterLoop = 100
NumberOfTimesOuterLoopRan = 0
AverageAccuracy = 0
for runs in range(1, NumberOfTimesToRunOuterLoop + 1):
    NumberOfTimesTrue = 0
    NumberOfIterations = 100000
    NumberOfTimesOuterLoopRan += 1
    for i in range(0, NumberOfIterations):
        if true_percentage_of_time(70):
            NumberOfTimesTrue += 1

    Accuracy = NumberOfTimesTrue / NumberOfIterations * 100
    AverageAccuracy += Accuracy
    # print(str(NumberOfTimesTrue) + " times true was returned")
    # print(str(NumberOfIterations) + " times function was called")
    # print(str(Accuracy) + " percentage of the time true was returned")
    # print("---------------------------------------------------")
    if Accuracy < 69.9 or Accuracy > 70.1:
        # print("---------------------------------------------------")
        # print(str(NumberOfTimesTrue) + " times true was returned")
        # print(str(NumberOfIterations) + " times function was called")
        # print(str(Accuracy) + " percentage of the time true was returned")
        # print('Unreliable')
        NumberOfTimesUnreliable += 1
        # print("---------------------------------------------------")
        continue
    else:
        break

    # Code to keep us updated while program is running
    # if runs % 50 == 0:
    #     print(str(runs) + ' runs and ' + str(NumberOfTimesUnreliable) + ' unreliable so far')


# Final result update
print('Final total Runs of outer loop = ' + str(NumberOfTimesToRunOuterLoop))
print('Final total number of times unreliable = ' + str(NumberOfTimesUnreliable))
# print('The average of the accuracy = ' + str(AverageAccuracy / NumberOfTimesOuterLoopRan))
print('Number of times outer loop ran = ' + str(NumberOfTimesOuterLoopRan))
