# Assignment: Fun with Functions
# Create a series of functions based on the below descriptions.
#
# Odd/Even:
# Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.
#
# Your program output should look like below:
#
# Number is 1.  This is an odd number.
# Number is 2.  This is an even number.
# Number is 3.  This is an odd number.
# ...
# Number is 2000.  This is an even number.
# Copy
# Multiply:
# Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.
#
# The function should multiply each value in the list by the second argument. For example, let's say:
#
# a = [2,4,10,16]
# Copy
# Then:
#
# b = multiply(a, 5)
# print b
# Copy
# Should print [10, 20, 50, 80 ].
#
# Hacker Challenge:
# Write a function that takes the multiply function call as an argument. Your new function should return the multiplied list as a two-dimensional list. Each internal list should contain the 1's times the number in the original list. Here's an example:
#
# def layered_multiples(arr):
#   # your code here
#   return new_array
# x = layered_multiples(multiply([2,4,5],3))
# print x
# # output
# >>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

def odd_even():
    for i in range (1,2001):
        if (i%2==1):
            print "Number is {0}. This is an odd number.".format(i)
        else:
            print "Number is {0}. This is an even number.".format(i)

# print odd_even()


def multiply(arr,num):
    # print arr, num
    for i in range (0,len(arr)):
        arr[i] = arr[i] * num
    # print arr
    return arr
arr = [2,4,10,16]
num = 5
b = multiply(arr,num)
# b

def layered_multiples(arr):
    new_array = []
    for x in arr:
        new_array1 = []
        for i in range (0,x):
            new_array1.append(1)
        new_array.append(new_array1)
    return new_array
x = layered_multiples(multiply([2,4,5],3)) #is equal to arr = [6,12,15]
print x
