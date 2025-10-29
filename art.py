from colors import Colors
from screen_clear_demo import clear_screen
import time

# Using a 2D Arraw, try to recreate something like this in the terminal:

# Note: Only one print statement
def main():
    grid = [
        [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 2, 2, 2, 3, 3, 2, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 3, 2, 3, 3, 3, 2, 3, 3, 3, 0, 0, 0],
        [0, 0, 0, 2, 3, 2, 2, 3, 3, 3, 2, 3, 3, 3, 0, 0],
        [0, 0, 0, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0],
        [0, 0, 0, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 0, 0, 0],
        [0, 0, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 0, 0],
        [0, 0, 3, 3, 2, 1, 3, 1, 1, 3, 1, 2, 3, 3, 0, 0],
        [0, 0, 3, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 3, 0, 0],
        [0, 0, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0],
        [0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0],
    ]
    draw(grid)


def create_image(grid):
    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col] == 1:
                grid[row][col] = f"{Colors.RED}{chr(0x2588)}{chr(0x2588)}{Colors.RESET}"
            elif grid[row][col] == 2:
                grid[row][col] = f"{Colors.GREEN}{chr(0x2588)}{chr(0x2588)}{Colors.RESET}"
            elif grid[row][col] == 3:
                grid[row][col] = f"{Colors.YELLOW}{chr(0x2588)}{chr(0x2588)}{Colors.RESET}"
            else:
                grid[row][col] = "  "

def draw(grid):
    create_image(grid)
    draw_image(grid)

def draw_image(grid):
    for index, value in enumerate(grid):
            for col in value:
                print(col, end="")
            print()
            
if __name__ == "__main__":
    main()