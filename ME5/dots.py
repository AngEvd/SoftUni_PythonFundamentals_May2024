def main():
    """
    Reads the number of rows and the matrix content from the user, and then
    prints the length of the longest chain of connected dots and the matrix.
    """
    rows = int(input())
    matrix = [input().split() for _ in range(rows)]

    visited = set()

    print(count_connected_dots(matrix, visited))


def count_connected_dots(graph: list, visited: set) -> int:
    """
    Counts the maximum chain of connected dots (".") in the given graph.
    :param graph: A 2D list representing the matrix of characters.
    :param visited: A set to keep track of visited coordinates.
    :return: The length of the longest chain of connected dots.
    """
    max_chain_length = 0
    for row in range(len(graph)):
        for col in range(len(graph[0])):
            if graph[row][col] == ".":
                current_chain_length = count_neighbours(graph, row, col, visited)
                max_chain_length = max(current_chain_length, max_chain_length)
    return max_chain_length


def count_neighbours(graph: list, row: int, col: int, visited: set) -> int:
    """
    Recursively counts the number of connected dots starting from a given position.

    :param graph: A 2D list representing the matrix of characters.
    :param row: The row index of the current position.
    :param col: The column index of the current position.
    :param visited: A set to keep track of visited coordinates.
    :return: The count of connected dots from the current position.
    """
    if not is_valid(row, col, graph):
        return 0

    if any([graph[row][col] == "-", (row, col) in visited]):
        return 0

    count = 1
    visited.add((row, col))

    for neighbour in get_neighbours(row, col):
        count += count_neighbours(graph, neighbour[0], neighbour[1], visited)

    return count


def get_neighbours(row: int, col: int):
    """
    Gets the neighboring cells of a given position.
    :param row: The row index of the current position.
    :param col: The column index of the current position.
    :return: A list of tuples representing the coordinates of the neighboring cells.
    """
    neighbours = ((row - 1, col),
                  (row + 1, col),
                  (row, col - 1),
                  (row, col + 1)
                  )
    return neighbours


def is_valid(row: int, col: int, graph: list) -> bool:
    """
    Checks if a given cell is within the bounds of the graph.
    :param row: The row index of the current position.
    :param col: The column index of the current position.
    :param graph: A 2D list representing the matrix of characters.
    :return: True if the position is within bounds, False otherwise.
    """
    return all([row >= 0, col >= 0, row < len(graph), col < len(graph[0])])


if __name__ == '__main__':
    main()
