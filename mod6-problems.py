# 1. Given a list of numbers, write code to iterate through the list and calculate the sum of all even numbers. Print the resulting sum.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = 0
for num in numbers:
    if num % 2 == 0:
        even_sum += num
print("The sum of all even numbers is:", even_sum)


# 2. With a list of strings provided, write code that counts how many times the word "Olympic" appears in the list, and then print the count.

strings = ["Olympic", "College", "Olympic", "Event", "Olympic"]
olympic_count = strings.count("Olympic")
print("The word 'Olympic' appears", olympic_count, "times.")


# 3. Given a list of strings, write code to create a new list that includes only the strings longer than three characters. Print the resulting filtered list.

string_list = ["apple", "is", "a", "banana", "cat", "egg"]
filtered_list = []
for s in string_list:
    if len(s) > 3:
        filtered_list.append(s)
print("Filtered list with strings longer than three characters:", filtered_list)


# 4. For a list of integers, write code that counts how many numbers are positive and how many are negative, then print both counts.

int_list = [1, -2, 3, -4, 5, -6]
positive_count = 0
negative_count = 0
for num in int_list:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
print("Positive numbers:", positive_count)
print("Negative numbers:", negative_count)

# 5. For a list of integers, use a loop to build a new list where each element is the square of the corresponding element in the original list. Print the new list.

original_list = [1, 2, 3, 4, 5]
squared_list = []
for num in original_list:
    squared_list.append(num ** 2)
print("Squared list:", squared_list)
