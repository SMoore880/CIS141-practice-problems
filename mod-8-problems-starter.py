"""
#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to it.
    Write a Python script that reads a file gardening_tips.txt and prints
    out each tip one by one.
"""

#1 - Gardening Tips
print("\n=== Gardening Tips ===")

# Create gardening_tips.txt with at least 3 tips
with open("gardening_tips.txt", "w") as file:
    file.write("Water your plants early in the morning.\n")
    file.write("Use compost to enrich the soil.\n")
    file.write("Rotate your crops each season.\n")

# Read and print each tip one by one
with open("gardening_tips.txt", "r") as file:
    for line in file:
        print(line.strip())


"""
#2. Write a Python program that allows users to log their hiking trips. The program should:
    - Use a while loop to repeatedly ask for a hike name and distance in miles
    - Save each entry to hiking_log.txt (each hike on a new line)
    - When the user presses 0, exit the loop & print the contents of hiking_log.txt
"""

#2 - Hiking Log
print("\n=== Hiking Log ===")
print("Enter 0 to stop logging hikes.")

# Open the file in append mode so it keeps previous entries
with open("hiking_log.txt", "a") as file:
    while True:
        # Ask for hike name
        hike_name = input("Enter the name of the hike (or 0 to exit): ")
        if hike_name == "0":
            break

        # Ask for hike distance
        distance = input("Enter the distance in miles: ")
        if distance == "0":
            break

        # Write the entry to the file
        file.write(f"{hike_name}: {distance} miles\n")
        print("Hike logged!\n")

# Display the log
print("\nYour Hiking Log:")
with open("hiking_log.txt", "r") as file:
    for line in file:
        print(line.strip())


"""
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into it. Write a Python program that:
    - Reads the file
    - Requests 5 inputs from the user: 5 words the user would like to count the frequency of
    - Counts how many times each word appears
    - Creates a dictionary of the words and their counts
    - Print the dictionary to the console
"""

#3 - Song Lyrics Word Count
print("\n=== Song Lyrics Word Count ===")

# Read the lyrics file
with open("song_lyrics.txt", "r") as file:
    lyrics = file.read().lower()

# Clean up the lyrics by removing punctuation
import string

cleaned_lyrics = lyrics.translate(str.maketrans("", "", string.punctuation))

# Ask for 5 words to count
words_to_count = []
print("Enter 5 words to count in the song lyrics:")
for i in range(5):
    word = input(f"Word {i+1}: ").lower()
    words_to_count.append(word)

# Count the words and store in a dictionary
word_count = {}
for word in words_to_count:
    count = cleaned_lyrics.split().count(word)
    word_count[word] = count

# Display the word count
print("\nWord Count:")
print(word_count)


"""
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated by commas.
    Write a program that reads the poll.txt file
    Count how many votes "yea" or "nay" received and print the results.
"""

#4 - Vote Counting
print("\n=== Vote Count ===")

# Read the poll file
with open("poll.txt", "r") as file:
    votes = file.read().split(",")

# Count the votes
vote_count = {"yea": votes.count("yea"), "nay": votes.count("nay")}

# Display the results
print("Vote Count Results:")
print(f"Yea: {vote_count['yea']}")
print(f"Nay: {vote_count['nay']}")
