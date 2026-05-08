import pygame
from maze import Maze

# ---------------- SETTINGS ----------------
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 20, 20
CELL_SIZE = WIDTH // COLS

WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator & Solver")
clock = pygame.time.Clock()

maze = Maze(ROWS, COLS, CELL_SIZE)

running = True
generating = True
solving = False

while running:
    clock.tick(30)  #  slower frame rate 

    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ---------------- GENERATION ----------------
    if generating:
        generating = not maze.step_generation()

    # ---------------- SOLVER START ----------------
    elif not solving:
        maze.prepare_solver()
        solving = True

    # ---------------- SOLVING ----------------
    else:
        maze.step_solver()

    maze.draw(screen)
    pygame.display.flip()

pygame.quit()