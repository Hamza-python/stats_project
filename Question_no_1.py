import math
file = open("/Users/ms2051/Desktop/input.txt", "r")
project_file = file.read()
file.close()
input = project_file.split()
input.sort()

# Smallest Number
print(input[0] + " is the smallest number")

# greater num
print(input[-1] + " is the greater number")

# to convert string list into int list
for i in range(0, len(input)):
    input[i] = int(input[i])

# find mean
Sum = sum(input)
xbar = Sum/len(input)
# printing result
print("Mean = " + str(xbar))

# find variance
Var = sum((x - xbar) ** 2 for x in input) / len(input)
# printing result
print("Variance = " + str(Var))

# find standard deviation
stan_dev = math.sqrt(Var)
print("Standard Dviation = " + str(stan_dev))