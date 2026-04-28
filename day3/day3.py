""" 
x = [1, 2, 3]
y = x
x.append(4)

print("x:", x)
print("y:", y) """

# lists are mutable #

""" test1 = 85
test1 = test1 + 5
print(test1) """

# area

""" rectangle_length = 7
rectangle_width = rectangle_length - 1
rectangle_area = rectangle_length * rectangle_width
print(rectangle_area)
 """
""" 
a = [10, 20]
b = a
b[0] = 99
print(a) """

## python indices start at 0

""" # Variables

player1 = "Yusei"
player2 = "Jack"
lifepoint1 = 8000
lifepoint2 = 8000

# constant 

Junk_Synchron_Level = 3
Tuner_Level = 3
Junk_Warrior_ATK = 2300

print("Duelist 1: ", player1)
print("Duelist 2: ", player2)
print("Duelist 1 Life Points: ", lifepoint1)
print("Duelist 2 Life Points: ", lifepoint2)

# Synchro Summoning

Synchro_Monster_Level = Junk_Synchron_Level + Tuner_Level

# Synchro Summon Logic 

if Junk_Synchron_Level == Tuner_Level:
    Junk_Warrior_Level = Synchro_Monster_Level
    Synchro_Monster_Level = 0
    lifepoint2 = lifepoint2 - Junk_Warrior_ATK

print("Yusei: Junk Warrior is summoned as a level", Junk_Warrior_Level, "monster.")
print("Yusei: Junk Warrior directly attacks!")
print("Enemy Life Points:", lifepoint2)
print("Yusei: I end my turn.")

print("=== Conditional Logic Playground ===")
"""

# Simple if
score = 85
if score >= 70:
    print("Passing grade")

# If-else
age = 16
if age >= 18:
    print("Adult")
else:
    print("Minor")

# Nested conditionals
grade = 92
if grade >= 90:
    print("A range")
    if grade >= 95:
        print("High A")
    else:
        print("Low A")

# Multi-way selection
temp = 72
if temp > 90:
    print("Hot")
elif temp > 70:
    print("Warm")
elif temp > 50:
    print("Cool")
else:
    print("Cold")

# Boolean logic
x = 12
if x > 5 and x < 20:
    print("In range")

# Logical errors demonstration
value = 10
if value == 10:
    print("Correct comparison")

# Tracing example
n = 3
if n >= 5:
    print("High")
elif n >= 3:
    print("Mid")
else:
    print("Low")

print("\nTry changing values and adding new conditions.")

def one_turn_duel():
    rule = str(input("Do you want to play with 4000 or 8000 life points? "))
    while rule != "4000" or "8000":
        rule = 