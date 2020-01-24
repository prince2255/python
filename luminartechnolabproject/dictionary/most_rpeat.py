line="hai hai hello hai"
words=line.split(" ")
dict={}
for word in words:
    if(word not in dict):
        dict[word]=1
    else:
        dict[word]+=1
tmp=list()
for k,v in dict.items():
    tmp.append((v,k))
tmp=sorted(tmp)
print(tmp[1])