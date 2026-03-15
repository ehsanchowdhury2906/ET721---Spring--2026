import pytest
from main import Connect4


@pytest.fixture
def game():
    return Connect4()



def test_horizontal_win(game):
    game.board[5] = ['X', 'X', 'X', 'X', ' ', ' ', ' ']
    assert game.check_win('X') is True

def test_vertical_win(game):
    for row in range(2, 6):
        game.board[row][0] = 'X'
    assert game.check_win('X') is True

def test_diagonal_win_down_right(game):
    for i in range(4):
        game.board[i][i] = 'X'
    assert game.check_win('X') is True

def test_diagonal_win_up_right(game):
    for i in range(4):
        game.board[5 - i][i] = 'X'
    assert game.check_win('X') is True

def test_no_win(game):
    game.board[5][0] = 'X'
    game.board[5][2] = 'X'
    game.board[5][4] = 'X'
    assert game.check_win('X') is False

def test_x_switches_to_o(game):
    game.current_player = 'X'
    game.switch_player()
    assert game.current_player == 'O'

def test_o_switches_to_x(game):
    game.current_player = 'O'
    game.switch_player()
    assert game.current_player == 'X'

def test_alternates_multiple_times(game):
    expected = ['O', 'X', 'O', 'X']
    results = []
    for _ in range(4):
        game.switch_player()
        results.append(game.current_player)
    assert results == expected

def test_starts_as_x(game):
    assert game.current_player == 'X'


#test results


#   test horizontal win  passed
#   test_vertical_win     passed
#   test_diagonal_win_down_right   passed
#   test_diagonal_win_up_right    passed
#   test_no_win   passed

# Bugs/Issues: None. All methods behaved correctly under all test conditions.
