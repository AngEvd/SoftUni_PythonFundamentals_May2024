def main():
    """
    Main function to solve the maze problem. It reads the maze configuration from input,
    finds the start position, and attempts to traverse the maze to find the longest path
    to the exit.

    """
    maze_rows = int(input())

    maze = []
    visited = set()  # keeps visited places to avoid cycles
    moves = 1  # if starting position is on the edge needs 1 move to get out
    longest_path = 0  # counter for the longest path out so far

    for i in range(maze_rows):
        maze.append([char for char in input()])

    start = find_start(maze, maze_rows)
    visited.add(start)
    result = traverse_maze(maze, start, visited, moves, longest_path)
    print(f"Kate got out in {result} moves" if result else "Kate cannot get out")


def find_start(maze: list, rows: int) -> tuple:
    """
    Finds the starting position "k" in the maze

    :param maze: The maze represented as a list of lists of characters
    :param rows: The integer number of rows in the maze
    :return: The (row, column) position of the start
    """
    for i in range(rows):
        for j in range(len(maze[i])):
            if maze[i][j] == "k":
                return i, j


def is_valid(row: int, col: int, maze: list) -> bool:
    """
    Checks if a position is valid for movement.

    :param row: The row index of the position.
    :param col: The column index of the position.
    :param maze: The maze represented as a list of lists of characters.
    :return: True if the position is valid for movement, False otherwise.
    """
    return 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == " "


def is_exit(row: int, col: int, maze: list) -> bool:
    """
    Checks if a position is at the exit of the maze.

    :param row: The row index of the position.
    :param col: The column index of the position.
    :param maze: The maze represented as a list of lists of characters.
    :return: True if the position is at the exit, False otherwise.
    """
    return row == len(maze) - 1 or col == len(maze[0]) - 1 or row == 0 or col == 0


def traverse_maze(maze: list, current_position: tuple, visited: set, moves: int, longest_path: int) -> int:
    """
    Traverses the maze recursively to find the longest path to an exit.

    :param maze: The maze represented as a list of lists of characters.
    :param current_position: The current (row, column) position in the maze.
    :param visited: A set of visited positions to avoid cycles.
    :param moves: The current number of moves made.
    :param longest_path: The longest path found so far.
    :return: The length of the longest path to an exit if found, otherwise 0.
    """
    current_row, current_col = current_position
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    if is_exit(current_row, current_col, maze) and moves > longest_path:
        longest_path = moves

    for direction in directions:
        new_row = current_row + direction[0]
        new_col = current_col + direction[1]
        new_position = (new_row, new_col)

        if is_valid(new_row, new_col, maze) and new_position not in visited:
            visited.add(new_position)
            result = traverse_maze(maze, new_position, visited, moves + 1, longest_path)
            visited.remove(new_position)
            if result is not None:
                longest_path = max(result, longest_path)
    return longest_path


if __name__ == '__main__':
    main()
