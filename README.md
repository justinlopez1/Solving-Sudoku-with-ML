# Solving-Sudoku-with-ML
Solving Sudoku Boards Using a CNN created with pytorch!!! 

Info
- To train a net run the train.py file, to test a net run the test.py file. Net, epochs, batch size, lr, loss and optimizer functions, and more, can all be specified in the daya.py file.
- To load and store nets I use pickle. Every 100 epochs the model will be stored in the specified file in the fileName variable in the data.py file
- To create a new net create an instance of the SudokuSolver class.

Notes
- Our way of generating boards from the prog 1 project is creating boards without a unique solution, meaning there are multiple correct solutions.
- To get around this all i did was get a sudoku validator function from geeks for geeks.
- This also means that we are training on these faulty boards, so to optimize this we should be using a better dataset like the one from kaggle.

- Tested using both ReLU and Sigmoid, best accuracy was ReLU with aorund 92% correctly getting boards, with 50 cells not filled in
- Like others I also found that allowing the nn to fill in clues one at a time based on the best guess has way more success than having it guess an entire board at once.

- Followed the same general model from the following article: https://medium.com/analytics-vidhya/how-to-solve-sudoku-with-convolutional-neural-networks-cnn-c92be8830c52
- I also tested using a normal nn, different activation, and different loss/optimizers and found that the one from the article has been working the best.
- If anyone wants to i think it would be cool to change the amount of nodes in the hidden layers, as well as changing the amount of layers.
- Something similar has been done in this work, which is also mentioned throughout the article that was above: https://cs230.stanford.edu/files_winter_2018/projects/6939771.pdf
