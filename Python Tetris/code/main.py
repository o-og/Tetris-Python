# Welcome! Please run this script by clicking the play button...                                                       right over here ^
# You can use ⌘ + ⌥ + D on the keyboard lower the dock
# use the left and right arrows to move the pieces around
# use the up arrow to rotate the pieces 90 degrees
# use the down arrow to move the pieces down faster
# ENJOY!!!





























from settings import *
from sys import exit
from os.path import join

# components
from game import Game
from score import Score
from preview import Preview

from random import choice

class Main:
    def __init__(self):

        # general
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Tetris')

        # shapes
        self.next_shapes = [choice(list(TETROMINOS.keys())) for shape in range(3)]

        # components
        self.game = Game(self.get_next_shape, self.update_score)
        self.score = Score()
        self.preview = Preview()

        # music
        self.music = pygame.mixer.Sound(join('sound', 'music.wav'))
        self.music.play(-1)

    def update_score(self, lines, score, level):
        self.score.lines = lines
        self.score.score = score
        self.score.level = level

    def get_next_shape(self):
        next_shape = self.next_shapes.pop(0)
        self.next_shapes.append(choice(list(TETROMINOS.keys())))
        return next_shape

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # display
            self.display_surface.fill(GRAY)

            # components
            self.game.run()
            self.score.run()
            self.preview.run(self.next_shapes)

            # updating the game
            pygame.display.update()
            self.clock.tick()

if __name__ == '__main__':
    main = Main()
    main.run()
