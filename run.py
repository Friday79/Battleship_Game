import random
import sys
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)



class BattleshipGame:
    def __init__(self, grid_size):
        """
        Game is init by giving the grid_size and placing the computer's ships.
        """
        self.grid_size = grid_size
        self.grid = [["0"] * grid_size for _ in range(grid_size)]
        self.ships = []
        self.num_ships = grid_size // 2
        self.place_ships() 

    def place_ships(self):
        """
        Randomly place ships on the grid.
        """
        while len(self.ships) < self.num_ships:
            row = random.randint(0, self.grid_size - 1)
            col = random.randint(0, self.grid_size - 1)
            if (row, col) not in self.ships:
                self.ships.append((row, col))

    def display_grid(self):
        """
        Display the grid to the player.
        """
        for row in self.grid:
            print(" ".join(row))

    def take_guess(self):
        """
        Get and validate the user's guess.
        """
        while True:
            try:
                guess_row = int(input(
                    f"Enter row location (0-{self.grid_size - 1}): "))
                guess_col = int(input(
                    f"Enter col location (0-{self.grid_size - 1}): "))
                if not (0 <= guess_row < self.grid_size and 0 <= guess_col < self.grid_size):
                    print(Fore.RED + "Location out of bounds, try again.")
                elif self.grid[guess_row][guess_col] != "0":
                    print(Fore.YELLOW + "You have already guessed this spot,")
                    print("try again.")
                else:
                    return guess_row, guess_col
            except ValueError:
                print(Fore.RED + "Invalid input, please enter numbers.")

    def update_grid(self, row, col, hit):
        """
        Update the grid based on whether the guess was a hit or miss.
        """
        self.grid[row][col] = "X" if hit else "_"
        print(Fore.GREEN + "Hit!" if hit else  Fore.BLUE + "Miss!")

    def check_guess(self, row, col):
        """
        Check if the guess hit a ship.
        """
        return (row, col) in self.ships

    def play(self):
        """
        Main game loop where the player plays against the computer.
        """
        attempts = 0
        hits = 0
        print(
            Fore.CYAN + f"Welcome to Battleships! need to sink {self.num_ships} ships.")

        while hits < self.num_ships:
            print("\nCurrent grid:")
            self.display_grid()
            row, col = self.take_guess()
            attempts += 1

            if self.check_guess(row, col):
                hits += 1
                print("You hit a ship!")
                self.update_grid(row, col, hit=True)
                self.ships.remove((row, col))
            else:
                print("You missed!")
                self.update_grid(row, col, hit=False)

        print(Fore.GREEN + f"Congratulations! You sunk all ships in {attempts} attempts.")


def main():
    """
    Initialize and run the Battleships game.
    """
    print(Fore.CYAN + "🧠 Let's play Battleship!\n")
    while True:
        try:
            grid_size = int(input(
                "Enter grid size (minimum 5, maximum 12): "))
            if grid_size < 5 or grid_size > 12:
                print(Fore.RED + "Grid size must be between 5 and 12.")
            else:
                break
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")
        except (KeyboardInterrupt, EOFError):
            print(Fore.MAGENTA + "\n Goodbye!")
            sys.exit(0)
    game = BattleshipGame(grid_size)
    print(Fore.MAGENTA + "🛳️  Welcome Aboard, Captain!")
    print(Fore.CYAN + "🎯 Your mission: Locate and destroy all enemy ships.")
    print(Fore.YELLOW + "🧠 Use your brain, guess wisely, and aim carefully!")
    print(Fore.CYAN + "🔢 You'll enter row and column numbers ( 0 1 ..) to fire.")
    print(Fore.GREEN + "💥 'X' means a hit, '_' means a miss, and '0' means ungues.")
    print(Fore.MAGENTA + "🗺️  Grid size number will be // 2 to get number of ship.")
    printFore.YELLOW + ("🚨 You have unlimited guesses, try use as few as possible.")
    game.play()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(Fore.RED + f"\n Unexpected error: {e}")
        sys.exit(1)
    
