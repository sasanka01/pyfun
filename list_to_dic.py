# Create a function that takes in two lists and creates a single dictionary where the first list contains keys and the second values. Assume the lists will be of equal length.
#
# Your first function will take in two lists containing some strings. Here are two example lists:
#
# name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
# favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
# Copy
# Here's some help starting your function.
#
# def make_dict(arr1, arr2):
#   new_dict = {}
#   # your code here
#   return new_dict
# Copy
# Hacker Challenge:
# If the lists are of unequal length, the longer list should be used for the keys, the shorter for the values.


name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]



def list_to_dic(arr1, arr2):
    dictionary = dict(zip(arr1,arr2))
    return dictionary

a = list_to_dic(name,favorite_animal)
print a
