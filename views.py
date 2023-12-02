import controler
import datetime
import models



def main():
   print("welcome to blood bank")
   print("enter 1 for log_in")

def admin():
   print("enter 1 for user registeration")
   print("enter 2 for blood donate")
   print("enter 3 for blood reciver")
   print("enter 4 for read all user information")
   print("enter 5 for Update a user")
   print("enter 6 for delete a user")
   print("any other number for exit")



def user_choice(n):
    if n == '1':
        user_choice()
            
def  admin_choice(n):
    if n == '1':
        user_registeration()
    elif n=='2':
        blood_donor()
    elif n == '3':
        blood_receive()
    elif n == '4':
        users_info()
    elif n == '5':
        user_update()
    elif n == '6':
        delete_user()
    else:
        print("Invalid choice")


def user_registeration():
    '''
    role 1 for user
    role 2 for admin
    '''
    username=input("enter the username : ")
    password=input("enter the password : ")
    name=input("enter the name : ")
    role=input("enter the role : ")
    data= (username,password, name, role)
    if models.create_user(data):
       print("user registeration successfully")
    else:
        print("user registeration failed")


def blood_donor():
    user_name= input("enter user_name")
    blood_group=input("enter blood_group")
    donote_date=datetime.datetime.now().date()
    data=(user_name,blood_group,donote_date)
    if donote_date(data):
        models.blood_donor(data)
        print("donote successfully")
    return False
   
    

def blood_receive():
    user_name=input("enter user_name:")
    blood_group=input("enter blood_group")
    receive_date=datetime.datetime.now().date()
    data=(user_name,blood_group,receive_date)
    if receive_date(data):
        models.blood_receiver(data)
        print("Receive successfully")
    return False
    
    

def users_info():
    data=models.users_info()
    print(data)
    

def user_update():
    user_name=input("enter your username")
    data=models.user_update(user_name)
    print("user update successfully",data)

      

def delete_user():
    user_name=input("enter your user_name:")
    models.delete_user(user_name)
    print("user delete successfully")


def login():
    username = input("Enter your username : ")
    password = input("Enter your password : ")
    role = controler.user_validestion(username,password)
    if role :
        if role == 2:
            print("log in successfully")
          
        else:
            user_registeration()
            print("log in successfully")
            
          
    else:    
        print("Invalid username or password")







    
    

    





