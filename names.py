def names(list):
    for i in range(0,len(list)):
        student = list[i]
        # print student
        print student['first_name'], student['last_name']


students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

names(students)


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }


def names_2(dic):
    for key,value in dic.items():
        print key
        for counter, i in enumerate(value,1):
            print counter,'- ' + i['first_name'],i['last_name'] +' -', len(i['first_name']) + len(i['last_name'])

names_2(users)
