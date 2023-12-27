import pygame
from constants import*
from button import*

class Menu:
    def __init__(self, font):
        self.font = font
        self.easyButton = Button(100, 100, 100, 100, self.font, 'Easy', self.easyButtonClicked)
        self.mediumButton = Button(100, 250, 100, 100, self.font, 'Medium', self.mediumButtonClicked)
        self.hardButton = Button(100, 400, 100, 100, self.font, 'Hard', self.hardButtonClicked)
    
    def easyButtonClicked(self):
        print("Easy button clicked")
        self.easyButton.buttonText = self.font.render('Easy', True, self.easyButton.fillColors['pressed'])
        self.easyButton.alreadyPressed = True
        return 20
    
    def mediumButtonClicked(self):
        print("Medium button clicked")
        self.mediumButton.buttonText = self.font.render('Medium', True, self.mediumButton.fillColors['pressed'])
        self.mediumButton.alreadyPressed = True
        return 30
    
    def hardButtonClicked(self):
        print("Hard button clicked")
        self.hardButton.buttonText = self.font.render('Hard', True, self.hardButton.fillColors['pressed'])
        self.hardButton.alreadyPressed = True
        return 40
    
    def drawButtons(self, window):
        pos = pygame.mouse.get_pos()
        if self.easyButton.buttonRect.collidepoint(pos):
            self.easyButton.buttonText = self.font.render('Easy', True, self.easyButton.fillColors['hover'])
            if pygame.mouse.get_pressed()[0] and not self.easyButton.alreadyPressed:
                return self.easyButtonClicked()
        else:
            self.easyButton.buttonText = self.font.render('Easy', True, self.easyButton.fillColors['normal'])
            
        if self.mediumButton.buttonRect.collidepoint(pos):
            self.mediumButton.buttonText = self.font.render('Medium', True, self.mediumButton.fillColors['hover'])
            if pygame.mouse.get_pressed()[0] and not self.mediumButton.alreadyPressed:
                return self.mediumButtonClicked()
        else:
            self.mediumButton.buttonText = self.font.render('Medium', True, self.mediumButton.fillColors['normal'])
            
            
        if self.hardButton.buttonRect.collidepoint(pos):
            self.hardButton.buttonText = self.font.render('Hard', True, self.hardButton.fillColors['hover'])
            if pygame.mouse.get_pressed()[0] and not self.hardButton.alreadyPressed:
                return self.hardButtonClicked()
        else:
            self.hardButton.buttonText = self.font.render('Hard', True, self.hardButton.fillColors['normal'])
            
        if not pygame.mouse.get_pressed()[0]:
            self.easyButton.alreadyPressed = False
            self.mediumButton.alreadyPressed = False
            self.hardButton.alreadyPressed = False
            
        self.easyButton.draw(window)
        self.mediumButton.draw(window)
        self.hardButton.draw(window)
        return 0