from constants import*
from sudoku_generator import*
from cell import Cell
import pygame
import copy

class Board:
    def __init__(self, removedCells, font):
        self.rowCount = BOARD_ROWS
        self.colCount = BOARD_COLS
        self.removedCells = removedCells
        board = generate_sudoku(self.rowCount, removedCells)
        self.board = board[0]
        self.fullboard = board[1]
        self.cellBoard = []
        self.currentCell = None
        self.font = font
        self.unchangedBoard = copy.deepcopy(self.board)
        
        for row in range(self.rowCount):
            temp = []
            for col in range(self.colCount):
                temp.append(Cell(row, col, self.board[row][col], font, self.fullboard[row][col]))
            self.cellBoard.append(temp)  
            
        self.oneDboard = []
        for row in self.board:
            for col in row:
                self.oneDboard.append(col)
             
        self.lines = []
        self.boldLines = []
        for i in range(1, 3):
            self.boldLines.append(pygame.Rect((SQUARE_SIZE*3*i) - (BOLD_LINE_WIDTH/2), 0, BOLD_LINE_WIDTH, HEIGHT-50)) 
            self.boldLines.append(pygame.Rect(0, (SQUARE_SIZE*3*i) - (BOLD_LINE_WIDTH/2), WIDTH, BOLD_LINE_WIDTH))
            
        for i in range(1, 3):
            self.lines.append(pygame.Rect((SQUARE_SIZE*i) - (LINE_WIDTH/2), 0, LINE_WIDTH, HEIGHT-50)) 
            self.lines.append(pygame.Rect(0, (SQUARE_SIZE*i) - (LINE_WIDTH/2), WIDTH, LINE_WIDTH))
            
        for i in range(1, 3):
            self.lines.append(pygame.Rect((SQUARE_SIZE*i)+(SQUARE_SIZE*3) - (LINE_WIDTH/2), 0, LINE_WIDTH, HEIGHT-50)) 
            self.lines.append(pygame.Rect(0, (SQUARE_SIZE*i)+(SQUARE_SIZE*3) - (LINE_WIDTH/2), WIDTH, LINE_WIDTH))
            
        for i in range(1, 3):
            self.lines.append(pygame.Rect((SQUARE_SIZE*i)+(SQUARE_SIZE*6) - (LINE_WIDTH/2), 0, LINE_WIDTH, HEIGHT-50)) 
            self.lines.append(pygame.Rect(0, (SQUARE_SIZE*i)+(SQUARE_SIZE*6) - (LINE_WIDTH/2), WIDTH, LINE_WIDTH))
            
        self.lines.append(pygame.Rect(0, HEIGHT-50, WIDTH, LINE_WIDTH))
        
    def check_win(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] != self.fullboard[row][col]:
                    return False
        return True
        
    def print_board(self):
        for row in self.board:
            print(row) 
        print("\n")
        for row in self.fullboard:
            print(row)
        for row in self.cellBoard:
            for col in row:
                print(col.value, end="")
            print()
            
    def draw_lines(self, window):
        for line in self.lines:
            pygame.draw.rect(window, BLACK, line)
        for line in self.boldLines:
            pygame.draw.rect(window, BLACK, line)
            
    def draw_board(self, window):
        pos = pygame.mouse.get_pos()
        for row in self.cellBoard:
            for cell in row:
                cell.drawCell(window, pos)
                
        self.draw_lines(window)
        
    def draw_board_for_ai(self, window):
        for row in self.cellBoard:
            for cell in row:
                cell.drawCellforAI(window)
                
        self.draw_lines(window)
        
    def unclick_all(self):
        for row in self.cellBoard:
            for cell in row:
                cell.clicked = False
        
    def check_click(self, pos):
        for row in self.cellBoard:
            for cell in row:
                if cell.Rect.collidepoint(pos):
                    self.unclick_all()
                    cell.clicked = not cell.clicked
                    self.currentCell = (cell.row, cell.col)
                    
    def update_board(self, key):
        if self.currentCell != None and self.cellBoard[self.currentCell[0]][self.currentCell[1]].changeable:
            if key == pygame.K_1:
                self.cellBoard[self.currentCell[0]][self.currentCell[1]].value = 1
            elif key == pygame.K_2:
                self.cellBoard[self.currentCell[0]][self.currentCell[1]].value = 2
            elif key == pygame.K_3:
                self.cellBoard[self.currentCell[0]][self.currentCell[1]].value = 3
            elif key == pygame.K_4:
                self.cellBoard[self.currentCell[0]][self.currentCell[1]].value = 4
            elif key == pygame.K_5:
                self.cellBoard[self.currentCell[0]][self.currentCell[1]].value = 5
            elif key == pygame.K_6:
                self.cellBoard[self.currentCell[0]][self.currentCell[1]].value = 6
            elif key == pygame.K_7:
                self.cellBoard[self.currentCell[0]][self.currentCell[1]].value = 7
            elif key == pygame.K_8:
                self.cellBoard[self.currentCell[0]][self.currentCell[1]].value = 8
            elif key == pygame.K_9:
                self.cellBoard[self.currentCell[0]][self.currentCell[1]].value = 9
                
    def reset(self):
        board = generate_sudoku(self.rowCount, self.removedCells)
        self.board = board[0]
        self.fullboard = board[1]
        self.cellBoard = []
        self.currentCell = None
        
        for row in range(self.rowCount):
            temp = []
            for col in range(self.colCount):
                temp.append(Cell(row, col, self.board[row][col], self.font, self.fullboard[row][col]))
            self.cellBoard.append(temp)  
            
    def find_optimal_cell(self):
        count = 0
        maxCount = None
        bestRow = None
        bestCol = None
        
        
        
        for i in range(9):
            rowlist = []
            count = 0
            col = 0
            for j in range(9):
                rowlist.append(self.board[i][j])
            for k in range(9):
                if rowlist[k] == 0:
                    count += 1
                    col = k
            if count == 1:
                return (i, col)
                    
                
        
        
        for i in range(9):
            collist = []
            count = 0
            row = 0
            for j in range(9):
                collist.append(self.board[j][i])
            for k in range(9):
                if collist[k] == 0:
                    count += 1
                    row = k
            if count == 1:
                return (row, i)        
        
        
        
           
        for row in self.cellBoard:
            for cell in row:
                if cell.changeable and cell.value == 0:
                    for i in range(9):
                        if self.board[cell.row][i] != 0:
                            count += 1
                    for i in range(9):
                        if self.board[i][cell.col] != 0:
                            count += 1
                    if cell.row < 3 and cell.col < 3:               #this is a mess, but it works
                        for i in range(3):                          #top left
                            for j in range(3):
                                if self.board[i][j] != 0:
                                    count += 1 
                    elif cell.row < 3 and cell.col < 6:             #top middle
                        for i in range(3):
                            for j in range(3, 6):
                                if self.board[i][j] != 0:
                                    count += 1
                    elif cell.row < 3 and cell.col < 9:             #top right
                        for i in range(3):
                            for j in range(6, 9):
                                if self.board[i][j] != 0:
                                    count += 1
                    elif cell.row < 6 and cell.col < 3:             #middle left
                        for i in range(3, 6):
                            for j in range(3):
                                if self.board[i][j] != 0:
                                    count += 1
                    elif cell.row < 6 and cell.col < 6:             #middle middle
                        for i in range(3, 6):
                            for j in range(3, 6):
                                if self.board[i][j] != 0:
                                    count += 1
                    elif cell.row < 6 and cell.col < 9:             #middle right
                        for i in range(3, 6):
                            for j in range(6, 9):
                                if self.board[i][j] != 0:
                                    count += 1
                    elif cell.row < 9 and cell.col < 3:
                        for i in range(6, 9):
                            for j in range(3):
                                if self.board[i][j] != 0:
                                    count += 1
                    elif cell.row < 9 and cell.col < 6:
                        for i in range(6, 9):
                            for j in range(3, 6):
                                if self.board[i][j] != 0:
                                    count += 1
                    elif cell.row < 9 and cell.col < 9:
                        for i in range(6, 9):
                            for j in range(6, 9):
                                if self.board[i][j] != 0:
                                    count += 1
                    if maxCount == None or count > maxCount:
                        maxCount = count
                        bestRow = cell.row
                        bestCol = cell.col
                        
        if maxCount == None:
            return None
        return (bestRow, bestCol)
    
    def get_box_vals(self, row, col):
        boxCells = []
        if row < 3 and col < 3:               #this is a mess, but it works
            for i in range(3):                          #top left
                for j in range(3):
                    boxCells.append(self.board[i][j])
        elif row < 3 and col < 6:             #top middle
            for i in range(3):
                for j in range(3, 6):
                    boxCells.append(self.board[i][j])
        elif row < 3 and col < 9:             #top right
            for i in range(3):
                for j in range(6, 9):
                    boxCells.append(self.board[i][j])
        elif row < 6 and col < 3:             #middle left
            for i in range(3, 6):
                for j in range(3):
                    boxCells.append(self.board[i][j])
        elif row < 6 and col < 6:             #middle middle
            for i in range(3, 6):
                for j in range(3, 6):
                    boxCells.append(self.board[i][j])
        elif row < 6 and col < 9:             #middle right
            for i in range(3, 6):
                for j in range(6, 9):
                    boxCells.append(self.board[i][j])
        elif row < 9 and col < 3:
            for i in range(6, 9):
                for j in range(3):
                    boxCells.append(self.board[i][j])
        elif row < 9 and col < 6:
            for i in range(6, 9):
                for j in range(3, 6):
                    boxCells.append(self.board[i][j])
        elif row < 9 and col < 9:
            for i in range(6, 9):
                for j in range(6, 9):
                    boxCells.append(self.board[i][j])
        return boxCells
    
    def restart(self):
        for i in range(9):
            for j in range(9):
                self.board[i][j] = self.unchangedBoard[i][j]
                self.cellBoard[i][j].value = self.unchangedBoard[i][j]
                
    def get_box_vals_rows_cols(self, row, col):
        rows = []
        cols = []
        if row < 3:
            rows.extend([0, 1, 2])
        elif row < 6:
            rows.extend([3, 4, 5])
        elif row < 9:
            rows.extend([6, 7, 8])
        if col < 3:
            cols.extend([0, 1, 2])
        elif col < 6:
            cols.extend([3, 4, 5])
        elif col < 9:
            cols.extend([6, 7, 8]) 
        cols.remove(col)
        rows.remove(row)
        total = []
        for i in range(2):
            for j in range(9):
                total.append(self.board[rows[i]][j])
                total.append(self.board[j][cols[i]])
        return total
        
        
            