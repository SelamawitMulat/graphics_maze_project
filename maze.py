import pygame
import random
import time

class Maze:
    def __init__(self, rows, cols, cell_size):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size

        # walls
        self.northWall = [[True for _ in range(cols)] for _ in range(rows)]
        self.eastWall = [[True for _ in range(cols)] for _ in range(rows)]

        # generation
        self.visited_gen = [[False for _ in range(cols)] for _ in range(rows)]
        self.stack = [(0, 0)]
        self.visited_gen[0][0] = True

        # solver
        self.visited_solve = [[False for _ in range(cols)] for _ in range(rows)]
        self.dead = [[False for _ in range(cols)] for _ in range(rows)]
        self.path_stack = []

    # ---------------- GENERATION ----------------
    def step_generation(self):
        if not self.stack:
            return True

        r, c = self.stack[-1]

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

            # remove walls
            if nr == r - 1:
                self.northWall[r][c] = False
            elif nr == r + 1:
                self.northWall[nr][nc] = False
            elif nc == c - 1:
                self.eastWall[nr][nc] = False
            elif nc == c + 1:
                self.eastWall[r][c] = False

            self.visited_gen[nr][nc] = True
            self.stack.append((nr, nc))
        else:
            self.stack.pop()

        time.sleep(0.03)  # 🟢 slower generation

        return False

    # ---------------- SOLVER ----------------
    def prepare_solver(self):
        self.path_stack = [(0, 0)]
        self.visited_solve[0][0] = True

    def step_solver(self):
        if not self.path_stack:
            return

        r, c = self.path_stack[-1]

        if (r, c) == (self.rows - 1, self.cols - 1):
            return

        moved = False

        if c < self.cols - 1 and not self.eastWall[r][c] and not self.visited_solve[r][c + 1]:
            self.path_stack.append((r, c + 1))
            self.visited_solve[r][c + 1] = True
            moved = True

        elif r < self.rows - 1 and not self.northWall[r + 1][c] and not self.visited_solve[r + 1][c]:
            self.path_stack.append((r + 1, c))
            self.visited_solve[r + 1][c] = True
            moved = True

        elif c > 0 and not self.eastWall[r][c - 1] and not self.visited_solve[r][c - 1]:
            self.path_stack.append((r, c - 1))
            self.visited_solve[r][c - 1] = True
            moved = True

        elif r > 0 and not self.northWall[r][c] and not self.visited_solve[r - 1][c]:
            self.path_stack.append((r - 1, c))
            self.visited_solve[r - 1][c] = True
            moved = True

        if not moved:
            r2, c2 = self.path_stack.pop()
            self.dead[r2][c2] = True

        time.sleep(0.03)  # 🟠 slower solver movement

    # ---------------- DRAW ----------------
    def draw(self, screen):
        for r in range(self.rows):
            for c in range(self.cols):
                x = c * self.cell_size
                y = r * self.cell_size

                # solver red dot
                if self.path_stack and (r, c) == self.path_stack[-1]:
                    pygame.draw.circle(
                        screen,
                        (255, 0, 0),
                        (x + self.cell_size // 2, y + self.cell_size // 2),
                        self.cell_size // 4,
                    )

                # generation green dot
                if self.stack and (r, c) == self.stack[-1]:
                    pygame.draw.circle(
                        screen,
                        (0, 200, 0),
                        (x + self.cell_size // 2, y + self.cell_size // 2),
                        self.cell_size // 4,
                    )

                # dead ends
                if self.dead[r][c]:
                    pygame.draw.rect(
                        screen,
                        (0, 0, 255),
                        (x, y, self.cell_size, self.cell_size)
                    )

                # north wall
                if self.northWall[r][c]:
                    pygame.draw.line(screen, (0, 0, 0), (x, y), (x + self.cell_size, y), 2)

                # east wall
                if self.eastWall[r][c]:
                    pygame.draw.line(screen, (0, 0, 0),
                                     (x + self.cell_size, y),
                                     (x + self.cell_size, y + self.cell_size), 2)

        # border
        pygame.draw.rect(
            screen,
            (0, 0, 0),
            (0, 0, self.cols * self.cell_size, self.rows * self.cell_size),
            2
        )