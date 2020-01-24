lst=[1,2,3,4,30,5,6,7,8,11,12,13,14,15]
lst.sort()
flg=0
low=0
upp=len(lst)
mid=(low+upp)//2
element=int(input("enter num"))
while(low<=upp):
    if(element<lst[mid]):
        upp=mid-1
    elif(element>lst[mid]):
        low=mid+1
    elif(element==lst[mid]):
        flg+=1
        break
    mid=(low+upp)//2
if(flg==0):
    print("not found",mid)
else:
    print("found",mid)


