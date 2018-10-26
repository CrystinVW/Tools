from __future__ import print_function
import unittest


def __init__(self, init=None):
    self.__queens = 8

def print_board(solution):
    length = len(solution)
    print("for:", length)
    print('-' * length)

    if solution == []:
        print("no solution found")
    else:
        for i in range(length):
            for j in range(length):
                if (i, j) in solution:
                    print("Q", end="")
                else:
                    print(".", end="")
            print()

    print('-' * length)


def safe(one, two):
    one_x, one_y = one
    two_x, two_y = two
    return not (one_x == two_x or one_y == two_y or abs(two_x - one_x) == abs(two_y - one_y))

def solve_queens(row, placed, size):
    if row == size:
        print_board(placed)
    answer = []
    for column in range(size):

        new_queen = (row, column)
        good = True
        for queen in placed:
            good &= safe(queen, new_queen)
        if good:
            answer.append(new_queen)
            placed.append(new_queen)
            if not solve_queens(row + 1, placed, size):
                placed.pop(-1)
                answer.pop(-1)
            else:
                return True

    return False


			#check all queens with the queens in placed
			#and compare together
				#check the location of queens and compare to new location of all queens (row,column)

#create a loop with a boolean object, with old queens to the new queens and and to
	#def _solve(row, placed, size)
	#solve_queeens(0,[],8)
	#def solve(size)
		#_solve(0,[],size)

'''
    solve_queens(row)
        if the row is greater than the size of the board, we're done

        go through the columns in this row
            go through all the already placed queens and see if
                placing a new queen at (row, column) is safe

            if it is
                place it at (row, column)
                if not solve_queens(row+1)
                    remove row and column
    '''

class test_solve_queens(unittest.TestCase):

    def test_one_queen(self):
        self.assertFalse(solve_queens(0, [], 1), [(0, 0)])
    def test_two_queens(self):
        self.assertEquals(solve_queens(0, [], 2), 0)
    def test_three_queens(self):
        self.assertEquals(solve_queens(0, [], 3), 0)
    def test_four_queens(self):
        self.assertFalse(solve_queens(0, [], 4), [(0, 1), (1, 3), (2, 0), (3, 2)])
        #self.assertEquals(print_board(solve_queens(0, [], 4), 2)
    def test_eight_queens(self):
        self.assertFalse(solve_queens(0, [], 8), [(0, 1), (1, 4), (2, 7), (3, 5), (4, 2), (5, 6), (6, 1), (7, 3)])
        #a = solve_queens(0, [], 8)
        #self.assertEquals(print_board(a), 92)
    def test_empty(self):
        solve_queens(0, [], 0)
        self.assertEquals(solve_queens(0, [], 0), 0)
    def test_safe(self):
        self.assertFalse(solve_queens(0, [], 2), (0, 0))
    def test_print_board(self):
        self.assertEquals(print_board([(0, 1), (1, 3), (2, 0), (3, 2)]), None)

if __name__ == '__main__':
    #solution = [(0, 1), (1, 3), (2, 0), (3, 2)]
    #print_board(solution)
    solve_queens(0, [], 3)
    unittest.main()
