w=open("/home/user/Downloads/fakefriends.csv")
dict={}
for lines in w:
    words=lines.rstrip("\n").split(",")
    if(words[2] not in dict):
        dict[words[2]]=1
    else:
        dict[words[2]]+=1
print(dict)
tem=list()
for k,v in dict.items():
    tem.append((v,k))
    tem=sorted(tem)
print(tem)
print("count=",tem[0][0])
print("age=",tem[0][1])
print("max count=",tem[-1][0])
print("age of max count=",tem[-1][1])