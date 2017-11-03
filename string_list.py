words = "it's thanksgiving day. It's my Birthday,too"

print words.find('day')

new_words = words.replace("day","month")

print new_words


x = [2,54,-2,7,12,98]

print max(x)
print min(x)

y = ["hello",2,54,-2,7,12,98,"world"]

z = [y[0],y[-1]]
print z

a = [19,2,54,-2,7,12,98,32,10,-3,6]

a.sort()
print a


b = a[:len(a)/2]

print b

del a[:5]

a.insert(0,b)
print a
