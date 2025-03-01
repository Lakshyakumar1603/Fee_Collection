#class
import mysql.connector as con
mydb=con.connect(host='localhost',user='root',database='fee_structure')
myc=mydb.cursor()

def show_cls():
    myc.execute('select * from class')
    result=myc.fetchall()
    print("\n")
    n=50
    print("*"*n)
    print("Class_ID\tClass\t\tTeacher Name")
    for i in result:    
        print('  ',i[0],' \t\t',i[1],i[2],'\t\t',i[3])
    print("*"*n)

def ct():
    cls=int(input("Enter Class:"))
    sec=input("Enter Section:")
    nm=input("Enter class Teacher's Name to Add/Update:")
    if len(nm)<20:
        nm=nm+(20-(len(nm)))*(' ')
    nm=nm.capitalize()
    sql="update class set tname='{}' where cname={} and sec='{}'".format(nm,cls,sec)
    myc.execute(sql)
    mydb.commit()
    print("Updated!")

def menu():
    a=True
    while a:
        n=50
        print('\n')
        print(n*'~')
        print('***CLASS MANAGEMENT***'.center(20))
        print("1. Show All Classes")
        print("2. Add/Update Class Teacher")
        print("3. Return to Main Menu")
        ch=int(input("Enter your Choice  : "))
        print(n*'~')
        if ch==1:
            show_cls()
        elif ch==2:
            ct()
        elif ch==3:
            a=False
