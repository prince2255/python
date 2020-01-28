w=open("/home/user/PycharmProjects/luminartechnolabproject/files/word_count_text")
dict={}
for lines in w:
    words=lines.rstrip("\n").split(" ")
    for word in words:
        if(word not in dict):
            dict[word]=1
        else:
            dict[word]+=1
print(dict)