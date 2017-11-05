import random
random_num = random.randint(1,100)
def grades(random_num):
    # print random_num
    if random_num in range(60,70):
        print "score", random_num, ": Your grade is D"
        # return random_num
    elif random_num in range(70,80):
        print "score", random_num, ": Your grade is C"
    elif random_num in range(80,90):
        print "score", random_num, "Your grade is B"
    elif random_num in range(90,101):
        print "score", random_num, "your grade is A"
    else:
        print "End of the program . Bye"

    return random_num


grade = grades(random_num)
print grade
