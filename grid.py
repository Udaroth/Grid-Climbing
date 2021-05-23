"""
Climbing Grid
==============

Your task is to implement the function, that given an "n" x "m" climbing grid,
find the maximum score such that your total summed energy cost is under some
budget B.

Your constraints:
    * Your budget B is an integer, and your path must result in a cost less
      than or equal to B.
    * You may only move RIGHT and UP in direction along the grid to form a
      path.
    * Optimise the maximum score gained.
    * You _MUST_ start from the bottom left vertex.

=== Example ===

Budget = 10
Cost Right = 3
Cost up = 2

Grid:
    1 1 2
    1 2 2
    1 2 1

Path for maximum reward:

        2
      2 2
    1 2

Return: 9
"""

from typing import List


def max_score(
        height: int,
        width: int,
        grid: List[List[int]],
        cost_right: int,
        cost_up: int,
        budget: int) -> int:
    """
    Get the max score by traversing the `grid`.

    ***IMPORTANT NOTE***: Your GRID is represented in coordinates, so:
    grid[0][0] is the bottom, leftmost vertex, and
    grid[height-1][width-1] is the top, rightmost.

    Example: The Grid

    1 2 3
    4 5 6
    7 8 9

    Is represented as

    grid = [
      [7, 8, 9],
      [4, 5, 6],
      [1, 2, 3]
    ]

    so grid[0][0] == 7 and grid[3-1][3-1] == 3.

    :param cost_up - the cost of moving upwards
    :param cost_right - the cost of moving right
    :param height - the height of the grid (n)
    :param width - the width of the grid (m)
    :param grid - The nxm matrix of vertices.
    :param budget - The maximum budget you can use.
    :returns The maximum score obtained by your path.
    """
    # TODO implement me please

    score = [[-1]*width]*height

    for h in range(height):
        for w in range(width):

            # Base Case
            if w == 0 and h == 0:
                # We are at the origin, we return the score of this square
                score[0][0] = grid[0][0]

            # Case 1: We cannot reach the this square with our budget
            elif budget < (cost_right*(w) + cost_up*(h)):
                # If we are still on the first row
                if h == 0:
                    # we'll return the solution left of it because that should've been initialised.
                    score[h][w] = score[h][w-1]
                # else if there's a square that we can't reach on the left most column
                elif w == 0:
                    # Then it's score is given by the square beneath it which should have been initialised.
                    score[h][w] = score[h-1][w]
                # Otherwise if its not on either edge, the optimal solutino of this square is given by
                else:
                    # Square not on the left edge or bottom edge, the optimal solution is given by the max of optimal solution left of or beneath it.
                    # Those squares should always be initialised
                    score[h][w] = max(score[h-1][w], score[h][w-1])
            # Case 2: We can reach it with our budget, but the square is on the left most column; the optimal solution is given by its score plus the optimal solution beneath it
            elif w == 0: 
                score[h][w] = grid[h][w] + score[h-1][w]
            # Case 3: We can reach it with our budget, but the square is on the bottom most row, the optimal solution is given by its score plus the optimal solutino left of it
            elif h == 0:
                score[h][w] = grid[h][w] + score[h][w-1]
            # Caes 4: We can reach it with our budget, and the square has both left and bottom neighbours
            else:
                # Optimal score is given by score of current square plus optimal of bottom or optimal of left.
                score[h][w] = max(
                grid[h][w] + score[h][w-1], 
                grid[h][w] + score[h-1][w]
                )
    

    return score[height-1][width-1]

