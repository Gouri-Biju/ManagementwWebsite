import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred)

email = input("Please enter your email : ")
password = input("Please enter your password : ")
phone = input("Please enter your phone number : ")
id = input("Please enter your id : ")

user = auth.create_user(uid=id,email=email, password=password, phone_number=phone)
print("User created {} : ".format(user.uid))
