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
