import unittest
from main import Connect4


class TestWinConditions(unittest.TestCase):

    def setUp(self):
        self.game = Connect4()

    def test_horizontal_win(self):
        self.game.board[5] = ['X', 'X', 'X', 'X', ' ', ' ', ' ']
        self.assertTrue(self.game.check_win('X'))

    def test_vertical_win(self):
        for row in range(2, 6):
            self.game.board[row][0] = 'X'
        self.assertTrue(self.game.check_win('X'))

    def test_diagonal_win_down_right(self):
        for i in range(4):
            self.game.board[i][i] = 'X'
        self.assertTrue(self.game.check_win('X'))

    def test_diagonal_win_up_right(self):
        for i in range(4):
            self.game.board[5 - i][i] = 'X'
        self.assertTrue(self.game.check_win('X'))

    def test_no_win(self):
        self.game.board[5][0] = 'X'
        self.game.board[5][2] = 'X'
        self.game.board[5][4] = 'X'
        self.assertFalse(self.game.check_win('X'))


class TestDropChip(unittest.TestCase):

    def setUp(self):
        self.game = Connect4()

    def test_successful_drop(self):
        result = self.game.drop_chip(1)
        self.assertTrue(result)
        self.assertEqual(self.game.board[5][0], 'X')

    def test_full_column_returns_false(self):
        for row in range(6):
            self.game.board[row][0] = 'X'
        self.assertFalse(self.game.drop_chip(1))

    def test_invalid_column_too_low(self):
        self.assertFalse(self.game.drop_chip(0))

    def test_invalid_column_too_high(self):
        self.assertFalse(self.game.drop_chip(8))

    def test_full_board(self):
        for row in range(6):
            for col in range(7):
                self.game.board[row][col] = 'X'
        self.assertFalse(self.game.drop_chip(1))
        self.assertTrue(self.game.is_full())


if __name__ == '__main__':
    unittest.main(verbosity=2)



#
# TestWinConditions:
#   test_horizontal_win .............. PASS
#   test_vertical_win ................ PASS
#   test_diagonal_win_down_right ..... PASS
#   test_diagonal_win_up_right ....... PASS
#   test_no_win ...................... PASS
#

#
# Bugs/Issues: None. All methods behaved correctly under all test conditions.
