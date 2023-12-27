
import math, random, copy

class SudokuGenerator:
    def __init__(self, row_length, removed_cells):  #initializes instance of sudokugenerator
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.box_length = int(math.sqrt(row_length))
        self.board = [[0] * row_length for i in range(row_length)]  #creates empty 2d list for the board


    def get_board(self):
        return self.board

    def print_board(self):  #prints the board for debugging purposes
        #print(self.board[-1])
        #for i in range(2, len(self.board) + 1):
            #print(self.board[-i])
        for i in self.board:
            print(i)

        #just for debuging purposes

    def valid_in_row(self, row, num): #checks the entire row to see if its valid to put in row
        for item in self.board[row]:
            if item == num:
                return False

        return True

    def valid_in_col(self, col, num):   #checks the column down, or checks the same index in each row of the 2d list.
        for i in range(0, self.row_length):
            if self.board[i][int(col)] == num:
                return False

        return True

    def valid_in_box(self, row_start, col_start, num):   #checks the 9 boxes that are in each sudoku box from the top left index of the box, ex. 0, 0 or 3, 3 etc
        for i in range(0, int(self.box_length)):
            if self.board[row_start+i][int(col_start+i)] == num or self.board[row_start+i][int(col_start)] == num or self.board[row_start][int(col_start+i)] == num \
            or self.board[row_start+2][int(col_start+1)] == num or self.board[row_start+1][int(col_start+2)] == num:
                return False   #its a bit confusing but each if and or statement above checks different boxes in the 3x3square

        return True

    def is_valid(self, row, col, num):   #runs the above 3 statements to check if a sudoku cell is correct
        row_start = (row // int(self.box_length)) * int(self.box_length)
        col_start = (col // int(self.box_length)) * int(self.box_length)  #these two statements are for the valid in box command becuase it has to use the top left index to check the entire box
        if not self.valid_in_row(row, num):
            return False
        elif not self.valid_in_col(col, num):
            return False
        elif not self.valid_in_box(row_start, col_start, num):
            return False
        else:
            return True


    def fill_box(self, row_start, col_start):  #randomly fills box with 1-9
        randomlist = []
        for p in range(1, self.row_length+1):
            randomlist.extend([p]) #creates randomlsit which is a list from 1-9
        random.shuffle(randomlist)   #shuffles the random list so that we have a random list of numbesr from 1-9

        counter = 0
        for row in range(0, int(self.box_length)):      #places the random list in the box, 3 in each row, using the top left corner index of the box
            for col in range(0, int(self.box_length)):
                self.board[row+row_start][col+col_start] = randomlist[counter]
                counter += 1


    def fill_diagonal(self):     #runs the fill box command for each box along the diagonal, so that the backtracaking function below can be used to fill in the rest
        for i in range(0, int(self.box_length)):
            self.fill_box(3 * i, 3 * i )


    def fill_remaining(self, row, col): #backtracking function given to us
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][int(col)] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][int(col)] = 0
        return False

    def fill_values(self):   #fills the entire board
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)


    def remove_cells(self):    #removes self.removed_cells amount of cells from the board at random by picking random numbers between 0-8 self.removed cell amount of times
        randomlist = []
        for p in range(0, self.row_length):
            randomlist.extend([p])
        counter = 0
        while counter < self.removed_cells:
            x = random.choice(randomlist)
            y = random.choice(randomlist)
            if self.board[x][y] != 0:
                self.board[x][y] = 0
                counter += 1  #counter used here so that we dont count when the random index's chosen were the same twice in a row so we actually have the desired amount of cells removed

def generate_sudoku(size, removed):  #given to use, generates an instance of class SudokuGenerator
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    fullboard = copy.deepcopy(sudoku.get_board())
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board, fullboard