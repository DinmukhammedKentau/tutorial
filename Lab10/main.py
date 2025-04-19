from Lab10.db.dbConnector import DBConnector
from Lab10.db.PhoneBook import PhoneBook

db=DBConnector()
db.createTable()
while True:
   print("[1] ADD USER")
   print("[2] ALL USERS")
   print("[3] UPDATE USER")
   print("[4] DELETE USER")
   print("[0] EXIT")
   choice=int(input("Enter your choice: "))
   if choice==0:
       break
   elif choice==1:
      print("ENTER NAME")
      name=input()
      print("ENTER SURNAME")
      surname=input()
      print("ENTER PHONE NUMBER")
      phone=input()
      user=PhoneBook(name,surname,phone)
      db.add_phone(user)
   elif choice==2:
       allUsers=db.get_all_users()
       for user in allUsers:
          print(user)
   elif choice==3:
      allUsers = db.get_all_users()
      for user in allUsers:
         print(user)
      print("ENTER ID:")
      id=int(input())
      print("UPDATE BY NAME/PHONE NUMBER?")
      upd=input()
      if upd=="name":
         print("ENTER NEW NAME:")
         name=input()
         db.update_first_name(id,name )
      elif upd=="phone":
         print("ENTER NEW PHONE NUMBER:")
         new_phone=input()
         db.update_phone_by_phone(id,new_phone)
   elif choice==4:
         allUsers = db.get_all_users()
         for user in allUsers:
            print(user)
         a=input("ID engiz oshirgin keletinin")#PostgreSQL
         # автоматты түрде жолды санға түрлендіре алады (егер мән сан болса)
         db.delete_phone_by_id(a)

