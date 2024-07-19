import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred)


email = input("Enter the email : ")

user = auth.get_user_by_email(email)

#print(user.email_verified)