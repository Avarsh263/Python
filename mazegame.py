def print_maze(maze, player_pos):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if (row, col) == player_pos:
                print("P", end=" ")  # Player position
            else:
                print(maze[row][col], end=" ")
        print()

def is_valid_move(maze, position):
    row, col = position
    if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != "#":
        return True
    return False

def maze_game():
    # Simple Maze Layout (P = Player, E = Exit, # = Wall, . = Path)
    maze = [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', '.', '#', '.', '.', '#'],
        ['#', '.', '#', '.', '#', '.', '#', '#'],
        ['#', '.', '#', '.', '.', '.', '.', '#'],
        ['#', '.', '#', '#', '#', '#', '.', '#'],
        ['#', '.', '.', 'E', '#', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#']
    ]

    # Player's starting position
    player_pos = (1, 1)
    
    print("Welcome to the Maze Game! Your goal is to reach the 'E' (exit).")
    print("Use W (up), S (down), A (left), and D (right) to move.\n")
    
    while True:
        print_maze(maze, player_pos)
        
        move = input("Enter your move (W/A/S/D): ").upper()
        row, col = player_pos
        
        if move == 'W':  # Move up
            new_pos = (row - 1, col)
        elif move == 'S':  # Move down
            new_pos = (row + 1, col)
        elif move == 'A':  # Move left
            new_pos = (row, col - 1)
        elif move == 'D':  # Move right
            new_pos = (row, col + 1)
        else:
            print("Invalid move! Use W, A, S, or D to move.")
            continue

        # Check if the move is valid (not hitting walls)
        if is_valid_move(maze, new_pos):
            player_pos = new_pos
            
            # Check if the player reached the exit
            if maze[player_pos[0]][player_pos[1]] == 'E':
                print("Congratulations! You've reached the exit!")
                break
        else:
            print("Invalid move! You hit a wall.")

if __name__ == "__main__":
    maze_game()
