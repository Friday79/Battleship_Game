import random

class BattleshipGame:
 def _init_(self, grid_size):
    """
    The Game is initialize by given the grid_size and 
    the computer ships.
    """
self.grid_size = grid_size
  self.grid = [["0"]]*grid_size for _ in range(grid_size)
  self.ship = []
  self.num_ships = grid_size // 2
  self.place_ships()  

  def place_ships(self):
    """
    randomly place ship on the grid
    """   
    while len(self.ship) < self.num_ships:
        row,col = random.randint(0, self.grid_size -1), random.randint(0, self.grid_size -1)
        if(row, col) not in self.ships:
            self.ships.append(row, col)

    def display_grid(self)
    """
    The grid display to the player
    """
      for row in self.grid:
        print(" ".join(row))

def take_guess(self):
  """
  Getting the input of the user and validate the guess
  """
  