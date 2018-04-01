import random


# Function definition
def true_percentage_of_time(percentage):
    x = random.randrange(0, 101)

    if x <= percentage:
        return True


# Driver function
NumberOfTimesUnreliable = 0
NumberOfTimesToRunOuterLoop = 50

for runs in range(1, NumberOfTimesToRunOuterLoop):
    NumberOfTimesTrue = 0
    NumberOfIterations = 100
    for i in range(0, NumberOfIterations):
        if true_percentage_of_time(70):
            NumberOfTimesTrue += 1

    accuracy = NumberOfTimesTrue / NumberOfIterations * 100
    # print(str(NumberOfTimesTrue) + " times true was returned")
    # print(str(NumberOfIterations) + " times function was called")
    # print(str(accuracy) + " percentage of the time true was returned")
    # print("---------------------------------------------------")
    if accuracy < 69.9 or accuracy > 70.1:
        print("---------------------------------------------------")
        print(str(NumberOfTimesTrue) + " times true was returned")
        print(str(NumberOfIterations) + " times function was called")
        print(str(accuracy) + " percentage of the time true was returned")
        print('Unreliable')
        NumberOfTimesUnreliable += 1
        print("---------------------------------------------------")

    # Code to keep us updated while program is running
    if runs % 50 == 0:
        print(str(runs) + ' runs and ' + str(NumberOfTimesUnreliable) + ' unreliable so far')

# Final result update
print('Final total Runs of outer loop = ' + str(NumberOfTimesToRunOuterLoop))
print('Final total number of times unreliable = ' + str(NumberOfTimesUnreliable))
