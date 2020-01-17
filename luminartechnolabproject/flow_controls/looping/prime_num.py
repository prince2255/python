no=int(input("no1"))
for i in range(2,no):
    if(no%i==0):
        flg=flg+1
        break
    else:
        flg=0
if(flg==0):
    print("its prime")
else:
    print("not prime")