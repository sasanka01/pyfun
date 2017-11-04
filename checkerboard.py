for i in range(1, 9):
        if (i%10==0):
            output = "\n"
        elif(i%2==0):
            output = " *" * 4
        else:
            output = "* " * 4
        print output
