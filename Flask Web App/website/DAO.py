import mysql.connector
from . import dbconfig as cfg
from flask_login import UserMixin

class Users_Class:
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

    def get_user_exists(self, email):
        exists = True
        cursor = self.get_cursor()
        sql="select email from users where email = %s limit 1"
        values = (email, )
        cursor.execute(sql, values)
        result =  cursor.fetchone()
        if result is None:
            exists = False
        self.close_all()

        return exists

    def get_user_uid(self, email):
        cursor = self.get_cursor()
        sql="select uid from users where email = %s limit 1"
        values = (email, )
        cursor.execute(sql, values)
        result =  cursor.fetchone()
        id = result[0]
        self.close_all()

        return id
    
    def get_user_firstname(self, email):
        cursor = self.get_cursor()
        sql="select firstname from users where email = %s limit 1"
        values = (email, )
        cursor.execute(sql, values)
        result =  cursor.fetchone()
        firstname = result[0]
        self.close_all()

        return firstname

    def get_user_firstname_by_uid(self, uid):
        cursor = self.get_cursor()
        sql="select firstname from users where uid = %s"
        values = (uid, )
        cursor.execute(sql, values)
        result =  cursor.fetchone()
        firstname = result[0]
        self.close_all()

        return firstname

    def get_user_password(self, email):
        cursor = self.get_cursor()
        sql="select password from users where email = %s limit 1"
        values = (email, )
        cursor.execute(sql, values)
        result =  cursor.fetchone()
        password = result[0]
        self.close_all()

        return password

    def get_user_password_by_uid(self, uid):
        cursor = self.get_cursor()
        sql="select password from users where uid = %s"
        values = (uid, )
        cursor.execute(sql, values)
        result =  cursor.fetchone()
        password = result[0]
        self.close_all()

        return password

    def get_user_email_by_uid(self, uid):
        cursor = self.get_cursor()
        sql="select email from users where uid = %s"
        values = (uid, )
        cursor.execute(sql, values)
        result =  cursor.fetchone()
        email = result[0]
        self.close_all()

        return email



class User_Class(UserMixin):
    def __init__(self, uid, email, password, name, active=True):
        self.uid = uid
        self.email = email
        self.password = password
        self.name = name
        self.active = active

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def get_id(self):
        return self.uid

class Notes_Class:
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
            date VARCHAR(20), 
            time VARCHAR(20), 
            data VARCHAR(1000), 
            euro VARCHAR(20),
            usd VARCHAR(20),
            gbp VARCHAR(20),
            uid int, 
            PRIMARY KEY (nid),
            FOREIGN KEY (uid) REFERENCES users(uid))
            '''
        cursor.execute(sql)

        self.connection.commit()
        self.close_all() 
         
    def create_note(self, values):
       cursor = self.get_cursor()
       sql="insert into notes (data, date, time, euro, usd, gbp, uid) values (%s, %s, %s, %s, %s, %s, %s)"
       cursor.execute(sql, values)

       self.connection.commit()
       newid = cursor.lastrowid
       self.close_all()
       return newid   

    def get_user_notes(self, uid):
        cursor = self.get_cursor()
        sql="select data from notes where uid = %s"
        values = (uid, )
        cursor.execute(sql, values)
        results =  cursor.fetchall()
        notes = []
        for i in results:
            notes.append(i[0])
        self.close_all()

        return notes

    def get_user_date(self, uid):
        cursor = self.get_cursor()
        sql="select date from notes where uid = %s"
        values = (uid, )
        cursor.execute(sql, values)
        results =  cursor.fetchall()
        date = []
        for i in results:
            date.append(i[0])
        self.close_all()

        return date

    def get_user_time(self, uid):
        cursor = self.get_cursor()
        sql="select time from notes where uid = %s"
        values = (uid, )
        cursor.execute(sql, values)
        results =  cursor.fetchall()
        time = []
        for i in results:
            time.append(i[0])
        self.close_all()

        return time

    def get_user_euro(self, uid):
        cursor = self.get_cursor()
        sql="select euro from notes where uid = %s"
        values = (uid, )
        cursor.execute(sql, values)
        results =  cursor.fetchall()
        euro = []
        for i in results:
            euro.append(i[0])
        self.close_all()

        return euro

    def get_user_usd(self, uid):
        cursor = self.get_cursor()
        sql="select euro from notes where uid = %s"
        values = (uid, )
        cursor.execute(sql, values)
        results =  cursor.fetchall()
        usd = []
        for i in results:
            usd.append(i[0])
        self.close_all()

        return usd
    
    def get_user_gbp(self, uid):
        cursor = self.get_cursor()
        sql="select euro from notes where uid = %s"
        values = (uid, )
        cursor.execute(sql, values)
        results =  cursor.fetchall()
        gbp = []
        for i in results:
            gbp.append(i[0])
        self.close_all()

        return gbp

    def get_user_nid(self, uid):
        cursor = self.get_cursor()
        sql="select nid from notes where uid = %s"
        values = (uid, )
        cursor.execute(sql, values)
        results =  cursor.fetchall()
        nid = []
        for i in results:
            nid.append(i[0])
        self.close_all()

        return nid

    def delete_note_by_nid(self, nid):
        cursor = self.get_cursor()
        sql="delete from notes where nid = %s"
        values = (nid,)

        cursor.execute(sql, values)

        self.close_all()
 
