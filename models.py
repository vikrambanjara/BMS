
import sqlite3
connection = sqlite3.connect('blooddatabase.db')
cursur = connection.cursor()

cursur.execute("""CREATE TABLE IF NOT EXISTS user
               (
                ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name TEXT NOT NULL,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                role INT NOT NULL DEFAULT 1
               )""")

cursur.execute("""CREATE TABLE IF NOT EXISTS BLOOD_DONOR
               (
                username TEXT NOT NULL UNIQUE,
                blood_group TEXT NOT NULL,
                DONATION_DATE DATE NOT NULL)""")

cursur.execute("""CREATE TABLE IF NOT EXISTS BLOOD_RECEIVER
               ( usernmame TEXT NOT NULL UNIQUE,
                blood_group TEXT NOT NULL,
                RECEIVE_DATE DATE NOT NULL)""")

print("successfully create table")


def find_username(username):
   cursur.execute("SELECT * FROM user WHERE username=?",(username,))
   data=cursur.fetchone()
   if data:
      return True
   return False

   

def create_user(data):
    cursur.execute("INSERT INTO user (username,password, name,role ) VALUES(?,?,?,?)",data)
    connection.commit()
    return True
   

def donote_date(username):
    cursur.execute("SELECT donote_date FROM blood_donor WHERE username(?)",username)
    data=cursur.fetchone()
    if data:
        return data
    return False

def receiver_date(username):
    cursur.execute("SELECT receiver_date FROM blood_receiver WHERE username(?)",username)
    data=cursur.fetchall()
    if data:
       return data
    return False

    


def blood_donor(data):
    cursur.execute("INSERT INTO blood_donor VALUES(?,?,?)",data)
    connection.commit()
    return True


    
def blood_receiver(data):
    cursur.execute("INSERT INTO blood_receiver VALUES(?,?,?)",data)
    connection.commit()
    return True

def users_info():
    cursur.execute("SELECT * FROM USERS")
    data = cursur.fetchall()
    return data


# def user_update(username):
#     cursur.execute("UPDATE FROM user_update WHERE username=(?) ",(username,))
#     connection.commit()
#     return True


def delete_user(username):
    cursur.execute("DELETE FROM user WHERE username=(?) ",(username,))
    connection.commit()
    return True


connection.commit()


    