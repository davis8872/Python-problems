mylist=[int(input("Enter the elements :")) for _ in range(int(input("Enter the number of elements :")))]
print(mylist)
i=0
newlist=[]
while i < len(mylist):
    if mylist[i] not in newlist:
        newlist.append(mylist[i])
    i+=1
print(newlist)