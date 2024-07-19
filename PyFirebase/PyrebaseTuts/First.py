import pyrebase


firebaseConfig = {
  "apiKey": "AIzaSyB_472PSuQvvsjrT6UqfoEFFWxaDNAxEzo",
  "authDomain": "testproject-301ac.firebaseapp.com",
  "databaseURL":"https://testproject-301ac-default-rtdb.firebaseio.com/"
  "projectId": "testproject-301ac",
  "storageBucket": "testproject-301ac.appspot.com",
  "messagingSenderId": "1002844568057",
  "appId": "1:1002844568057:web:17f3ef4521911af1af6528",
  "measurementId": "G-RNJB2CW9LD"
}

firebase =pyrebase.initialize_app(firebaseConfig)