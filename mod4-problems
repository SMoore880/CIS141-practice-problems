# A | B | (A AND B) OR (NOT B)
# ----------------------------
# True | True | True
# True | False| True
# False| True | False
# False| False| True

#Sensor threshold
sensor_threshold = float(input("Please enter the sensor threshold: "))
if sensor_threshold < 8:
    print("Headlights On")
else:
    print("Headlights Off")

#3. Bank balance check
balance = float(input("Hello valued patron, please enter your bank balance: "))
print(balance < 100)

#4. Movie restrictions
age = int(input("Please enter your age: "))
if age < 13:
    print("You are old enough to see G rated movies.")
elif age < 18:
    print("You are old enough to see PG-13 rated movies.")
else:
    print("You are old enough to see R rated movies.")

#5. Order total with shipping charge
order_total = float(input("Please enter your order total: "))
if order_total < 50:
    total_cost = order_total + 5
    print("Total cost: $" + str(total_cost))
else:
    print("Total cost: $" + str(order_total))
    print("You have free shipping!")
