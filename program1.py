'''

name=input("What is your name? ")
age=int(input("How old are you? "))
print(f"Hello {name} !! Your are {age} years old.")
print(f"Next Year you will be {age+1} !!")

number=int(input("Enter a number"))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")


'''

'''
Calculator program
'''

'''
number1=int(input("Enter thr First Number- "))
number2=int(input("Enter the Second Number- "))

print(f"Addition: {number1+number2}")
print(f"Subtraction: {number1-number2}")
print(f"Multiplication: {number1*number2}")

if number2 == 0:
    print("Division is not possible. Number2 is zero.")
else:
    print(f"Division: {number1/number2}")
'''

''' Grade Program '''
'''
marks=input("Enter the Marks - ")

if not(marks.isdigit()):
    print("Invalid marks. please enter number only")
else:
    marks=int(marks)

    if marks > 100 or marks < 0:
        print("Invalid marks Entered.")
    elif marks >= 90:
        print("Grade A")
    elif marks >= 80:
        print("Grade B")
    elif marks >= 50:
        print("Grade C")
    else:
        print("FAIL")

'''

'''
Loop
'''

'''
n=int(input("Enter a Number: "))

total = 0

for i in range(1,n+1):
    total = total + i

print(f"sum = {total}")
'''

''' string looping'''

'''
word=input("Enter a word: ")
totalVowels=0
for ch in word:
    if ch.lower() in "aeiou":
        totalVowels=totalVowels+1
    
print(f"TotalVowel is {totalVowels}")
'''

'''Largest of three numbers'''
'''
number1=int(input("Enter First number:"))
number2=int(input("Enter Second number:"))
number3=int(input("Enter Third number:"))

if number1> number2 and number1> number3:
    print(f"Number1 {number1} is the largest number")
elif number2> number1 and number2> number3:
    print(f"Number2 {number2} is the largest number")
else:
    print(f"Number3 {number3} is the largest number")
'''

'''Password Checker '''
