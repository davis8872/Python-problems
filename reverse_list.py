# Program to reverse a list.
mylist=[1,2,3,4,5]
i=len(mylist)
newlist=[]
while i>0:
    newlist.append(i)
    i-=1
print(newlist)