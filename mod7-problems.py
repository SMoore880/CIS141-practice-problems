"""
#1. Write a function called count_vowels(input) that takes a string
    and returns the number of vowels (a, e, i, o, u) in it.
"""


def count_vowels(input_string):
    vowels = "aeiouAEIOU"  # Here are the vowels we're checking against.
    count = 0  # Start off with a count of zero.
    for char in input_string:  # Loop through each character in the string.
        if char in vowels:  # If the character is one of our vowels,
            count += 1  # then add one to our count.
    return count  # Give back the final count of vowels.


# Example tests:
print(count_vowels("Authoritative"))  # Expected output: 7
print(count_vowels("Radiation"))  # Expected output: 5


"""
#2. Write a function called is_palindrome(s) that checks whether a string is a
palindrome
(reads the same forward and backward, ignoring case). The function should returns
either True or False.
"""


def is_palindrome(s):
    s_lower = s.lower()  # Convert everything to lowercase so case doesn't matter.
    return s_lower == s_lower[::-1]  # Check if the string reads the same backward.


# Example tests:
print(is_palindrome("Deified"))  # Expected output: True
print(is_palindrome("Keyboard"))  # Expected output: False


"""
#3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
For example, water is very effective to fight fire.
Write a function called type_advantage(attacker, defender) that takes two Pokémon types as
strings and returns "Super Effective", "Not Very Effective", or "Neutral" based
on
simple type effectiveness rules. Your solution only needs to work for these three sets of input:
print(type_advantage("Water", "Fire"))  # "Super Effective"
print(type_advantage("Fire", "Water"))  # "Not Very Effective"
print(type_advantage("Electric", "Grass"))  # "Neutral"
"""


def type_advantage(attacker, defender):
    if attacker == "Water" and defender == "Fire":  # Water does great against Fire.
        return "Super Effective"
    elif (
        attacker == "Fire" and defender == "Water"
    ):  # Fire doesn't do well against Water.
        return "Not Very Effective"
    else:  # Anything else is considered neutral.
        return "Neutral"


# Example tests:
print(type_advantage("Water", "Fire"))  # Expected: "Super Effective"
print(type_advantage("Fire", "Water"))  # Expected: "Not Very Effective"
print(type_advantage("Electric", "Grass"))  # Expected: "Neutral"


"""
#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington State Ferry fare
based on age and whether the person has a vehicle. Assume the following rates:
* Adults (19-64): $10 without a vehicle, $20 with a vehicle.
* Seniors (65+): $5 without a vehicle, $15 with a vehicle.
* Children (0-18): Free.
"""


def ferry_fare(age, vehicle):
    if age < 19:  # Kids get to ride free.
        return 0
    elif 19 <= age <= 64:  # For adults...
        return 20 if vehicle else 10  # ...it's $20 with a vehicle, $10 without.
    elif age >= 65:  # And seniors pay less.
        return 15 if vehicle else 5  # ...$15 with a vehicle, $5 without.


# Example tests:
print(ferry_fare(30, False))  # Expected: 10 (adult without vehicle)
print(ferry_fare(30, True))  # Expected: 20 (adult with vehicle)
print(ferry_fare(70, False))  # Expected: 5  (senior without vehicle)
print(ferry_fare(70, True))  # Expected: 15 (senior with vehicle)
print(ferry_fare(10, False))  # Expected: 0  (child)


"""
#5. Write a function called level_up(experience) that takes a player's experience points
and returns their new level based on these rules:
* 0-99 XP → Level 1
* 100-199 XP → Level 2
* 200+ XP → Level 3
"""


def level_up(experience):
    if experience < 100:  # Less than 100 XP means you're level 1.
        return 1
    elif experience < 200:  # 100 to 199 XP puts you at level 2.
        return 2
    else:  # 200 or more XP, You're at level 3.
        return 3


# Example tests:
print(level_up(50))  # Expected: 1
print(level_up(150))  # Expected: 2
print(level_up(250))  # Expected: 3
