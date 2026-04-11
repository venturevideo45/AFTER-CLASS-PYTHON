x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))

print("Before swapping:")
print("x =", x)
print("y =", y)
print("z =", z)

print("After swapping:")

if x > y and x > z  and y > z:
    print("ORDER: x > y > z")
elif x > y and x > z and z > y:
    print("ORDER: x > z > y")    
elif y > x and y > z and x > z:
    print("ORDER: y > x > z")
elif y > x and y > z and z > x:
    print("ORDER: y > z > x")
elif z > x and z > y and x > y:
    print("ORDER: z > x > y")
elif z > x and z > y and y > x:
    print("ORDER: z > y > x")

elif x == y == z:
    print("All numbers are equal.")

else:
    print("ERROR: Invalid input or numbers are not distinct.")
