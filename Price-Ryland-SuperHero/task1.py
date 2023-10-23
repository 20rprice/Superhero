# Ryland Price
# CS1400 - MWF 8:30

import random

# Print welcome message
print("Welcome to the Guessing Game")

comp_var = random.randint(1, 10)

print("The Computer has picked a number from 1-10. Try to match it.")

user_var = int(input("What number do you choose (1-10): "))

print("You picked " + str(user_var) + ", and the actual number was " + str(comp_var))

off_by = abs(comp_var - user_var)

if off_by == 0:
    print("Honored to play with you, True Aggie.")
elif off_by == 1:
    print("You are a worthy opponent, Big Blue.")
elif off_by == 2:
    print("You have much to learn, Hurd.")
elif off_by == 3:
    print("Little Blue, your time will come.")
else:
    print("Keep working hard on the Quad.")
