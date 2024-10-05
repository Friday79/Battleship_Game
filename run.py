import random

class BattleshipGame:
 def _init_(self, grid_size):
    """
    The Game is initialize by given the grid_size and 
    the computer ships.
    """
self.grid_size = grid_size
  self.grid = [["0"] * grid_size for _ in range(grid_size)]
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
  While True:
     Try:
     guess_row = int(input(f"Enter row location(0-{self.grid_size -1}):"))
     guess_col = int(input(f"Enter col location(0-{self.grid_size -1}):"))
     if not (0 <= guess_row < self.grid_size and 0 <= guess_col < self.grid_size):
            print("location out of bounds, try again.")
            elif self.grid[guess_row][guess_col] != "0":
                 print("you have already guess the location, try again")
                 else:
                       return guess_row, guess_col
              except valueError:
                  print("invalid input,please enter numbers.")

    def update_grid(self,row,col,hit):
      """
      Grid updating according to guess hit or miss
      """
      self.grid[row][col] = "X" if hit else "_"
         print("Hit!" if hit else "Miss!" )

def check_guess(self,row,col):
  """
  check if the guess hit the ship
  """
  return(row,col) in self.ships

  def play(self):
    """
    where the user play against the computer, the game loop.
    """
    attempts = 0
    hits = 0
      print(f"Welcome to Battleships you need to sink 7self.num_ships.")

While hits < self.num_ships:
  print("\nCurrent grid:")
  self.display_grid()
  row,col = self.take_grid()
  attempts += 1

  if self.check_guess(row,col):
    hit += 1
       print("you hit a ship")
       self.update_grid(row,col,hit = Trueself.ships.remove((row,col)))
       else:
          print(" you missed!")
            self.update_grid(row,col, hit= False)
            else:
              
              print("Congratulation! you sunk all ships in the  {attempts} attempts.")

              def main():
                """
                Initialize and run the battleships game.
                """

                While True:
                  Try:
                  grid_size = int(input("Enter grid_side(minimum 5):"))
                  if grid_side < 5:
                      print("Grid side must be at least 5.")
                      else:
                        break
                        except valueError:
                            print("invalid input.Please enter a number.")

                            game = BattleshipGame(grid_side)
                            game.play()

                            if _name_ == "_main_":
                              main()

