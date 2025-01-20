import math
# 1. Create a program that prints the following output to the screen: "Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked."
print("Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked.")

# 2. Create a program that prompts for 2 numbers and then outputs the addition, subtraction, multiplication, and division of the first number by the second number.
    # Number inputs
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
    # Number outputs
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula.
    # Sides of the pyramid
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
    # sum and area
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print(f"The area of the triangle is: {area}")

# 4. Create a program that computes different statistics given five numbers including the total, average, minimum, maximum, range, and standard deviation
numbers = []
for i in range(5):
    numbers.append(float(input("Enter a number: ")))
total = sum(numbers)
average = total / 5
minimum = min(numbers)
maximum = max(numbers)
range_value = maximum - minimum
std_deviation = math.sqrt(sum((x - average) ** 2 for x in numbers) / 5)
print("Total:", total)
print("Average:", average)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Range:", range_value)
print("Standard Deviation:", std_deviation)
