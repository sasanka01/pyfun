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
    print arr
    return arr
arr = [2,4,10,16]
num = 5
b = multiply(arr,num)
b
