import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred)
'''
try:
    #email = input("Please enter your email : ")
    email = input("Please enter your email : ")
    user = auth.get_user_by_email(email)

    print('User id : {} and user phone : {} '.format(user.uid, user.phone_number))
except:
    print("No user found")

'''

page = auth.list_users()

for user in page.users:
    print("User id : {} and email : {} ".format(user.uid, user.email))




