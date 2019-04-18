#    Project: The infamous Pacman
#    AndrewID  : srahmoun

#    Created: 11/25/2018
#    Modification History:
#    11/25/2018 - 20:29   
#    04/02/2019 - 19:00 
#    04/04/2019 - 14:49
#               - 17:54
#    04/16/2019 - 17:36
#    04/18/2019 - 13:47

import gui, engine
import tkinter

root = tkinter.Tk()

# Defining the board as a list A where each index contains a list B
# Every list B is equivalent to a row where each index is a column
# This is a 21x21 board
board = []
for i in range(21):
    board.append([])
    for j in range(21):
        board[i].append("0")

# We associate numbers from 0 to 4 to a certain object
# 0 = empty, 1 = pacman, 2 = wall, 3 = circle, 4 = goal
# We will now create the map
drawMap = ("022222222222222222220" +  # Row 1
           "023333333323333333320" +  # Row 2
           "024223222323222322420" +  # Row 3
           "023333333333333333320" +  # Row 4
           "023223232222232322320" +  # Row 5
           "023333233323332333320" +  # Row 6
           "022223222020222322220" +  # Row 7
           "000023200050002320000" +  # Row 8
           "222223202222202322222" +  # Row 9
           "000003002000200300000" +  # Row 10
           "222223202222202322222" +  # Row 11
           "000023200000002320000" +  # Row 12
           "022223202222202322220" +  # Row 13
           "023333333323333333320" +  # Row 14
           "023223222323222322320" +  # Row 15
           "024323333313333323420" +  # Row 16
           "022323232222232323220" +  # Row 17
           "023333233323332333320" +  # Row 18
           "023222222323222222320" +  # Row 19
           "023333333333333333320" +  # Row 20
           "022222222222222222220")  # Row 21

# Then we will assign it to the board
for i in range(21 * 21):
    board[i // 21][i % 21] = int(drawMap[i])

infamousPac = engine.Pacman(board, 15, 10)
frame = gui.GameFrame(root, infamousPac)
root.mainloop()

