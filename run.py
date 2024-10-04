import random

Class BattleshipGame:
 def_init_(self,grid_size):
    """
    The Game is initialize by given the grid_size and 
    the computer ships.
    """
  self.grid_size = grid_size
  self.grid = [["0"]]*grid_size for _ in range(grid_size)
  self.ship = []
  self.num_ships = grid_size // 2
  self.place_ships()  
