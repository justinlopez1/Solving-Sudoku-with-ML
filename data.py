import torch
from torch import nn
import torch.optim as optim
from model import SudokuSolver
import pickle

epochs = 500000
learning_rate = .0001
batch_size = 5
device = "cuda" if torch.cuda.is_available() else "cpu"

cells_removed = 40

fileName = "models/CELossAdamOptimizer.obj"

filehandler = open(fileName, 'rb')  
net = pickle.load(filehandler)   #load existing net
#net = SudokuSolver()   #new net
net.to(device)


optimizer = optim.Adam(net.parameters(), lr=learning_rate) 
loss_func = nn.CrossEntropyLoss()