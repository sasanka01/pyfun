# l = [2,3,1,7,4,12]
#l = ['magical','unicorns']
l = ['magical unicorns',19,'hello',98.98,'world']
add = 0
strings = ""
output = ""

for i in l:
    if isinstance(i,int):
        add = add + i
        if output == "string":
            output = "mixed"
        else:
            output = "integer"

    elif isinstance(i,str):
        strings = strings + i
        if output == "integer":
            output = "mixed"
        else:
            output = "string"

print add
print strings
print output
