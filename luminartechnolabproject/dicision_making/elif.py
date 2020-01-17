no1=int(input("enter the value no1"))
no2=int(input("enter the value no2"))
no3=int(input("enter thew value no3"))
if(no1>no2):
    if(no1>no3):
        print("no1 is greater")
    else:print("no3 is greater")
elif(no2>no3):
    print("no2 is greater")
else:
    print("no3 is greater")