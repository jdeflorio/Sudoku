import pygame
import sys
from tkinter import *
from tkinter import messagebox

WHITE = (255,255,255)
LIGHTGRAY = (200,200,200)
BLACK = (0,0,0)
SCREENWIDTH = 900
SCREENHEIGHT = 900
CELLSIZE = SCREENWIDTH//9
BOXSIZE = SCREENWIDTH//3

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption("Sudoku")
    screen.fill(WHITE)
    drawGridLines(screen)

    """
    grid = [ [5, 3, 4, 6, 7, 8, 9, 1, 2],
             [6, 7, 2, 1, 9, 5, 3, 4, 8],
             [1, 9, 8, 3, 4, 2, 5, 6, 7],
             [8, 5, 9, 7, 6, 1, 4, 2, 3],
             [4, 2, 6, 8, 5, 3, 7, 9, 1],
             [7, 1, 3, 9, 2, 4, 8, 5, 6],
             [9, 6, 1, 5, 3, 7, 2, 8, 4],
             [2, 8, 7, 4, 1, 9, 6, 3, 5],
             [3, 4, 5, 2, 8, 6, 1, 7, 9]
             ]
    """
    grid = createGrid("grid1.txt")

    drawBoxNums(screen, grid)

    pygame.display.update()



    canChangeBox = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                mousex, mousey = event.pos
                canChangeBox = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if isGridCorrect(grid):
                        Tk().wm_withdraw()
                        messagebox.showinfo('Checker','Correct')
                    else:
                        Tk().wm_withdraw()
                        messagebox.showinfo('Checker','Wrong')
            if (event.type == pygame.KEYDOWN) and canChangeBox:
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    updateGrid(mousex, mousey, 1, grid, screen)
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    updateGrid(mousex, mousey, 2, grid, screen)
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    updateGrid(mousex, mousey, 3, grid, screen)
                if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    updateGrid(mousex, mousey, 4, grid, screen)
                if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    updateGrid(mousex, mousey, 5, grid, screen)
                if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    updateGrid(mousex, mousey, 6, grid, screen)
                if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    updateGrid(mousex, mousey, 7, grid, screen)
                if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    updateGrid(mousex, mousey, 8, grid, screen)
                if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    updateGrid(mousex, mousey, 9, grid, screen)
                if event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                    updateGrid(mousex, mousey, 0, grid, screen)
                canChangeBox = False












def createGrid(file):
    grid = [[0 for x in range(9)] for y in range(9)]
    f = open(file, "r")
    row = 0
    for line in f:
        column = 0
        for ch in line:
            if ch != '\n':
                grid[row][column] = int(ch)
                column = column + 1
        row = row + 1
    return grid




def isGridCorrect(grid):
    #check horizontal
    for row in range(len(grid)):
        checkDict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
        for column in range(len(grid[row])):
            if grid[row][column] == 0:
                return False
            checkDict[grid[row][column]] = checkDict[grid[row][column]] + 1
            if checkDict[grid[row][column]] > 1:
                return False
    #check vertical
    for column in range(len(grid[0])):
        checkDict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
        for row in range(len(grid)):
            if grid[row][column] == 0:
                return False
            checkDict[grid[row][column]] = checkDict[grid[row][column]] + 1
            if checkDict[grid[row][column]] > 1:
                return False
    return True

def updateGrid(xpos, ypos, value, gameGrid, screen):
    #find pos on grid
    row = int(ypos/CELLSIZE)
    column = int(xpos/CELLSIZE)
    gameGrid[row][column] = value
    screen.fill(WHITE)
    drawGridLines(screen)
    drawBoxNums(screen, gameGrid)
    pygame.display.update()


def drawBoxNums(gameScreen, gameGrid):
    font = pygame.font.Font('freesansbold.ttf', 120)
    y = 0
    for row in range(len(gameGrid)):
        column = 0
        for i in range(0, SCREENWIDTH, CELLSIZE):
            if gameGrid[row][column] > 0:
                text = font.render(str(gameGrid[row][column]), True, BLACK)
                textRect = text.get_rect()
                textRect.x = i + 15
                textRect.y = y
                blit = gameScreen.blit(text, textRect)
            column = column + 1
        y = y + CELLSIZE



def drawGridLines(gameScreen):
    #draws cell lines in light gray
    for i in range(0, SCREENWIDTH, CELLSIZE):
        pygame.draw.line(gameScreen, LIGHTGRAY, (i,0), (i, SCREENHEIGHT))
    for i in range(0, SCREENHEIGHT, CELLSIZE):
        pygame.draw.line(gameScreen, LIGHTGRAY, (0,i), (SCREENWIDTH, i))
    #draws box lines in black
    for i in range(0, SCREENWIDTH, BOXSIZE):
        pygame.draw.line(gameScreen, BLACK, (i,0), (i, SCREENHEIGHT))
    for i in range(0, SCREENHEIGHT, BOXSIZE):
        pygame.draw.line(gameScreen, BLACK, (0,i), (SCREENWIDTH, i))



main()
