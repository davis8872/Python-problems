# Program to sort a list using while loop.
mylist=[2,4,1,5,6]
print(mylist)
n=len(mylist)
i=0
swapped=True
while True:
    swapped=False
    while i < n-1:
        if mylist[i] > mylist[i+1]:
            mylist[i],mylist[i+1] = mylist[i+1],mylist[i]
            swapped=True
        i+=1
    
print(mylist)