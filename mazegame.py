import random

def generate_solvable_maze(rows, cols):
    # Initialize the maze with all walls
    maze = [["#" for _ in range(cols)] for _ in range(rows)]

    # Stack for DFS and visited set
    stack = [(1, 1)]
    visited = set([(1, 1)])

    # Define directions (up, down, left, right) for DFS
    directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]

    # Mark the starting point and the exit as paths
    maze[1][1] = "."
    maze[rows - 2][cols - 2] = "E"  # Exit point

    # DFS to carve out a solvable path
    while stack:
        current = stack[-1]
        row, col = current

        # Find neighbors two steps away that are not visited
        neighbors = []
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 1 <= new_row < rows - 1 and 1 <= new_col < cols - 1 and (new_row, new_col) not in visited:
                neighbors.append((new_row, new_col))

        if neighbors:
            # Choose a random neighbor to move to
            next_cell = random.choice(neighbors)
            new_row, new_col = next_cell

            # Knock down the wall between the current cell and the chosen neighbor
            wall_row, wall_col = (row + new_row) // 2, (col + new_col) // 2
            maze[wall_row][wall_col] = "."

            # Mark the new cell as visited and carve the path
            visited.add(next_cell)
            maze[new_row][new_col] = "."
            stack.append(next_cell)
        else:
            stack.pop()

    return maze

def print_maze(maze, player_pos, exit_pos):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if (row, col) == player_pos:
                if (row, col) == exit_pos:
                    print("😊🚪", end=" ")  # Show both player and exit if on the same tile
                else:
                    print("😊", end=" ")  # Player's current position
            elif (row, col) == exit_pos:
                print("🚪", end=" ")  # Exit is represented by a door emoji
            else:
                print(maze[row][col], end=" ")
        print()

def is_valid_move(maze, position):
    row, col = position
    return 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != "#"

def maze_game():
    rows, cols = 15, 15  # Maze dimensions
    maze = generate_solvable_maze(rows, cols)

    # Player's starting position
    player_pos = (1, 1)
    exit_pos = (rows - 2, cols - 2)  # Exit position

    print("Welcome to the Maze Game! Your goal is to reach the '🚪' (exit).")
    print("Use W (up), S (down), A (left), and D (right) to move.\n")

    while True:
        print_maze(maze, player_pos, exit_pos)

        move = input("Enter your move (W/A/S/D): ").upper()
        row, col = player_pos

        # Process player movement
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
            if player_pos == exit_pos:
                print_maze(maze, player_pos, exit_pos)  # Show the final position with the exit
                print("Congratulations! You've reached the exit!")
                break
        else:
            print("Invalid move! You hit a wall.")

if __name__ == "__main__":
    maze_game()
