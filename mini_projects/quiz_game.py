print("Welcome to my computer quiz!")

playing = input("Do you want to play?")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play:)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central unit":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics unit":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random memory":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("You got " + str(score) + " questions correct!")
