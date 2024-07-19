import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred, {'databaseURL':'https://myproject-1de74-default-rtdb.firebaseio.com/'})

#inserting data
'''
ref = db.reference('/')

ref.set({
    'Employee': {
        'emp1' : {
            'name': 'Gouri',
            'email' : 'gouribiju1902@gmail.com',
            'age' : 20
        }
    }
})
'''

ref = db.reference('Employee2')

emp_ref = ref.push({
    'name':'test',
    'lname':'testlname',
    'email':"test@gmail.com",
    'age':23
})

print(emp_ref)
