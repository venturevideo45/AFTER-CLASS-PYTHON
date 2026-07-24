num = int(input("Enter a number: "))
#  Power of 2 Check
print("Power of 2 check:")
for x in [num]:
    result = x > 0 and (x & (x - 1)) == 0 
    print(" ", x, "->", bin(x), "->", result)
print()