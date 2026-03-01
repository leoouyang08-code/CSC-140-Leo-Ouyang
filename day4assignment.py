print("Welcome to the Basketball Score Logger! ")

# Name inputs outside of try block
team_name = input("Enter your team name: ").strip()
opponent_name = input("Enter opponent team name: ").strip()

# Validate your team points
while True:
    try:
        points_input = input("Enter total points scored: ").strip()
        points = int(points_input)

        if points < 0:
            print("Points cannot be negative.")
        else:
            break
    except ValueError:
        print("Please enter a valid whole number.")

# Validate enemy points
while True:
    try:
        enemy_points_input = input("Enter enemy total points scored: ").strip()
        enemy_points = int(enemy_points_input)

        if enemy_points < 0:
            print("Points cannot be negative.")
        else:
            break
    except ValueError:
        print("Please enter a valid whole number.")

try:
    print("\n--- Game Summary ---")
    print(f"Team Name     : {team_name}")
    print(f"Opponent      : {opponent_name}")
    print(f"Points Scored : {points}")
    print(f"Enemy Points  : {enemy_points}")

    # Determine result
    if points > enemy_points:
        result = "Win"
    elif points < enemy_points:
        result = "Loss"
    else:
        result = "Tie"

    print(f"Game Result   : {result}")

    # Write to file
    with open("basketball_logs.txt", "w") as f:
        f.write("Basketball Game Log\n")
        f.write("---------------------\n")
        f.write(f"Team Name     : {team_name}\n")
        f.write(f"Opponent      : {opponent_name}\n")
        f.write(f"Points Scored : {points}\n")
        f.write(f"Enemy Points  : {enemy_points}\n")
        f.write(f"Game Result   : {result}\n")

    print("\nGame data successfully saved to file.")

    # Reopen and read file
    print("\n--- Reading Saved Game Log ---")
    with open("basketball_logs.txt", "r") as f:
        contents = f.read()
        print(contents)

except FileNotFoundError:
    print("The file could not be found.")

except PermissionError:
    print("Perms denied buddy.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")