str="ABAB"
dict={}
for ch in str:
    if(ch not in dict):
        dict[ch]=1
    else:
        print("frst recsve ch=",ch)
        break