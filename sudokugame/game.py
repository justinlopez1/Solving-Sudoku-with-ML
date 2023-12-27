from board import Board
import pygame
import neat
from constants import*

class Game:
    removed = 20
    
    def __init__(self, font, WINDOW, numsRemoved=30):
        self.font = font
        self.sudoku = Board(self.removed, self.font)
        self.WINDOW = WINDOW
        
    def test_ai(self, genome, config):
        wins = 0
        total = 100
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        for i in range(total):
            self.sudoku.reset();             
            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                #find optimal board index
                #pass board and optimal index into NN
                #NN returns optimal move at index
                bestIndex = self.sudoku.find_optimal_cell()     #finds the best cell to guess at based on what board index has the most information
                if bestIndex == None:
                    run = False
                    break                                            #if board has been filled, break out of loop
                bestRow = bestIndex[0]
                bestCol = bestIndex[1]          
                input = []  
                #print(bestRow)
                #rint(bestCol)                   
                for i in range(27):
                    input.append(0)
                for i in range(9):
                    if self.sudoku.board[i][bestCol] != 0:
                        input[self.sudoku.board[i][bestCol] - 1] += .33
                for i in range(9):           
                    if self.sudoku.board[bestRow][i] != 0:                              #first 9 inputs here for connecting row and col density
                        input[self.sudoku.board[bestRow][i] - 1] += .33
                boxVals = self.sudoku.get_box_vals(bestRow, bestCol)  
                for i in range(9):
                    if boxVals[i] != 0:
                        input[boxVals[i] - 1] += .33                      
                                    
                boxValsRowsCols = self.sudoku.get_box_vals_rows_cols(bestRow, bestCol)  
                for i in boxValsRowsCols:
                    if i != 0:
                        input[i - 1 + 9] += .25                               #second set of 9 inputs are for rows and cols in the same box number density
                                    
                for i in range(9):
                    for j in range(9):
                        if self.sudoku.board[i][j] != 0:                                #third set of 9 inputs are for the whole board density
                            input[self.sudoku.board[i][j] - 1 + 18] += .11
                            
                output = net.activate(input)
                result = output.index(min(output)) + 1
                
                if self.sudoku.fullboard[bestRow][bestCol] == result:
                    pass
                else:                                                       #plus ten for correct guess, minus 5 when guess was blatantly wrong
                    for i in range(9):
                        if self.sudoku.board[i][bestCol] == result or self.sudoku.board[bestRow][i] == result or boxVals[i] == result:
                            print("EPIC FAIL")
                    
                self.sudoku.board[bestRow][bestCol] = result
                self.sudoku.cellBoard[bestRow][bestCol].value = result
                
                self.WINDOW.fill(WHITE)        
                self.sudoku.draw_board_for_ai(self.WINDOW)
                pygame.display.update()    
                
            if self.sudoku.check_win():
                wins += 1 
                
        print(float(wins)/total)
                
                
                
                
                
    def train_ai(self, genome, config):
        for i in range(15):
            #self.sudoku.restart()            #same board for each genome
            self.sudoku.reset();              #new board for each genome     havent found which to be better 
            net = neat.nn.FeedForwardNetwork.create(genome, config)
            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                #find optimal board index
                #pass board and optimal index into NN
                #NN returns optimal move at index
                bestIndex = self.sudoku.find_optimal_cell()     #finds the best cell to guess at based on what board index has the most information
                if bestIndex == None:
                    run = False
                    break                                            #if board has been filled, break out of loop
                bestRow = bestIndex[0]
                bestCol = bestIndex[1]          
                input = []  
                #print(bestRow)
                #rint(bestCol)                   
                for i in range(27):
                    input.append(0)
                for i in range(9):
                    if self.sudoku.board[i][bestCol] != 0:
                        input[self.sudoku.board[i][bestCol] - 1] += .33
                for i in range(9):           
                    if self.sudoku.board[bestRow][i] != 0:                              #first 9 inputs here for connecting row and col density
                        input[self.sudoku.board[bestRow][i] - 1] += .33
                boxVals = self.sudoku.get_box_vals(bestRow, bestCol)  
                for i in range(9):
                    if boxVals[i] != 0:
                        input[boxVals[i] - 1] += .33                      
                                    
                boxValsRowsCols = self.sudoku.get_box_vals_rows_cols(bestRow, bestCol)  
                for i in boxValsRowsCols:
                    if i != 0:
                        input[i - 1 + 9] += .25                               #second set of 9 inputs are for rows and cols in the same box number density
                                    
                for i in range(9):
                    for j in range(9):
                        if self.sudoku.board[i][j] != 0:                                #third set of 9 inputs are for the whole board density
                            input[self.sudoku.board[i][j] - 1 + 18] += .11
                            
                output = net.activate(input)
                result = output.index(min(output)) + 1
                if self.sudoku.fullboard[bestRow][bestCol] == result:
                    genome.fitness += 10
                else:                                                       #plus ten for correct guess, minus 10 when guess was blatantly wrong
                    stop = False
                    for i in range(9):
                        if not stop:
                            if self.sudoku.board[i][bestCol] == result:
                                genome.fitness -= 10
                                stop = True
                            if self.sudoku.board[bestRow][i] == result:
                                genome.fitness -= 10
                                stop = True
                            if boxVals[i] == result:
                                genome.fitness -= 10
                                stop = True
                    
                self.sudoku.board[bestRow][bestCol] = self.sudoku.fullboard[bestRow][bestCol]
                self.sudoku.cellBoard[bestRow][bestCol].value = self.sudoku.fullboard[bestRow][bestCol]
                
                self.WINDOW.fill(WHITE)        
                self.sudoku.draw_board_for_ai(self.WINDOW)
                pygame.display.update()     
        