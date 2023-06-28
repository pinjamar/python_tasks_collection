# You are going to write a program that will mark a spot with an X.
# In the starting code, you will find a variable called map.
# This map contains a nested list. When map is printed this is what the nested list looks like:
# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
# This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{row1}\n{row2}\n{row3}" to format the 3 lists to be printed as a 3 by 3 square, each on a new line.

# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']

# Your job is to write a program that allows you to mark a square on the map using a two-digit system.

# The first digit in the input will specify the column (the position on the horizontal axis).

# The second digit in the input will specify the row number (the position on the vertical axis).

# 🚨 Don't change the code below 👇
row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆
treasure = position.split(",")

if treasure[1] == "1":
    if treasure[0] == "1":
        row1[0] = " X"
    elif treasure[0] == "2":
        row1[1] = " X"
    elif treasure[0] == "3":
        row1[2] = " X"
    else:
        print("Please pick a number between 1 and 3.")
elif treasure[1] == "2":
    if treasure[0] == "1":
        row2[0] = " X"
    elif treasure[0] == "2":
        row2[1] = " X"
    elif treasure[0] == "3":
        row2[2] = " X"
    else:
        print("Please pick a number between 1 and 3.")
elif treasure[1] == "3":
    if treasure[0] == "1":
        row3[0] = " X"
    elif treasure[0] == "2":
        row3[1] = " X"
    elif treasure[0] == "3":
        row3[2] = " X"
    else:
        print("Please pick a number between 1 and 3.")
else:
    print("Please pick a number between 1 and 3.")


print(treasure)
print(f"{row1}\n{row2}\n{row3}")
