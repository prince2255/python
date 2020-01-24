lst[1,3,2,4,5,6,8,9,10]
lst.sort()
element=int(input("enter num"))
flg=0
low=0
upp=len(lst)
while(low<=upp):
    value=lst[low]+lst[upp]
   if(element==value):
    flg+=1
    break
   elif(value<element):
       low+=1
   elif(value>element):
        upp-=1
        print((lst[low],lst[upp]))
else:
    print(not found)
