import torch
from torch import nn
import torch.optim as optim
from model import SudokuSolver
import pickle
 
epochs = 60000 #doing total 100,000
current_epoch = 0
learning_rate = .0001
batch_size = 10
device = "cuda" if torch.cuda.is_available() else "cpu"

cells_removed = 50

fileName = "models/CELossAdamOptimizer.obj"

filehandler = open(fileName, 'rb')  
net = pickle.load(filehandler)   #load existing net
#net = SudokuSolver()   #new net
net.to(device)

optimizer = optim.Adam(net.parameters(), lr=learning_rate) 
loss_func = nn.CrossEntropyLoss()