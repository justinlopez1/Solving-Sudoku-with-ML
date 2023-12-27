import torch
from torchvision.transforms import ToTensor
from data_preprocess import generate_board


def train_epoch(device, net, optimizer, loss_func, batch_size):
    runningLoss = 0.0
    for i in range(batch_size):
        data, target = generate_board()
        data = torch.tensor(data, dtype=torch.float32).to(device)
        target = torch.tensor(target, dtype=torch.float32).to(device)
        
        data = data.unsqueeze(0)
        output = net(data)
        output = torch.squeeze(output)
        
        optimizer.zero_grad()
        loss = loss_func(output, target)
        loss.backward()
        optimizer.step()
        
        runningLoss += loss.item()
    
    return runningLoss / batch_size