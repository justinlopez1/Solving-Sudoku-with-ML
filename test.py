from train_model import train_epoch
from model import SudokuSolver
from data import *
from data_preprocess import generate_board
from data_preprocess import generate_empty
from validator import isValidSudoku
import pickle

def full(data):
    for row in data:
        for num in row:
            if num == 0:
                return False
    return True

softMax = nn.Softmax(dim=1)

net.eval()
test_count = 100
passed = 0

print("Testing", fileName, "on", device)

for test_index in range(test_count):
    dataList, target = generate_board()
    dataTensor = torch.tensor(dataList, dtype=torch.float32).to(device)
    targetTensor = torch.tensor(target, dtype=torch.float32).to(device)
    
    dataTensor = dataTensor.squeeze(0)
    
    finalOutput = generate_empty()
    targetList = generate_empty()
    
    for i in range(9):
        for j in range(9):
            if dataTensor[i][j].max(0, keepdim=True)[0].item() > 0:
                finalOutput[i][j] = dataTensor[i][j].max(0, keepdim=True)[1].item()+1
            else:
                finalOutput[i][j] = 0
            targetList[i][j] = targetTensor[i][j].max(0, keepdim=True)[1].item()+1
                
    guessIndex = 0 
    while not full(finalOutput):
        dataTensor = dataTensor.unsqueeze(0)
        output = net(dataTensor)
        dataTensor = dataTensor.squeeze(0)
        output = torch.squeeze(output)
        output = softMax(output)
        
        guessI = 0
        guessJ = 0
        guessNum = 0
    
        for i in range(9):
            for j in range(9):
                if finalOutput[i][j] == 0 and output[i][j].max(0, keepdim=True)[0].item() > guessNum:
                    guessI = i
                    guessJ = j
                    guessNum = output[i][j].max(0, keepdim=True)[0].item()
                    
        guess = output[guessI][guessJ].max(0, keepdim=True)[1].item()+1
        finalOutput[guessI][guessJ] = guess
        dataTensor[guessI][guessJ][guess-1] = 1

        guessIndex += 1
   
    if isValidSudoku(finalOutput):
        passed += 1
        print("Test", test_index, "passed")
    
print()
print("Tests passed:", passed, "/", test_count)