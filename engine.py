#    Project: The infamous Pacman
#    Name      : Samar Rahmouni
#    AndrewID  : srahmoun
#    File      : Back-end engine for the pacman game

# We define pacman as a class
class Pacman:
    def __init__(self,board,xInitialPosition,yInitialPosition):
        self.board = board
        self.xPosition = xInitialPosition
        self.yPosition = yInitialPosition

    def movePacman(self,direction):
        if direction == "up":
            if self.board[self.xPosition-1][self.yPosition] != 2:
                self.move((self.xPosition-1,self.yPosition))
        elif direction == "down":
            if self.board[self.xPosition+1][self.yPosition] != 2:
                self.move((self.xPosition+1,self.yPosition))
        elif direction == "right":
            if self.board[self.xPosition][self.yPosition+1] != 2:
                self.move((self.xPosition,self.yPosition+1))
        elif direction == "left":
            if self.board[self.xPosition][self.yPosition-1] != 2:
                self.move((self.xPosition,self.yPosition-1))
        else:
            raise ValueError

    def move(self,destination):
        self.board[self.xPosition][self.yPosition] = 0
        self.board[destination[0]][destination[1]] = 1
        self.xPosition = destination[0]
        self.yPosition = destination[1]


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
           "000023200000002320000" +  # Row 8
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
    board[i / 21][i % 21] = drawMap[i]

'''movement = raw_input()
while not movement.isvalid():
    movement = raw_input("Enter a valid movement: U, D, L or R.")
pacman.move()'''

