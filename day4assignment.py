print("Welcome to the Basketball Score Logger! ")

try:
    team_name = input("Enter your team name: ").strip()
    opponent_name = input("Enter opponent team name: ").strip()

    points_input = input("Enter total points scored: ").strip()
    points = int(points_input)

    enemy_points_input = input("Enter enemy total points scored: ").strip()
    enemy_points = int(enemy_points_input)

    # Validate scores
    if points < 0 or enemy_points < 0:
        print("Points cannot be negative.")
    else:
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

        # Writes to file
        with open("basketball_logs.txt", "w") as f:
            f.write("Basketball Game Log\n")
            f.write("---------------------\n")
            f.write(f"Team Name     : {team_name}\n")
            f.write(f"Opponent      : {opponent_name}\n")
            f.write(f"Points Scored : {points}\n")
            f.write(f"Enemy Points  : {enemy_points}\n")
            f.write(f"Game Result   : {result}\n")

        print("\nGame data successfully saved to file.")

        # Reopens and reads file
        print("\n--- Reading Saved Game Log ---")
        with open("basketball_logs.txt", "r") as f:
            contents = f.read()
            print(contents)

except ValueError:
    print("Please enter valid whole numbers for the scores.")

except FileNotFoundError:
    print("The file could not be found.")

except PermissionError:
    print("Permission denied while accessing the file.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")