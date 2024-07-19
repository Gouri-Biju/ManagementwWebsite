import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred)

email = input("Please enter email : ")
link = auth.generate_email_verification_link(email)
print(link)

#user = auth.get_user_by_email(email)
#print(user.email_verified)

link = auth.generate_password_reset_link(email)
print(link)
