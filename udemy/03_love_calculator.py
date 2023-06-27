# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

combine_names = name1 + name2
lower_combined = combine_names.lower()

t = lower_combined.count("t")
r = lower_combined.count("r")
u = lower_combined.count("u")
e = lower_combined.count("e")

true = t + r + u + e

l = lower_combined.count("l")
o = lower_combined.count("o")
v = lower_combined.count("v")
e = lower_combined.count("e")

love = l + o + v + e

true_love = int(str(true) + str(love))

if (10 > true_love) or (true_love > 90):
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif (40 <= true_love) and (true_love <= 50):
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")
