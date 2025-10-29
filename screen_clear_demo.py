import os
import time


def clear_screen():
    # Check the operating system
    if os.name == 'nt':  # For Windows
        _ = os.system('cls')
    else:  # For macOS and Linux
        _ = os.system('clear')


def main():
    clear_screen()
    for i in range(60):
        print(i)
        time.sleep(1)
        clear_screen()


if __name__ == "__main__":
    main()