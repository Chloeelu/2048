import random, sys

class TwentyFortyEight:
    def __init__(self) -> None: # Use as is
        """ 
            initializes the board data field
            and displays the initial board
            and prints a welcome message
        """

        self.board: list = []  # a 2-D list to keep current status of the game board
        for _ in range(4):     # initialize the board cells/tiles with ''
            rowList = []
            for _ in range(4):
                rowList.append('')
            self.board.append(rowList)

        # add two starting 2's at random cells; using a trivial search
        countOfTwosPlacedAtTheBeginning = 0  
        while countOfTwosPlacedAtTheBeginning < 2:  
            row = random.randint(0, 3)
            column = random.randint(0, 3)
            if self.board[row][column] == '': # if not already taken
                self.board[row][column] = 2
                countOfTwosPlacedAtTheBeginning += 1
        
        print(); print("Welcome! Let's play the 2048 game."); print()
    

    def displayGame(self) -> None:  # Use as is
        """ displays the current board on the console """

        print("+-----+-----+-----+-----+")
        for row in range(4): 
            for column in range(4):
                cell = self.board[row][column] 
                print(f"|{str(cell).center(5)}", end="")
            print("|")
            print("+-----+-----+-----+-----+")


    def addANewTwoToBoard(self) -> None:
        """ 
            adds a new 2 at a random available cell
        """
        col = random.randint(0,3)
        row = random.randint(0,3)
        while self.board[row][col] != '':
            col = random.randint(0,3)
            row = random.randint(0,3)
        self.board[row][col] = 2
        self.displayGame
        


    def isFull(self) -> bool:
        """ returns True if no empty cell is left, False otherwise """
        for row in range(4): 
            for column in range(4):
                if self.board[row][column] == '':
                    return False
        return True
            


    def getCurrentScore(self) -> int:
        """ 
            calculates and returns the score
            the score is the sum of all the numbers currently on the board
        """
        score=0
        for row in range(4): 
            for column in range(4):
                if self.board[row][column] != '':
                    score += int(self.board[row][column])
        return score


    def updateTheBoardBasedOnTheUserMove(self, move: str) -> None:
        """
            updates the board field based on the move argument
            the move argument is either 'W', 'A', 'S', or 'D'
            directions: W for up; A for left; S for down, and D for right
        """
        old : list = []
        for i in range(4):     # initialize the board cells/tiles with ''
            rowList = []
            for j in range(4):
                rowList.append(self.board[i][j])
            old.append(rowList)
        while True:
            # W for up move
            if move == 'W':
                for i in range(4):
                    # combine values
                    self.up_down_comb(i)
                    # move to top
                    self.up_down_move(i)
                
            # S for down move
            elif move == 'S':
                self.board.reverse()
                for i in range(4):
                    # combine values
                    self.up_down_comb(i)
                    # move to top
                    self.up_down_move(i)
                self.board.reverse()
            # A for left move
            elif move == 'A':
                for i in range(4):
                    # combine values
                    self.left_right_comb(i)
                    # move to top
                    self.left_right_move(i)

            # D for right move
            elif move == 'D':
                for i in range(4):
                    self.board[i] = self.board[i][::-1]
                for i in range(4):
                    # combine values
                    self.left_right_comb(i)
                    # move to top
                    self.left_right_move(i)
                for i in range(4):
                    self.board[i] = self.board[i][::-1]
            if self.board == old:
                move = input("Unable to move, please try another:").upper()
                while move not in ('W', 'A', 'S', 'D', 'Q'):
                    print('Enter one of "W", "A", "S", "D", or "Q"') # otherwise inform the user about valid input
                    move = input('> ').upper()
                if move == 'Q': # for quit
                    print("Exiting the game. Thanks for playing!")
                    sys.exit()
            else:
                break


# combination algorithms for up and down move
    def up_down_comb(self, col: int) -> None:
        for row in range(4):
            if self.board[row][col] != '':
                        #go down to search for number with same value
                        i = 1
                        while row+i < 4:
                            if self.board[row+i][col] == self.board[row][col]:
                                self.board[row][col] = self.board[row][col]*2
                                self.board[row+i][col] = ''
                                break
                            elif self.board[row+i][col] != '':
                                break
                            i += 1

# move algorithms for up and down move
    def up_down_move(self, c: int) -> None:
        new_col = list()
        for r in range(4):
            if self.board[r][c] != '':
                new_col.append(self.board[r][c])
        for x in range(4):
            if x<len(new_col):
                self.board[x][c] = new_col[x]
            else:
                self.board[x][c] = ''

# combination algorithms for right and left move
    def left_right_comb(self, row: int) -> None:
        for col in range(4):
            if self.board[row][col] != '':
                        #go down to search for number with same value
                        i = 1
                        while col+i < 4:
                            if self.board[row][col+i] == self.board[row][col]:
                                self.board[row][col] = self.board[row][col]*2
                                self.board[row][col+i] = ''
                                break
                            elif self.board[row][col+i] != '':
                                break
                            i += 1

# move algorithms for right and left move
    def left_right_move(self, r: int) -> None:
        new_col = list()
        for c in range(4):
            if self.board[r][c] != '':
                new_col.append(self.board[r][c])
        for x in range(4):
            if x<len(new_col):
                self.board[r][x] = new_col[x]
            else:
                self.board[r][x] = ''



if __name__ == "__main__":  # Use as is
    def promptGamerForTheNextMove() -> str: #An inner function
        """
            prompts the gamer to select the next move or Q (to quit)
            valid move direction: one of 'W', 'A', 'S' or 'D'.
            either returns a valid move direction or terminates the game
        """
        print("Enter one of WASD (move direction) or Q (to quit)")
        while True:  # prompt until a valid input is entered
            move = input('> ').upper()
            if move in ('W', 'A', 'S', 'D'): # a valid move direction
                return move  
            if move == 'Q': # for quit
                print("Exiting the game. Thanks for playing!")
                sys.exit()
            print('Enter one of "W", "A", "S", "D", or "Q"') # otherwise inform the user about valid input
   
    game = TwentyFortyEight()

    while True:  # Super-loop for the game
        game.displayGame()
        print(f"Score: {game.getCurrentScore()}")
        game.updateTheBoardBasedOnTheUserMove(promptGamerForTheNextMove())
        game.addANewTwoToBoard()

        if game.isFull():
            game.displayGame()
            print("Game is over. Check out your score.")
            print("Thanks for playing!")
            break
