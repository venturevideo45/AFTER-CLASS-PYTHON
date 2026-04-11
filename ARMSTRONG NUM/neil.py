num = int(input("Enter a number: "))


original_num = num


num_digits = 0
temp = num
while temp > 0:
    num_digits += 1
    temp //= 10


total_sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    
    power_val = 1
    for _ in range(num_digits):
        power_val *= digit
        
    total_sum += power_val
    temp //= 10


if original_num == total_sum:
    print(original_num, "is an Armstrong number.")
else:
    print(original_num, "is not an Armstrong number.")
