# 1. Prompt the user for a word. Then, prompt the user for how many times they'd like that word repeated. Use the skills you learned in this module to print the word the correct number of times.
word = input("Please enter a word to repeat: ")
count = int(input("How many times would you like the word repeated? "))
print(word * count)

# 2. Prompt the user for their name and their age. Calculate their age next year. Use string concatenation to print "Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
next_year_age = age + 1
print(
    "Hello, "
    + name
    + "! You are "
    + str(age)
    + " years old. Next year, you will be "
    + str(next_year_age)
    + " years old."
)

# 3. Prompt the user for a sentence and a word to try to find in that sentence. Have the program print out whether the word was found in the sentence. (i.e. True or False)
sentence = input("Please enter a sentence: ")
word_to_find = input("Please enter a word to find in the sentence: ")
print(word_to_find in sentence)

# 4. Prompt the user for: a word, a first index, and a last index. Slice the word at the indexes provided by the user and print to the screen.
word = input("Please enter a word: ")
start_index = int(input("Please enter the starting index: "))
end_index = int(input("Please enter the ending index: "))
print(word[start_index:end_index])

# 5. Print 3 words with a | character (called a pipe) in between them. Use the appropriate keyword argument in print() to do so.
word1 = input("Please enter the first word: ")
word2 = input("Please enter the second word: ")
word3 = input("Please enter the third word: ")
print(word1, word2, word3, sep="|")
