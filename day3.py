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

# Variables

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
