import pygame
from constants import*
class Cell:
    def __init__(self, row, col, value, font, correctValue):
        self.row = row
        self.col = col
        self.value = value
        self.Text = font.render(str(value), True, BLACK)
        self.Rect = self.Text.get_rect()
        self.Rect.y = self.row * SQUARE_SIZE
        self.Rect.x = self.col * SQUARE_SIZE
        self.Rect.width = SQUARE_SIZE
        self.Rect.height = SQUARE_SIZE
        self.clicked = False
        self.font = font
        self.changeable = False
        if self.value == 0:
            self.changeable = True
        self.correctValue = correctValue
        
    def drawCell(self, window, pos=None):
        if self.clicked:
            pygame.draw.rect(window, LIGHT_BLUE, self.Rect)
        elif self.Rect.collidepoint(pos):
            pygame.draw.rect(window, GREY, self.Rect)
        else:
            pygame.draw.rect(window, WHITE, self.Rect)
           
        if self.value != 0: 
            if self.changeable and self.value == self.correctValue:
                self.Text = self.font.render(str(self.value), True, BLUE)
            elif self.changeable and self.value != 0 and self.value != self.correctValue:
                self.Text = self.font.render(str(self.value), True, RED)
            else:
                self.Text = self.font.render(str(self.value), True, BLACK)

            window.blit(self.Text, (self.Rect.x + 29, self.Rect.y + 14))
            
    def drawCellforAI(self, window):
        pygame.draw.rect(window, WHITE, self.Rect)
        if self.value != 0:
            self.Text = self.font.render(str(self.value), True, BLACK)
            window.blit(self.Text, (self.Rect.x + 29, self.Rect.y + 14))