from enum import Enum
import pygame


CELL_SIZE = 20


class Cell(Enum):
    CLEAR = 0
    CROSS = 1
    ZERO = 2


class Player:
    '''

    Class of player. Contain type of Marks and Name
    '''
    def __init__(self, name, cell_type):
        self.name = name
        self.cell_type = cell_type


class GameField:
    '''

    '''
    pass


class GameFieldView:
    '''
    widget shows
    '''
    def __init__(self, field):
        # load pics
        self._field = field
        self._height = field.height * CELL_SIZE
        self._width = field.width * CELL_SIZE

    def draw(self):
        pass

    def check_coords_correct(self, x, y):
        return True

    def get_coords(self, x, y):
        return (0, 0)


class GameWindow:
    '''
    Contain widget of field and managing a game round
    '''
    def __init__(self):
        # initialize pygame
        pygame.init()
        self._height = 800
        self._width = 600
        self._title = 'my game'
        self._screen = pygame.display.set_mode(self._width, self._height)
        pygame.display.set_caption(self._title)

        self._field_widget = GameFieldView()
        player1 = Player('Petr', Cell.CROSS)
        player2 = Player('Vanya', Cell.ZERO)
        self._game_manager = GameRoundManager()

    def main_loop(self):
        finished = False
        while not finished:
            for event in pygame.get_events(...):
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.x, event.y
                    if self._field_widget.check_coords_correct(x, y):
                        i, j = self._field_widget.get_coords(x, y)
                        self._game_manager.handle_click(i, j)

class GameRoundManager:
    '''

    Manager that switch on all actions in game
    '''
    def __init__(self, player1: Player, player2: Player):
        self._players = [player1, player2]
        self.current_player = 0
        self._field = GameField()

    def handle_click(self):
        player = self._players[self._current_player]
        # player makes click on the field
        pass

