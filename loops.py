n=int(input("Enter the number of times you want the sum:"))
sum=0

for i in range(1,n+1):
    sum=sum+i
    print("/nSum=",sum)


#activity 2

string=input("Enter a string:")

string2=('')
for i in string:
    string2=i+string2

print("Original string is",string)
print("Reversed string is",string2)


#activity 3

n=int(input("Enter the value of n;"))

print("Numbers from {0} to {1} are:".format(n,1))

#start,stop,step
for i in range(n,0,-1):
    print(i)