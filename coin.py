import random
random_num = random.randint(0,1)
def coinToss():
    heads = 0
    tails = 0
    for i in range (1,5001):
        if random_num == 0:
            heads = heads + 1
            print "Attempt #{}: Throwing a coin .... it's a head! .... got {} head(s) so far and {} tail(s) so far".format(i,heads,tails)
        else:
            tails = tails + 1
            print "Attempt #{}: Throwing a coin .... it's a tail! ... got {} heads(s) so far and {} tail(s) so far ".format(i,heads,tails)
