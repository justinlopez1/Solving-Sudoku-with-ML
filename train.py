from train_model import train_epoch
from model import SudokuSolver
from data import *
import pickle

net.train()

print("Training on", device)

for epoch in range(current_epoch, epochs): 
    loss = train_epoch(device, net, optimizer, loss_func, batch_size)
    if (epoch+1) % 100 == 0:
        print("Epoch: {: >8} Loss: {}".format(epoch+1, loss))
        filehandler = open(fileName, 'wb') 
        pickle.dump(net, filehandler) #save net every 100 epochs    
    



