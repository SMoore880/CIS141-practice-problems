# 1. Prompt the user for a positive integer n. Use a while loop to sum all the integers from 1 up to n. Print the final sum.

n = int(input("Please enter a positive integer: "))
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print("The sum of all integers from 1 to", n, "is:", total)


# 2. Define a string variable and use a for loop to print each character on its own line. Convert each character to uppercase before printing.

my_string = "Olympic College"
for char in my_string:
    print(char.upper())
# 3. Use a for loop and the range() function to print all even numbers from 2 to 20.

for num in range(2, 21, 2):  # Start at 2, end at 20, step by 2
    print(num)
# 4. Use nested for loops to create a simple multiplication table for numbers 1 through 5.

for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()  # Newline after each row
# 5. Write a program that continuously asks the user to input a number. If the user enters 0, immediately stop asking for more numbers.

while True:
    num = int(input("Please enter a number (Enter 0 to stop): "))
    if num == 0:
        print("Now exiting...")
        break
    print("Thank you, you entered", num)
