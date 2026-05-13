#find if armstrong number
num = int(input("enter a number:"))
n = num 
total = 0
power = len(str(num))

while n > 0:
    digit = n % 10
    total += digit ** power
    n //= 10
if total == num:
    print("Armstrong number")
else:
    print("Not a Armstrong number")
    
