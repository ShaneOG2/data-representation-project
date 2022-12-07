import mysql.connector
from . import dbconfig as cfg
class User:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''
    
    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']


    def get_cursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def close_all(self):
        self.connection.close()
        self.cursor.close()

    def create_database(self):
        # Create database 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password   
        )
        self.cursor = self.connection.cursor()
        sql = "create database if not exists " + self.database
        self.cursor.execute(sql)

        self.connection.commit()
        self.close_all()

    def create_user_table(self): 
        cursor = self.get_cursor()
        sql='''
            create table if not exists users (
            uid int PRIMARY KEY NOT NULL AUTO_INCREMENT, 
            email VARCHAR(150), 
            password VARCHAR(150), 
            firstname VARCHAR(150));
            '''
        cursor.execute(sql)

        self.connection.commit()
        self.close_all() 
         
    def create_user(self, values):
       cursor = self.get_cursor()
       sql="insert into users (email, password, firstname) values (%s, %s, %s)"
       cursor.execute(sql, values)

       self.connection.commit()
       newid = cursor.lastrowid
       self.close_all()
       return newid  

    def get_user_password(self, email):
        cursor = self.get_cursor()
        sql="select password from users where email = %s limit 1"
        values = (email, )
        cursor.execute(sql, values)
        result =  cursor.fetchone()
        password = result[0]
        self.close_all()
        return password

class Note:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''
    
    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']

    def get_cursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def close_all(self):
        self.connection.close()
        self.cursor.close()

    def create_note_table(self): 
        cursor = self.get_cursor()
        sql='''create table if not exists notes (
            nid int NOT NULL AUTO_INCREMENT, 
            data VARCHAR(1000), 
            uid int,
            PRIMARY KEY (nid),
            FOREIGN KEY (uid) REFERENCES users(uid));
            '''
        cursor.execute(sql)

        self.connection.commit()
        self.close_all() 
         
    def create_note(self, values):
       cursor = self.get_cursor()
       sql="insert into notes (data, uid) values (%s, %s)"
       cursor.execute(sql, values)

       self.connection.commit()
       newid = cursor.lastrowid
       self.close_all()
       return newid   
 

#if __name__ == "__main__":
    #Users.create_database()

    #Users.create_user_table()

    #Notes.create_note_table()
#
    #Users.create_user(("shane@gmail.com", "12345678", "Shane"))

    #Notes.create_note_table()
    #Users.create_user(("paul@gmail.com", "12345678", "Paul"))
#
    #Notes.create_note(("Hello ervretgvergrege4r5g gfe e4ge3 4gege3f4 4 343 r", "6"))
    
    #print("sanity")