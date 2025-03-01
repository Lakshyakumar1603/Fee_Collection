#REPORT
import mysql.connector as con
import json
import datetime as dt

mydb=con.connect(host='localhost',user='root',database='fee_structure')
myc=mydb.cursor()
    

def check_date2(d):
    valid=True
    try:
        dd,mm,yy=d.split('-')
    except Exception as e:
        valid=False
    try:
        dt.datetime(int(yy),int(mm),int(dd))
    except ValueError:
        valid=False
    except NameError:
        valid=False
    if valid==True:
        return 1
    else:
        return 2

def date_change(a):
    d,m,y=a[0:2],a[3:5],a[6:10]
    date=y+'-'+m+'-'+d
    return date

def part_date():
    a=True
    while a:
        date=input("Enter Date(dd-mm-yyyy): ")
        if check_date2(date)==2:
            print("Enter Valid Date")
        elif check_date2(date)==1:
            date=date_change(date)
            sql="select cname,sec,tname,date,vvn,sf,cf,lvvn,lsf from class c,fee f where c.cid=f.cid and date='{}'".format(date)
            myc.execute(sql)
            result=myc.fetchall()
            if len(result)==0:
                print("NO DATA FOUND!")
                a=False        
            else:
                n=130
                print("\n")
                print('.'*n)
                print("Class\t Teacher's name\t\t   Date\t\t VVN\t SF\t CF\tLVVN\tLSF\n")
                for i in result:
                    #print(i[0])
                    print(i[0],i[1],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t',i[6],'\t',i[7],'\t',i[8])
                tvvn,tsf,tcf,tlvvn,tlsf=0,0,0,0,0
                for j in result:
                    tvvn=tvvn+j[4]
                    tsf=tsf+j[5]
                    tcf=tcf+j[6]
                    tlvvn=tlvvn+j[7]
                    tlsf=tlsf+j[8]
                gt=tvvn+tsf+tcf+tlvvn+tlsf
                data={'Total VVN':tvvn,'Total SF':tsf,'Total CF':tcf,'Total LATE VVN':tlvvn,'Total LATE SF':tlsf,'Grand Total':gt}
                print("\n")
                print(json.dumps(data,indent=30))
                print('.'*n)
                a=False        

def pr_date(d):
    month="jan feb mar apr may jun jul aug sep oct nov dec"
    mnm=month.split()
    
    return str(d[-2:])+"-"+mnm[int(d[5:7])-1].upper()+"-"+str(d[:4])
    
def part_class():
    cls=input("Enter class: ")
    sec=input("Enter section: ")
    sql="select tname,date,vvn,sf,cf,lvvn,lsf from class c,fee f where c.cid=f.cid and cname='{}' and sec='{}'".format(cls,sec)
    myc.execute(sql)
    result=myc.fetchall()
    if len(result)==0:
        print("NO DATA FOUND!")
    else:
        n=55
        print("\n")
        print("'"*n)
        print('Teacher name:',result[0][0].capitalize(),'\n')
        print("DATE\t\t  VVN\t  SF\t  CF\tLVVN\tLSF")
        for i in result:
            print(pr_date(str(i[1])),'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t',i[6])
        tvvn,tsf,tcf,tlvvn,tlsf=0,0,0,0,0
        for j in result:
            tvvn=tvvn+j[2]
            tsf=tsf+j[3]
            tcf=tcf+j[4]
            tlvvn=tlvvn+j[5]
            tlsf=tlsf+j[6]
        print("'"*n)
        print("The GRAND TOATAL:".center(60))
        data={'Total VVN':tvvn,'Total SF':tsf,'Total CF':tcf,'Total LATE VVN':tlvvn,'Total LATE SF':tlsf,}
        print(json.dumps(data,indent=20))
        print("'"*n)


def menu():
    a=True
    while a:
        n=50
        print('\n')
        print(n*'~')
        print('***REPORT***'.center(20))
        print("1. Class wise Report")
        print("2. Date wise Report")
        print("3. Return to Main Menu")
        ch=int(input("Enter your Choice  : "))
        print(n*'~')
        if ch==1:
            part_class()
        elif ch==2:
            part_date()
        elif ch==3:
            a=False
