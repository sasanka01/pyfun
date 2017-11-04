word_list = ['hello','world','my','name','is','Anna']
char = 'n'
new_list = []

for word in word_list:
    if char in word:
        # print i
        new_list.append(word)
        print new_list
