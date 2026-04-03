#1. Check if number is zero or non-zero
num = int(input())
if num == 0:
    print("The number is zero")
else:
    print("The number is non zero")

#2. Check if number is +ve or -ve
num = int(input())
if num > 0:
    print("The number is +ve number")
else:
    print("The number is -ve number")

#3. Check if number is even or odd
num = int(input())
if num%2 == 0:
    print("The number is an even number")
else:
    print("The number is an odd number")

#4. Check if a person is eligible to vote or not
num = int(input())
if num >= 18:
    print("The person is eligible to vote")
else:
    print("The person is a minor")

#5. Check if number is divisible by 3 or not
num = int(input())
if num % 3 ==0:
    print("The number is divisible by 3")
else:
    print("The number is not divisible by 3")

#6. Check if number is divisible by 3 and 5 or not
num = int(input())
if num % 3==0 and num % 5==0:
    print("The number is divisible by 3 and 5")
elif num % 3==0:
    print("The number is only divisible by 3")
elif num % 5==0:
    print("The number is only divisible by 5")
else:
    print("The number is not divisible by 3 and 5")

#7. Find biggest number amogst two numbers
num_1 = int(input())
num_2 = int(input())
if num_1 > num_2:
    print("Num 1 is the bigger number")
elif num_1 < num_2:
    print("Num 2 is the bigger number")
else:
    print("Both are equal numbers")
