lst=[10,20,21,24,25]
flg=0
element=int(input("enter num"))
for item in lst:
    if(item==element):
        flg+=1
        break
    else:
        flg=0
if flg==0:
     print("not found")
else:
    print("found")