mark1=int(input("enter the mark1"))
mark2=int(input("enter the mark2"))
mark3=int(input("enter the mark3"))
total=mark1+mark2+mark3
if(total>145):
    print("a+")
elif((total>140)&(total<145)):
    print("a")
elif((total>135)&(total<140)):
    print("B+")
elif((total>130)&(total<135)):
    print("B")
else:
    print("fail")