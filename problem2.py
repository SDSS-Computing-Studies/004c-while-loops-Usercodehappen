#! python3
"""
Have the user enter a number.
Display the multiples of that number, up to 12 times that number:
All numbers should be on the same line.
(2 marks)

inputs:
int number

outputs:
multiples of that number on one line

example:
Enter a number: 4
4 8 12 16 20 24 28 32 36 40 44 48
"""
x =""
number = (input("Enter an integer")).strip()
count = 0
while count <= 12:
    print(x,end=""+" ")
    x = int(number)*(count + 1)
    count = count + 1
    if count > 12:
        break