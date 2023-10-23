# Ryland Price
# CS1400 - MWF 8:30

import drawly, math
from drawly import circle, draw, set_color

input("Press Enter to create your Super Hero ")
print()
print("Please enter the parameters for your superhero: ")
print()

# Get user input for superhero parameters
hero_name = input("Super Hero Name: ")
hero_body_size = int(input("Body Size: "))
hero_x_location = int(input("X Location (0-1000): "))
hero_y_location = int(input("Y Location (0-600): "))
arm_length = int(input("Arm Length: "))
leg_length = int(input("Leg Length: "))
if leg_length < arm_length:
    leg_length = int(input("Input invalid, please enter a leg length longer than the arm length: "))
sword_length = int(input("Sword Length: "))
if arm_length + sword_length < leg_length:
    sword_length = int(input("Input invalid, please enter a sword length such that the arm plus sword length is longer than the leg length: "))
voice_power = int(input("Voice Power: "))
if voice_power < arm_length + sword_length:
    voice_power = int(input("Input invalid, please enter a Voice Power such that it is greater than the arm plus sword length: "))

print()

# print superhero welcome message and instructions for villain input
print("Welcome mighty " + hero_name + "!")

print()

print("Please enter the parameters for your villain: ")

# Collect input for villain
villain_name = input("Villain Name: ")
villain_body_size = int(input("Body Size: "))
villain_x_location = int(input("X Location (0-1000): "))
villain_y_location = int(input("Y Location (0-600): "))

# Print Villain mean welcome message
print("Prepare to be destroyed " + villain_name + "!")

print()

input("Hit Enter to help " + hero_name + " fight " + villain_name)

# Start drawly and name window
drawly.start(hero_name + " vs " + villain_name, (1000, 600), "Grey")
drawly.set_speed(2)

# Draw superhero and villain location
set_color("Blue")
circle(hero_x_location, hero_y_location, round(hero_body_size / 2), 0)

set_color("Red")
circle(villain_x_location, villain_y_location, round(villain_body_size / 2), 0)

draw()

# Draw rings for distance of each ability and create variables for attack range
punch = int(round(hero_body_size / 2)) + arm_length
kick = int(round(hero_body_size / 2)) + leg_length
blade = punch + sword_length

set_color("orange")
circle(hero_x_location, hero_y_location, punch, 3)
draw()

set_color("purple")
circle(hero_x_location, hero_y_location, kick, 3)
draw()

set_color("Yellow")
circle(hero_x_location, hero_y_location, blade, 3)
draw()

set_color("Green")
circle(hero_x_location, hero_y_location, voice_power, 3)
draw()

drawly.done()

# Create if, elif, and else statements to tell superhero what to do
hero_villain_dist = math.sqrt((hero_x_location - villain_x_location) ** 2 + (hero_y_location - villain_y_location) ** 2) - villain_body_size / 2
if hero_villain_dist <= punch:
    print("Use your flaming punch ability!")
elif hero_villain_dist <= kick:
    print("Use your stunning Kick!")
elif hero_villain_dist <= blade:
    print("Use your Sword of Maglidor!")
elif hero_villain_dist <= voice_power:
    print("Use your Voice of Immobilization!")
else:
    print(villain_name + " is running scared, chase after them!")

# Thank you statement
print()
print("Thanks For Playing!")