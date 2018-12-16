n=input()
k=n.split(" ")
sum_=0
for a in k:
    sum_=sum_+int(a)
print (sum_)

#----------rec-----------------------
def sum_(ilist):
    if len(ilist)==0:
        return 0
    else:
        return (ilist[0]) + (sum_(ilist[1:]))
n=input() 
slist=n.split(" ")
k=list(map(int,slist))
print(sum_(k))
#-------------while-----------------
n=input()
k=n.split(" ")
sum_=0
i=0
while i<len(k):
    sum_=sum_+int(k[i])
    i+=1
print(sum_)
