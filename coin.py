# Assignment: Coin Tosses
# Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
#
# Sample output should be like the following:
#
# Starting the program...
# Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
# Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far
# Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far
# Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
# ...
# Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far
# Ending the program, thank you!
# Hint: Use the python built-in round function to convert that floating point number into an integer
#
# x = .23945593
# y = .798839238
# x_rounded = round(x)
# # x_rounded will be rounded down to 0
# y_rounded = round(y)
# # y_rounded will be rounded up to 1
import random

def coinToss():
    heads = 0
    tails = 0
    for i in range (1,5001):
        random_num = random.randint(0,1)
        if random_num == 0:
            heads = heads + 1
            print "Attempt #{}: Throwing a coin .... it's a head! .... got {} head(s) so far and {} tail(s) so far".format(i,heads,tails)
        else:
            tails = tails + 1
            print "Attempt #{}: Throwing a coin .... it's a tail! ... got {} heads(s) so far and {} tail(s) so far ".format(i,heads,tails)

coinToss()
