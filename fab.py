num=int(input("Enter Range:"))
firstnum=int(input("Enter First Number:"))
secondnum=int(input("Enter second number:"))
for i in range(num):
    next=firstnum+secondnum
    firstnum=secondnum
    secondnum=next
    print(next,end=",")