from sudoku_generator import *
from board import*
from constants import*
from cell import*
from menu import*
import pygame

def play():
	drawMenu = True
	runningGame = False
	numsRemoved = 0

	pygame.init()
	pygame.font.init()
	font = pygame.font.SysFont('Arial', 40)
 
	keyText = font.render("\"r\" to get new board, \"m\" to go to menu", True, BLACK)

	mainMenu = Menu(font)

	WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Sudoku!")

	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN and runningGame:
				pos = pygame.mouse.get_pos()
				sudoku.check_click(pos)
			if event.type == pygame.KEYDOWN and runningGame and sudoku.currentCell != None:
				sudoku.update_board(event.key)
			if event.type == pygame.KEYDOWN and event.key == pygame.K_r and runningGame:
				sudoku.reset()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_m and not drawMenu:
				drawMenu = True
				runningGame = False
				numsRemoved = 0
    
		if numsRemoved != 0 and not runningGame:
			drawMenu = False
			sudoku = Board(numsRemoved, font)
			sudoku.print_board()
			runningGame = True

		if drawMenu:
			WINDOW.fill(WHITE)
			numsRemoved = mainMenu.drawButtons(WINDOW)
			
   
		else:
			WINDOW.fill(WHITE)
			sudoku.draw_board(WINDOW)
			WINDOW.blit(keyText, (60, HEIGHT-50))

		pygame.display.update()

	pygame.quit()

if __name__ == "__main__":
	play()