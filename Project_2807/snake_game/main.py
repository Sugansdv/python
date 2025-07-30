import curses
import random
import time

# === Food Position Generator ===
def generate_food(max_y, max_x, snake_body):
    while True:
        food = (random.randint(1, max_y - 2), random.randint(1, max_x - 2))
        if food not in snake_body:
            yield food

# === Snake Class ===
class Snake:
    def __init__(self, y, x):
        self.body = [(y, x), (y, x - 1), (y, x - 2)]
        self.direction = curses.KEY_RIGHT

    def move(self):
        head_y, head_x = self.body[0]
        if self.direction == curses.KEY_UP:
            new_head = (head_y - 1, head_x)
        elif self.direction == curses.KEY_DOWN:
            new_head = (head_y + 1, head_x)
        elif self.direction == curses.KEY_LEFT:
            new_head = (head_y, head_x - 1)
        else:
            new_head = (head_y, head_x + 1)

        self.body.insert(0, new_head)
        return self.body.pop()

    def grow(self):
        tail = self.body[-1]
        self.body.append(tail)

    def change_direction(self, new_dir):
        opposite = {
            curses.KEY_UP: curses.KEY_DOWN,
            curses.KEY_DOWN: curses.KEY_UP,
            curses.KEY_LEFT: curses.KEY_RIGHT,
            curses.KEY_RIGHT: curses.KEY_LEFT,
        }
        if new_dir != opposite.get(self.direction):
            self.direction = new_dir

    def head(self):
        return self.body[0]

    def collision(self, max_y, max_x):
        y, x = self.head()
        return (
            y in [0, max_y - 1] or
            x in [0, max_x - 1] or
            self.head() in self.body[1:]
        )

# === Main Game Loop ===
def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    max_y, max_x = stdscr.getmaxyx()
    snake = Snake(max_y // 2, max_x // 4)
    food_gen = generate_food(max_y, max_x, snake.body)
    food = next(food_gen)

    score = 0

    while True:
        stdscr.clear()
        stdscr.border()
        stdscr.addstr(0, 2, f" Score: {score} ")

        # Draw snake
        for y, x in snake.body:
            stdscr.addch(y, x, "#")

        # Draw food
        stdscr.addch(food[0], food[1], "*")

        # Input
        key = stdscr.getch()
        if key != -1:
            snake.change_direction(key)

        # Move
        removed = snake.move()

        # Check collision
        if snake.collision(max_y, max_x):
            msg = "Game Over! Press any key to exit."
            stdscr.addstr(max_y // 2, (max_x - len(msg)) // 2, msg)
            stdscr.nodelay(0)
            stdscr.getch()
            break

        # Check food eaten
        if snake.head() == food:
            snake.body.append(removed)
            food = next(generate_food(max_y, max_x, snake.body))
            score += 1

        stdscr.refresh()
        time.sleep(0.1)

if __name__ == "__main__":
    curses.wrapper(main)
