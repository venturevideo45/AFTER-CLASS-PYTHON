numlarg = int(input("Enter the larger number: "))
numsmall = int(input("Enter the smaller number: "))
a = numlarg
b = numsmall
while(numsmall):
    numstore = numsmall
    numsmall = numlarg % numsmall
    numlarg = numstore

print("The HCF is", numlarg)

LCM = (a * b) // numlarg
print("The LCM is", LCM)