# list methods part 2
# split()

# s = 'Abakash Das'
# print(s.split())

# s = 'Abakash Das'
# print(s.split('a'))

# s = 'Abakash Das'
# print(s.split('u'))

# s = 'Abakash Dasa'
# print(s.split('u'))

# dob = '1-1-2000'
# print(dob.split('-'))


# dob = '1-1-2000'
# print(dob.split('*'))

# join()

# l = ['Abakash', 'priyanka', 'rahul', 'zini']
# s = '+'.join(l)
# print(s)


# l = ['Abakash', 'priyanka', 'rahul', 'zini']
# s = '*'.join(l)
# print(s)


# l = ['Abakash', 'priyanka', 'rahul', 'zini']
# s = ''.join(l)
# print(s)


# l = ['surendra', 'priyanka', 'rahul', 'zini']
# s = ' '.join(l)
# print(s)

# l = ('Abakash', 'priyanka', 'rahul', 'zini')
# s = '.'.join(l)
# print(s)


# removing space from the string
# rstrip()
# s = 'Abakash      '
# print(len(s))
# print(len(s.rstrip()))

# #lstrip()
# s = '       Abakash       '
# print(len(s))
# print(len(s.rstrip()))


# # strip()
# s = '       Abakash       '
# print(len(s))
# print(len(s.strip()))

# fill char
# zfill()
# s = 'Abakash'
# print(s.zfill(15))


# s = 'Abakash'
# print(s.zfill(50))


# s = 'Abakash'
# print(s.zfill(9))

# rjust()

# s = 'hello'
# print(s.rjust(10))


# s = 'Abakash'
# print(s.rjust(50))


# s = 'Abakash'
# print(s.rjust(10, '*'))


# # ljust()
# s = 'Abakash'
# print(s.ljust(10, '*'))


# center()

# s = 'Abakash'
# print(s.center(20))


# s = 'Abakash'
# print(s.center(20, '*'))


# s = 'Abakash'
# print(s.center(21, '*'))


# min()
# s = 'Abakash'
# print(min(s))

# s = 'surendra'
# print(max(s))


# s = 'Abakash'
# print(sorted(s))


# s = 'Abakash'
# print(sorted(s,reverse=True))


# isidentifier()

# s = '123abc'
# print(s.isidentifier())


# s = 'abc123'
# print(s.isidentifier())


# s = 'True'
# print(s.isidentifier())


# s = '***aaa'
# print(s.isidentifier())

# s = 'Abakash'
# for i in enumerate(s):
#     print(i)


s = 'Abakash'
for i, j in enumerate(s):
    print(i, j)
