# all imports here
import math

# read input from file
def read_file(filename):
    file = open(filename, "r")
    file_data = file.read()
    file.close()
    return file_data

# sort the given data
def sorting(data):
    return data.sort()

# This function expects a sorted input list
def smallest_number(input):
    # Smallest Number
    return input[0] 

# This function expects a sorted input list
def greatest_num(input):
    # greater num
    return input[-1]

# This function expects a string list and converts it to int list
def convert_list_to_int(string_list):
    # to convert string list into int list
    for i in range(0, len(string_list)):
        string_list[i] = int(string_list[i])
    return string_list

def calculate_mean(data):
    # find mean
    Sum = sum(data)
    xbar = Sum/len(data)
    return str(xbar)

def calculate_variance(data, mean):
    # find variance
    Var = sum((x - mean) ** 2 for x in data) / len(data)
    return str(Var)

def calculate_std_dev(variance):
    # find standard deviation
    std_dev = math.sqrt(variance)
    return std_dev

# This function prints data along with message
def print_data(message, data):
    print(message+data)

if __name__ == '__main__':
    project_file = read_file("/Users/ms2051/Desktop/input.txt")
    # tokenize, split
    input = project_file.split()
    input = sorting(input)

    # Calculate smallest and greatest numbers and print it
    print_data("The smallest number is ", smallest_number(input))
    print_data("The greatest number is ", greatest_num(input))

    input = convert_list_to_int(input)

    # Calculate mean and print it
    mean = calculate_mean(input)
    print_data("Mean is ", calculate_mean(mean))

    # calculate variance and print it
    variance = calculate_variance(input, mean)
    print_data("Variance is ", variance)

    # Caluclate standard deviation and print it
    print_data("Standard Deviation is ", calculate_std_dev(variance))
