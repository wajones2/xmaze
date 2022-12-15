from curses import window
import sys, random
from tkinter.font import BOLD
import pygame
from pygame.locals import *
from buttons import *


class xMaze:
    def __init__(self):

        pygame.init()
        pygame.display.set_caption('game 1')

        pygame.joystick.init()
        joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

        for joystick in joysticks:
            print(joystick.get_name())
        # screen = pygame.display.set_mode((500, 500), 0 ,32)     # Window size...removing 0 eliminates the menu bar



        self.direction = 'RIGHT'
        self.change_to = self.direction

        self.window_screen(1050, 600, 700, 600)



    def utilities(self):

        self.generate_x_start = self.maze_barrier_x_start + 1
        self.generate_x_end = self.maze_barrier_x_end - 1


        self.generate_y_start = self.maze_barrier_y_start + 1
        self.generate_y_end = self.maze_barrier_y_end - 1

        self.generate_x = lambda: random.randint(self.generate_x_start, self.generate_x_end)
        self.generate_y = lambda: random.randint(self.generate_y_start, self.generate_y_end)





    def window_screen(self, window_x, window_y, screen_x, screen_y):

        self.window_x = window_x
        self.window_y = window_y
        self.screen_x = screen_x
        self.screen_y = screen_y


        self.screen = pygame.display.set_mode([self.window_x, self.window_y])
        self.clock = pygame.time.Clock()

        self.maze()

    # ----------------------------------------------------------------------------------------------------------------
    # Player 1  

    def players(self, player_count):
        self.player_count = player_count


        # self.p1_x = self.screen_x / 2   # Player 1 x-coordinate
        # self.p1_y = self.screen_y / 2   # Player 1 y-coordinate
        self.p1_x = self.generate_x()
        self.p1_y = self.generate_y()

        self.p1_w = 50  # Player 1 width
        self.p1_h = 50   # Player 1 height

        self.p1_square = pygame.Rect(self.p1_x, self.p1_y, self.p1_w, self.p1_h)  
        self.p1_square_color = 0 
        self.p1_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 0, 0), (255, 255, 255)] # Using RGB
        self.p1_motion = [0, 0]

        self.p1_fill = 0       # Fills in center from 1 - radius of object, 1 just and outline - radius being completely filled
        self.p1_corners = 1    # Rounds corners from 1 - radius, 1 being square - radius being circle
        self.p1_top_left_corner = 1       # Rounds specified corner
        self.p1_top_right_corner = 1      # Rounds specified corner
        self.p1_bottom_left_corner = 1      # Rounds specified corner
        self.p1_bottom_right_corner = 1    # Rounds specified corner


        self.p1_x_range = lambda: [x for x in range(self.p1_square.x, self.p1_square.x + self.p1_w)]
        self.p1_y_range = lambda: [y for y in range(self.p1_square.y, self.p1_square.y + self.p1_h)]


        self.p1_score_total = 0


        self.diamonds()

    def diamonds(self):


        # Objects to collect (called diamonds for now)

        self.diamond_count = 8   # Number of diamonds available at any given moment

        self.current_availability = lambda: random.randint(1,self.diamond_count)


        self.diamond_w = 20
        self.diamond_h = 20


        self.diamond_x_start = self.maze_barrier_x_start + 1 + self.diamond_w
        self.diamond_x_end = self.maze_barrier_x_end - 1 - self.diamond_w


        self.diamond_y_start = self.maze_barrier_y_start + 1 + self.diamond_h
        self.diamond_y_end = self.maze_barrier_y_end - 1 - self.diamond_h

        self.diamond_x = lambda: random.randint(self.diamond_x_start, self.diamond_x_end)
        self.diamond_y = lambda: random.randint(self.diamond_y_start, self.diamond_y_end)



        self.diamond_dimensions = lambda: pygame.Rect(self.diamond_x(), self.diamond_y(), self.diamond_w, self.diamond_h)
        self.diamond_position = self.diamond_dimensions()


        self.diamond_x_range = lambda: [x for x in range(self.diamond_position.x, self.diamond_position.x + self.diamond_w)]
        self.diamond_y_range = lambda: [y for y in range(self.diamond_position.y, self.diamond_position.y + self.diamond_h)]



        self.diamond_colors = [(71, 49, 218)]
        self.current_diamond_color = 0

        self.diamond_fill = 0
        self.diamond_corners = 25
        self.diamond_top_left_corner = 1       # Rounds specified corner
        self.diamond_top_right_corner = 1      # Rounds specified corner
        self.diamond_bottom_left_corner = 1      # Rounds specified corner
        self.diamond_bottom_right_corner = 1    # Rounds specified corner


        self.start()
    # ----------------------------------------------------------------------------------------------------------------


    def rockets(self):

        pass


    def maze(self):

        
        self.maze_barrier_x_start = (((self.window_x - self.screen_x) // 2) + 1)
        self.maze_barrier_x_end = (self.window_x - ((self.window_x - self.screen_x) // 2) + 1)
        self.maze_barrier_y_start = (((self.window_y - self.screen_y) // 2) + 1)
        # self.maze_barrier_y_start = 2
        self.maze_barrier_y_end = (self.window_y - ((self.window_y - self.screen_y) // 2) + 1)

        # ----------------------------------------------------------------------------------------------------------------

        # Create maze here
        ## Outline

        self.maze_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 0, 0), (255, 255, 255)] # Using RGB
        self.current_maze_color = 0
        self.maze_dimensions = pygame.Rect(self.maze_barrier_x_start - 1, self.maze_barrier_y_start - 1, 700, 600)     # (x-axis, y-axis, width, height) # Changes the size of the square
        self.maze_fill = 1
        self.maze_corners = 1



        self.utilities()
        self.players(1)


    def score(self):
        
        self.labels = ['Player 1 Score', 'Player 2 Score', 'Player 3 Score', 'Player 4 Score']

        self.score_label_font = pygame.font.SysFont('Menlo', 15, BOLD)
        self.p1_score_label = self.score_label_font.render(f"{self.labels[0]}: ", True, pygame.Color(255, 0, 0))
        self.p1_score_label_rect = self.p1_score_label.get_rect()
        self.p1_score_label_rect.topleft = (10,50)
        self.screen.blit(self.p1_score_label, self.p1_score_label_rect)

        self.score_total_label_font = pygame.font.SysFont('Menlo', 20)
        self.p1_score_total_label = self.score_total_label_font.render(f"{self.p1_score_total}", True, pygame.Color(255, 0, 0))
        self.p1_score_total_label_rect = self.p1_score_total_label.get_rect()
        self.p1_score_total_label_rect.topleft = (50,80)
        self.screen.blit(self.p1_score_total_label, self.p1_score_total_label_rect)


        # pygame.display.flip()

    def start(self):

        while True:

            self.screen.fill((0, 0, 0))     # Window background; currently black
            self.score()
            ## Testing
            ### pygame.draw.rect(screen, maze_colors[r_color], pygame.Rect(30,30,50,50), diamond_fill, diamond_corners)#, top_left_corner, top_right_corner, bottom_left_corner, bottom_right_corner)

            # Maze Outline 
            pygame.draw.rect(self.screen, self.maze_colors[self.current_maze_color], self.maze_dimensions, self.maze_fill, self.maze_corners)#, top_left_corner, top_right_corner, bottom_left_corner, bottom_right_corner)

            # Diamond
            pygame.draw.rect(self.screen, self.diamond_colors[self.current_diamond_color], self.diamond_position, self.diamond_fill, self.diamond_corners)#, top_left_corner, top_right_corner, bottom_left_corner, bottom_right_corner)


            pygame.draw.rect(self.screen, self.p1_colors[self.p1_square_color], self.p1_square, self.p1_fill, self.p1_corners)#, top_left_corner, top_right_corner, bottom_left_corner, bottom_right_corner)
            # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 20, 20)     # (Screen, (Color), (Starting location), Radius, fill)
            if abs(self.p1_motion[0]) < 0.1:        # Movement
                self.p1_motion[0] = 0

            if abs(self.p1_motion[1]) < 0.1:
                self.p1_motion[1] = 0

                self.score()
                
            # Changing Diamond location when collected



            self.tf_x = False
            self.tf_y = False
            for x1 in self.p1_x_range():
                if x1 in self.diamond_x_range():
                    self.tf_x = True

            for y1 in self.p1_y_range():
                if y1 in self.diamond_y_range():
                    self.tf_y = True

            
            if self.tf_x == True and self.tf_y == True:
                self.diamond_position = self.diamond_dimensions()
                self.p1_score_total += 1
            


            ### Blocks edge of screen

            if self.p1_square.x <= self.maze_barrier_x_start:
                self.p1_motion[0] = 0
                self.p1_square.x = self.maze_barrier_x_start + 1
            elif self.p1_square.x >= ((self.maze_barrier_x_end) - self.p1_w):
                self.p1_motion[0] = 0
                self.p1_square.x = (self.maze_barrier_x_end - 1) - self.p1_w
            else:
                self.p1_square.x += self.p1_motion[0] * 10   # Movment speed along x-axis

            if self.p1_square.y <= self.maze_barrier_y_start:
                self.p1_motion[1] = 0
                self.p1_square.y = self.maze_barrier_y_start + 1
            elif self.p1_square.y >= ((self.maze_barrier_y_end) - self.p1_h):
                self.p1_motion[1] = 0
                self.p1_square.y = (self.maze_barrier_y_end - 1) - self.p1_h
            else:
                self.p1_square.y += self.p1_motion[1] * 10   # Movement speed along y-axis


            for event in pygame.event.get():
                if event.type == JOYBUTTONDOWN: 

                    if event.button == xm_btns.A_BUTTON:
                        self.p1_square_color = (self.p1_square_color + 1) % len(self.p1_colors)
                if event.type == JOYAXISMOTION:     # Right or left thumbstick
                    if event.axis < 2:
                        self.p1_motion[event.axis] = event.value
                if event.type == JOYDEVICEADDED:
                    joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())] # This adds/removes controllers
                    for joystick in joysticks:

                        print(f"Controller '{joystick.get_name()}' has joined the game.")
                if event.type == JOYDEVICEREMOVED:
                    joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
                    print(f"Controller '{joystick.get_name()}' has left the game.")
                if event.type == QUIT:
                    print("Goodbye")
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                if event.type == pygame.KEYDOWN:
                    # W -> Up; S -> Down; A -> Left; D -> Right
                    if event.key == pygame.K_UP or event.key == ord('w'):
                        self.p1_motion = [0,-1]
                    if event.key == pygame.K_DOWN or event.key == ord('s'):
                        self.p1_motion = [0,1]
                    if event.key == pygame.K_LEFT or event.key == ord('a'):
                        self.p1_motion = [-1,0]
                    if event.key == pygame.K_RIGHT or event.key == ord('d'):
                        self.p1_motion = [1,0]
                    # Esc -> Create event to quit the game

                    ## Working on diagonal directio
                    # [1,1] # Right down 
                    # [1,-1] # Right up
                    # [-1,1] # Left down
                    # [-1,-1] # Left up

                    # if event.key == pygame.K_UP and event.key == pygame.K_RIGHT or event.key == ord('w') and event.key == ord('d'):
                        # self.p1_motion = [1,-1]

                    if event.key == pygame.K_ESCAPE:
                        pygame.event.post(pygame.event.Event(pygame.QUIT))
                elif event.type == pygame.KEYUP:
                    self.p1_motion = [0,0]

            pygame.display.update()
            self.clock.tick(60)


xm = xMaze()
# xm.window_screen(900, 600, 700, 600)
# xm.window_screen()


# self.window_x = 900   # Width of window
# self.window_y = 600   # Height of window
# self.screen_x = 700   # Width of maze border
# self.screen_y = 600   # Height of maze border
