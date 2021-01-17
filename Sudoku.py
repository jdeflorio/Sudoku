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
    grid = createGrid("grid3.txt")

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
                if event.key == pygame.K_s:
                    solveGrid(grid, screen)
            if (event.type == pygame.KEYDOWN) and canChangeBox:
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    updateGrid(grid, screen, mousex, mousey, 1)
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    updateGrid(grid, screen, mousex, mousey, 2)
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    updateGrid(grid, screen, mousex, mousey, 3)
                if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    updateGrid(grid, screen, mousex, mousey, 4)
                if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    updateGrid(grid, screen, mousex, mousey, 5)
                if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    updateGrid(grid, screen, mousex, mousey, 6)
                if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    updateGrid(grid, screen, mousex, mousey, 7)
                if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    updateGrid(grid, screen, mousex, mousey, 8)
                if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    updateGrid(grid, screen, mousex, mousey, 9)
                if event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                    updateGrid(grid, screen, mousex, mousey, 0)
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





def updateGrid(gameGrid, screen, xpos=-1, ypos=-1, value=-1):
    if xpos != -1 and ypos != -1:
        #find pos on grid
        row = int(ypos/CELLSIZE)
        column = int(xpos/CELLSIZE)
        gameGrid[row][column] = value
    screen.fill(WHITE)
    drawGridLines(screen)
    drawBoxNums(screen, gameGrid)
    pygame.display.update()

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


def findEmpty(gameGrid):
    for row in range(len(gameGrid)):
        for column in range(len(gameGrid[row])):
            if gameGrid[row][column] == 0:
                return (row, column)
    return (-1, -1)
                    

def isValid(gameGrid, square, num):
    for i in range(len(gameGrid)):
        if gameGrid[square[0]][i] == num and i != square[1]:
            return False
    
    for i in range(len(gameGrid)):
        if gameGrid[i][square[1]] == num and i != square[0]:
            return False

    boxRow = square[0] // 3
    boxColumn = square[1] // 3
    
    for i in range(boxRow*3, boxRow*3 + 3):
        for j in range(boxColumn*3, boxColumn*3 + 3):
            if gameGrid[i][j] == num and (i, j) != square:
                return False

    return True
        
def solveGrid(gameGrid, screen):
    emptySquare = findEmpty(gameGrid) #returns (row, column) of empty square
    if emptySquare == (-1, -1):
        return True             #check if grid is full
    else:
        for i in range(1, 10):
            if isValid(gameGrid, emptySquare, i):       #see if a number can fit in square 
                gameGrid[emptySquare[0]][emptySquare[1]] = i
                updateGrid(gameGrid, screen)
                if solveGrid(gameGrid, screen):         #recursivly check new grid, if new grid is full then returns true
                    return True
                else:                                   #if new check iterates thorugh 1-9 and does not find a value that fits, replaces square with zero and returns false to backtrack
                    gameGrid[emptySquare[0]][emptySquare[1]] = 0
                    updateGrid(gameGrid, screen)
    return False                    


main()
