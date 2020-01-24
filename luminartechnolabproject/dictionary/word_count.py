line="hai hello hai how"
words=line.split(" ")
dict={}
for word in words:
    if(word not in dict):
        dict[word]=1
    else:
        dict[word]+=1
for item in dict:
    print(item,end=" ")
    print(dict[item])