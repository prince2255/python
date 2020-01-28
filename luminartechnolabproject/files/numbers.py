f=open("/home/user/PycharmProjects/luminartechnolabproject/files/numb")
lst=list()
for data in f:
    numbers=data.split(",")
    for number in numbers:
        print(number)