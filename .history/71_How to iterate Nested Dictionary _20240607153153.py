students={
    101:{'name':'Abakash','email':'Abakash@gmail.com','address':'paradeep'},
    102:{'name':'Urmi','email':'Urmi@gmail.com','address':'cuttack'},
    103:{'name':'rahul','email':'rahul@gmail.com','address':'bbsr'},
    104:{'name':'zini','email':'zini@gmail.com','address':'paradeep'}
}

for k,v in students.items():
    print('student id is : ',k)

    for i in v:
        print(f'{i} is : {v[i]}')
    print('-'*20)