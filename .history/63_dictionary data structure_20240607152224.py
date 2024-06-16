# myinfo = {
#     'name': 'Abakash',
#     'email': 'Abakash@gmail.com',
#     'address': 'paradeep',
#     'mobile': 9090102423
# }

# print(myinfo['name'])
# print(myinfo)

# myinfo = {
#     'name': 'Abakash',
#     'Name': 'Priyanak',
#     'email': 'Abakash@gmail.com',
#     'address': 'paradeep',
#     'mobile': 9090102423
# }

# print(myinfo)

# Duplicate keys are not allowed
# myinfo = {
#     'name': 'Abakash',
#     'name': 'Priyanak',
#     'email': 'Abakash@gmail.com',
#     'address': 'paradeep',
#     'mobile': 9090102423
# }

# print(myinfo['name'])


# different ways for creating dict
# empty dict
# d = {}
# print(d)
# print(type(d))

# create empty dict then add item
# d = {}
# print(d)

# d['name'] = 'Abakash'
# d['address'] = 'paradeep'
# d['email'] = 'Abakash@gmail.com'

# print(d)


# create dict directly

# roll={1:'Abakash',2:'priyanka',3:'rahul',4:'zini'}
# print(roll)

# roll = {1: 'Abakash', 2: 'priyanka', 3: 'rahul', 4: 'zini'}
# print(roll[11])

# roll = {0: 'Abakash', 2: 'priyanka', 3: 'rahul', 4: 'zini'}
# print(roll[0])


# check the key is exists or not
# has_key()

# roll = {1: 'Abakash', 2: 'priyanka', 3: 'rahul', 4: 'zini'}
# print(roll.has_key(2))


# solution
# use in operator

# roll = {1: 'Abakash', 2: 'priyanka', 3: 'rahul', 4: 'zini'}
# print(2 in roll)
# print(2 not in roll)


#  Create a dictionary dynamically by taking user input


# d = {}

# while True:
#     key = input('Entre the key : ')
#     val = input('Enter the value : ')
#     d[key] = val

#     choice = input('Do you want to add more element [Y/N] : ').upper()

#     if choice == 'N':
#         break

# print(d)


# Traversing a dict
# roll = {1: 'Abakash', 2: 'priyanka', 3: 'rahul', 4: 'zini'}

# print only keys
# for i in roll:
#     print(i)


# print key and value
# roll = {1: 'Abakash', 2: 'priyanka', 3: 'rahul', 4: 'zini'}

# for i in roll:
#     print(i, roll[i])

# add item in dict
# d = {23: 'Abakash', 24: 'priyanka', 25: 'rahul', 26: 'zini'}
# print(d)
# d[27] = 'anjali'
# print(d)


# modify
# d = {23: 'Abakash', 24: 'priyanka', 25: 'rahul', 26: 'zini'}
# print(d)
# d[24] = 'anjali'
# print(d)

# d[1024] = 'hello'
# print(d)


# delete item

# d = {23: 'Abakash', 24: 'priyanka', 25: 'rahul', 26: 'zini'}
# print(d)
# del d[26]
# print(d)


# d = {23: 'Abakash', 24: 'priyanka', 25: 'rahul', 26: 'zini'}
# print(d)
# del d[123]
# print(d)


# delete all the items


# d = {23: 'Abakash', 24: 'priyanka', 25: 'rahul', 26: 'zini'}
# print(d)
# d.clear()
# print(d)


# how to delete entire dict

# d = {23: 'Abakash', 24: 'priyanka', 25: 'rahul', 26: 'zini'}
# print(d)
# del d
# print(d)


# dict key immutable in nature  henece we cant use list , set , dict as a dict key but we can use Number,Tuple,frozenset as a dict key otherwise we will get TypeError

# d = {[21, 22, 23]: 'Abakash', 24: 'Urmi', 25: 'rahul', 26: 'zini'}
# print(d)


# d = {(21, 22, 23): 'Abakash', 24: 'Urmi', 25: 'rahul', 26: 'zini'}
# print(d)


# l = [21, 22, 23]
# d = {l: 'Abakash', 24: 'Urmi', 25: 'rahul', 26: 'zini'}
# print(d)

# l.append(100)


# s = set((10, 20, 30))
# d = {s: 'Abakash', 24: 'Urmi', 25: 'rahul', 26: 'zini'}
# print(d)


# s = set((10, 20, 30))
# d = {frozenset(s): 'Abakash', 24: 'Urmi', 25: 'rahul', 26: 'zini'}
# print(d)

# s = set((10, 20, 30))
# d = {frozenset(s): 'Abakash', 24: 'Urmi', 25: 'rahul', 26: 'zini'}
# print(d[frozenset({10, 20, 30})])

# d = {12+13j: 'Abakash', 24: 'Urmi', 25: 'rahul', 26: 'zini'}
# print(d)


# d = {True: 'Abakash', 24: 'Urmi', 25: 'rahul', 26: 'zini'}
# print(d)

# d = {{1: 'one'}: 'Abakash', 24: 'Urmi', 25: 'rahul', 26: 'zini'}
# print(d)


# d = {23: {1: 'one'}, 24: 'Urmi', 25: 'rahul', 26: 'zini'}
# print(d)
