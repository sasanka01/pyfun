# Assignment: Filter by Type
# Write a program that, given some value, tests that value for its type. Here's what you should do for each type:
#
# Integer
# If the integer is greater than or equal to 100, print "That's a big number!" If the integer is less than 100, print "That's a small number"
#
# String
# If the string is greater than or equal to 50 characters print "Long sentence." If the string is shorter than 50 characters print "Short sentence."
#
# List
# If the length of the list is greater than or equal to 10 print "Big list!" If the list has fewer than 10 values print "Short list."
#
# Test your program using these examples:
#
# sI = 45
# mI = 100
# bI = 455
# eI = 0
# spI = -23
# sS = "Rubber baby buggy bumpers"
# mS = "Experience is simply the name we give our mistakes"
# bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
# eS = ""
# aL = [1,7,4,21]
# mL = [3,5,7,34,3,2,113,65,8,89]
# lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
# eL = []
# spL = ['name','address','phone number','social security number']

# USED Dictionary here

my_var ={ 'sI': 45,
'mI' : 100,
'bI' : 455,
'eI' : 0,
'spI' : -23,
'sS' : "Rubber baby buggy bumpers",
'mS' : "Experience is simply the name we give our mistakes",
'bS' : "Tell me and I forget. Teach me and I remember. Involve me and I learn.",
'eS' : "",
'aL' : [1,7,4,21],
'mL' : [3,5,7,34,3,2,113,65,8,89],
'lL' : [4,34,22,68,9,13,3,5,7,9,2,12,45,923],
'eL' : [],
'spL' : ['name','address','phone number','social security number']}


for key,value in my_var.items():
    print value
    print  type(value)
    if type(value) == int and value >= 100:
        print "thats a big number"
    elif type(value) == int and value < 100:
        print "thats a small number"
    if type(value) == str and len(value) >= 50:
        print "Long sentence"
    elif type(value) == str and len(value) < 50:
        print "small sentence"
    if type(value) == list and len(value) >= 10:
        print "big list"
    elif type(value) == list and len(value) < 10:
        print "small list"
