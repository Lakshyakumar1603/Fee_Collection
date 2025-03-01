import admin as ad
ad.create()
import cls as c
import fee as f
import report as r


a=True
print("***FEE MANAGEMENT PROJECT***".center(120))
while a:
    n=50
    print(n*'~')
    print('***MAIN MENU***'.center(20))
    print("1. Class Management")
    print("2. Fee Management")
    print("3. Report")
    print("4. Admin")
    print("5. EXIT.")
    print(n*'~')
    ch=int(input("Enter your Choice  : "))
    if ch==1:
        c.menu()
    elif ch==2:
        f.menu()
    elif ch==3:
        r.menu()
    elif ch==4:
        ad.menu()
    elif ch==5:
        a=False
        print('BYE BYE! . . . Have a good day!')
    else:
        print("Enter a VALID Choice!!")
