import pygame
import random


class Maze:
    def __init__(self, rows, cols, cell_size):

        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size

        # ==================================================
        # REQUIRED STRUCTURE
        # ==================================================
        self.northWall = [[True for _ in range(cols)] for _ in range(rows)]
        self.eastWall = [[True for _ in range(cols)] for _ in range(rows)]

        # Left boundary (as described in assignment)
        self.leftWall = [[True for _ in range(cols)] for _ in range(rows)]

        # ==================================================
        # GENERATION (DFS “mouse eating walls”)
        # ==================================================
        self.visited_gen = [[False for _ in range(cols)] for _ in range(rows)]
        self.stack = []

        self.current = (0, 0)
        self.visited_gen[0][0] = True

        # Start & End (on edges)
        self.start_row = random.randint(0, rows - 1)
        self.end_row = random.randint(0, rows - 1)

        self.leftWall[self.start_row][0] = False
        self.eastWall[self.end_row][cols - 1] = False

        # ==================================================
        # SOLVER (backtracking mouse)
        # ==================================================
        self.visited_solve = [[False for _ in range(cols)] for _ in range(rows)]
        self.path_stack = []
        self.dead = [[False for _ in range(cols)] for _ in range(rows)]
        self.finished = False

    # ======================================================
    # MAZE GENERATION (DFS STACK BACKTRACKING)
    # ======================================================
    def step_generation(self):

        r, c = self.current

        neighbors = []

        if r > 0 and not self.visited_gen[r - 1][c]:
            neighbors.append((r - 1, c))
        if r < self.rows - 1 and not self.visited_gen[r + 1][c]:
            neighbors.append((r + 1, c))
        if c > 0 and not self.visited_gen[r][c - 1]:
            neighbors.append((r, c - 1))
        if c < self.cols - 1 and not self.visited_gen[r][c + 1]:
            neighbors.append((r, c + 1))

        if neighbors:
            nr, nc = random.choice(neighbors)

            # remove wall between cells
            if nr == r - 1:
                self.northWall[r][c] = False
            elif nr == r + 1:
                self.northWall[nr][nc] = False
            elif nc == c - 1:
                self.eastWall[nr][nc] = False
            elif nc == c + 1:
                self.eastWall[r][c] = False

            # DFS behavior
            self.stack.append(self.current)
            self.visited_gen[nr][nc] = True
            self.current = (nr, nc)

        else:
            if self.stack:
                self.current = self.stack.pop()
            else:
                return True

        return False

    # ======================================================
    # SOLVER (BACKTRACKING MOUSE)
    # ======================================================
    def prepare_solver(self):
        self.path_stack = [(self.start_row, 0)]
        self.visited_solve[self.start_row][0] = True

    def step_solver(self):

        if self.finished or not self.path_stack:
            return

        r, c = self.path_stack[-1]

        if r == self.end_row and c == self.cols - 1:
            self.finished = True
            return

        neighbors = []

        if c < self.cols - 1 and not self.eastWall[r][c] and not self.visited_solve[r][c + 1]:
            neighbors.append((r, c + 1))

        if r < self.rows - 1 and not self.northWall[r + 1][c] and not self.visited_solve[r + 1][c]:
            neighbors.append((r + 1, c))

        if c > 0 and not self.eastWall[r][c - 1] and not self.visited_solve[r][c - 1]:
            neighbors.append((r, c - 1))

        if r > 0 and not self.northWall[r][c] and not self.visited_solve[r - 1][c]:
            neighbors.append((r - 1, c))

        if neighbors:
            nr, nc = random.choice(neighbors)
            self.path_stack.append((nr, nc))
            self.visited_solve[nr][nc] = True

        else:
            dr, dc = self.path_stack.pop()
            self.dead[dr][dc] = True

    # ======================================================
    # DRAW
    # ======================================================
    def draw(self, screen):

        for r in range(self.rows):
            for c in range(self.cols):

                x = c * self.cell_size
                y = r * self.cell_size

                # DEAD END (blue)
                if self.dead[r][c]:
                    pygame.draw.rect(screen, (0, 0, 255),
                                     (x, y, self.cell_size, self.cell_size))

                # SOLVER POSITION (red)
                if self.path_stack and (r, c) == self.path_stack[-1]:
                    pygame.draw.circle(screen, (255, 0, 0),
                                       (x + self.cell_size // 2,
                                        y + self.cell_size // 2),
                                       self.cell_size // 4)

                # GENERATION POSITION (green)
                if (r, c) == self.current:
                    pygame.draw.circle(screen, (0, 200, 0),
                                       (x + self.cell_size // 2,
                                        y + self.cell_size // 2),
                                       self.cell_size // 4)

                # NORTH WALL
                if self.northWall[r][c]:
                    pygame.draw.line(screen, (0, 0, 0),
                                     (x, y),
                                     (x + self.cell_size, y), 2)

                # EAST WALL
                if self.eastWall[r][c]:
                    pygame.draw.line(screen, (0, 0, 0),
                                     (x + self.cell_size, y),
                                     (x + self.cell_size, y + self.cell_size), 2)

                # LEFT BORDER
                if c == 0 and self.leftWall[r][c]:
                    pygame.draw.line(screen, (0, 0, 0),
                                     (x, y),
                                     (x, y + self.cell_size), 2)

        # bottom border
        pygame.draw.line(screen, (0, 0, 0),
                         (0, self.rows * self.cell_size),
                         (self.cols * self.cell_size,
                          self.rows * self.cell_size), 2)