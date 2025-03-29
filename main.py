while True:
    num_of_players = input("Select the number of players [2-4]: ")
    if num_of_players.isdigit():
        num_of_players = int(num_of_players)
        if 2 <= num_of_players <= 4:
            break
        else:
            print("Must be between 2-4 players.")
    else:
        print("Invalid value, try again.")

points = [0 for _ in range(num_of_players)]