#FEE
import json
import mysql.connector as con
mydb=con.connect(host='localhost',user='root',database='fee_structure')
myc=mydb.cursor()

def date_change(a):
    d,m,y=a[0:2],a[3:5],a[6:10]
    date=y+'-'+m+'-'+d
    return date

def date_check(a):
    d=a[0:2]
    d=int(d)
    if d>15:
        return 1

def clscode(c,s):
    c=str(c)
    s=s.upper()
    d={'1A':1,'1B':2,'1C':3,'2A':4,'2B':5,'2C':6,'3A':7,'3B':8,'3C':9,'4A':10,'4B':11,'4C':12,'5A':13,'5B':14,'5C':15,'6A':16,'6B':17,'6C':18,'7A':19,'7B':20,'7C':21,'8A':22,'8B':23,'8C':24,'9A':25,'9B':26,'9C':27,'10A':28,'10B':29,'10C':30,'11A':31,'11B':32,'11C':33,'11D':34,'12A':35,'12B':36,'12C':37,'12D':38}
    cls=c+s
    for i in d:
        if cls==i:
            a=d[cls]
    return a


def fee_rec():
    c=int(input("Enter Class(In digits): "))
    s=input("Enter section: ")
    cid=clscode(c,s)
    date=input("Enter date(dd-mm-yyyy): ")
    stu=int(input("Enter number of students: "))
    vvn=int(input("Enter Vidyalaya Vikash nidhi(VVN): "))
    sf=int(input("Enter Tution Fee(SF): "))
    cf=int(input("Enter Computer Fee(CF): "))
    lsf=0
    lvvn=0
    if date_check(date)==1:
        lsf=int(input("Enter LATE Tution Fee(SF): "))
        lvvn=int(input("Enter LATE Vidyalaya Vikash nidhi(VVN): "))
    tsf=sf+lsf
    tvvn=vvn+lvvn
    gt=tsf+tvvn+cf
    date=date_change(date)
    sql="insert into fee(cid,stu,date,sf,lsf,tsf,vvn,lvvn,tvvn,cf,gt) values({},{},'{}',{},{},{},{},{},{},{},{})".format(cid,stu,date,sf,lsf,tsf,vvn,lvvn,tvvn,cf,gt)
    myc.execute(sql)
    mydb.commit()
    print("Data Saved!")

def view():
    mydb=con.connect(host='localhost',user='root',database='fee_structure')
    myc=mydb.cursor()
    sql="select cname,sec,tname,sum(vvn),sum(sf),sum(cf),sum(lvvn),sum(lsf),gt from class c,fee f where c.cid=f.cid group by c.cid"
    myc.execute(sql)
    result=myc.fetchall()
    if len(result)==0:
        print("NO FEE DEPOSITED YET!")
    else:
        n=130
        print("\n")
        print("`"*n)
        print("Class\t  Teacher's Name\tTotal VVN\tTotal SF\tTotal CF\tTotal LATE VVN\t Total LATE SF\n")
        for i in result:
            print(' ',i[0],i[1],'\t',i[2],'\t',i[3],'\t\t',i[4],'\t\t',i[5],'\t\t',i[6],'\t\t',i[7])
        tvvn,tsf,tcf,tlvvn,tlsf=0,0,0,0,0
        for j in result:
            tvvn=int(tvvn+j[3])
            tsf=int(tsf+j[4])
            tcf=int(tcf+j[5])
            n=int(tlvvn+j[6])
            tlsf=int(tlsf+j[7])
        gt=tvvn+tsf+tcf+tlvvn+tlsf
        data={'Total VVN':tvvn,'Total SF':tsf,'Total CF':tcf,'Total LATE VVN':tlvvn,'Total LATE SF':tlsf,'Grand Total':gt}
        print("`"*n)
        print("The GRAND TOATAL:".center(60))
        print(json.dumps(data,indent=20))
        print("`"*n)

def menu():
    a=True
    while a:
        n=50
        print(n*'~')
        print('***FEE MANAGEMENT***'.center(20))
        print("1. Deposit Fee")
        print("2. View Fee")
        print("3. Return to Main Menu")
        ch=int(input("Enter your Choice  : "))
        print(n*'~')
        if ch==1:
            fee_rec()
        elif ch==2:
            view()
        elif ch==3:
            a=False
        else:
            print("Enter valid choice!")
            
