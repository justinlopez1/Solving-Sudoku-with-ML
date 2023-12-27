from constants import*
import pygame

class Button():
    def __init__(self, x, y, width, height, font, buttonText='Button',  onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = font
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False
        self.fillColors = {
            'normal': BLACK,
            'hover': GREY,
            'pressed': BLUE,
        }
        self.buttonText = font.render(buttonText, True, BLACK)
        self.buttonRect = self.buttonText.get_rect()
        self.buttonRect.center = (self.x, self.y)
        
    def draw(self, window):
        window.blit(self.buttonText, self.buttonRect)