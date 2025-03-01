#DATABASE
import mysql.connector as con

def checkDB():
    mydb=con.connect(host='localhost',user='root')
    myc=mydb.cursor()
    myc.execute('show databases')
    result=myc.fetchall()
    #print(result)
    ctr=0
    db="fee_structure"
    for i in result:
        if i[0]==db:
            ctr+=1
    return ctr

def dropDB():
    mydb=con.connect(host='localhost',user='root')
    myc=mydb.cursor()
    myc.execute('drop database Fee_structure')

def createDB():
    mydb=con.connect(host='localhost',user='root')
    myc=mydb.cursor()
    myc.execute('create database Fee_structure')
    myc.execute('use Fee_structure')
    myc.execute("""create table class
(
cid integer Primary key auto_increment,
cname varchar(4),
sec char(1),
tname varchar(20))""")

    myc.execute("""create table fee
(
fid integer primary key auto_increment,
cid integer,
stu integer,
date date,
sf integer,
lsf integer,
tsf integer,
vvn integer,
lvvn integer,
tvvn integer,
cf integer,
gt integer)""")
    myc.execute("create table pw(pw varchar(20))")
    myc.execute("insert into pw values('qwaszx')")
    mydb.commit()
    print("Database Created")

def cls_rec():
    mydb=con.connect(host='localhost',user='root',database='fee_structure')
    myc=mydb.cursor()
    l=['A','B','C','D']
    n=3
    for i in range(1,13):
        if i>10:
            n=4
        for j in range(n):
            sql="insert into class(cname,sec) values({},'{}')".format(i,l[j])
            myc.execute(sql)
            mydb.commit()
    
def create():
    a=checkDB()
    if a==0:
        createDB()
        cls_rec()

def pw():
    p=input("Enter password:")
    mydb=con.connect(host='localhost',user='root',database='fee_structure')
    myc=mydb.cursor()
    myc.execute("select * from pw")
    r=myc.fetchone()
    if p==r[0]:
        return 1

def changePW():
    mydb=con.connect(host='localhost',user='root',database='fee_structure')
    myc=mydb.cursor()
    npw=input('Enter new password:')
    myc.execute("update pw set pw='{}'".format(npw))
    mydb.commit()
    
def menu():
    if pw()==1:
        a=True
        while a:
            n=50
            print('\n')
            print(n*'~')
            print('***ADMIN***'.center(20))
            print("1. Recreate Database")
            print("2. Change password")
            print("3. Return to Main Menu")
            ch=int(input("Enter your Choice  : "))
            print(n*'~')
            if ch==1:
                dropDB()
                createDB()
                cls_rec()
            elif ch==2:
                changePW()
            elif ch==3:
                a=False
    else:
        print('Wrong password!!!')
