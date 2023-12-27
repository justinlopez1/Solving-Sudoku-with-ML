from sudokugame.sudoku_generator import generate_sudoku
from data import cells_removed

def generate_board():

    data = generate_sudoku(9, cells_removed)
    target = data[1]
    data = data[0]
    

    for i in range(9):
        for j in range(9):
            dataNum = data[i][j]
            targetNum = target[i][j]
            data[i][j] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            target[i][j] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            if dataNum != 0:
                data[i][j][dataNum-1] = 1
            target[i][j][targetNum-1] = 1
    
    return data, target
    
    
    
def generate_empty():
    return [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]]