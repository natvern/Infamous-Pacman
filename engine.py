#    Project: The infamous Pacman
#    Name      : Samar Rahmouni
#    AndrewID  : srahmoun
#    File      : Back-end engine for the pacman game

import random

# We define pacman as a class
class Pacman:
    def __init__(self,board,xInitialPosition,yInitialPosition):
        self.board = board
        self.xPosition = xInitialPosition
        self.yPosition = yInitialPosition
        self.phase = False
        self.alive = True

    def movePacman(self,direction,x,y):
        if direction == "up":
            if self.board[self.xPosition-1][self.yPosition] != 2:
                self.move([self.xPosition-1,self.yPosition],x,y)
        elif direction == "down":
            if self.board[(self.xPosition+1)%21][self.yPosition] != 2:
                self.move([(self.xPosition+1)%21 ,self.yPosition],x,y)
        elif direction == "right":
            if self.board[self.xPosition][(self.yPosition+1)%21] != 2:
                self.move([self.xPosition, (self.yPosition+1)%21],x,y)
        elif direction == "left":
            if self.board[self.xPosition][self.yPosition-1] != 2:
                self.move([self.xPosition,self.yPosition-1],x,y)
        else:
            raise ValueError

    def move(self,destination,x,y):
        self.board[self.xPosition][self.yPosition] = 0
        self.board[destination[0]][destination[1]] = 1
        self.xPosition = destination[0]
        self.yPosition = destination[1]
        if x == self.xPosition and y == self.yPosition:
            self.alive = False

    def showBoard(self):
        for row in self.board:
            print(row, "\n")

# We define the monsters as another Class
class Monster():
    def __init__(self, board, xInitialPosition, yInitialPosition):
        self.board = board
        self.xPosition = xInitialPosition
        self.yPosition = yInitialPosition
        self.phase = False

    def moveMonster(self):
        directions = ["up", "down", "right", "left"]
        direction = directions[random.randint(0,3)]
        if direction == "up":
            if self.board[self.xPosition-1][self.yPosition] != 2:
                self.move((self.xPosition-1,self.yPosition))
            else:
                self.moveMonster()
        elif direction == "down":
            if self.board[(self.xPosition+1)%21][self.yPosition] != 2:
                self.move(( (self.xPosition+1)%21 ,self.yPosition))
            else:
                self.moveMonster()
        elif direction == "right":
            if self.board[self.xPosition][(self.yPosition+1)%21] != 2:
                self.move((self.xPosition, (self.yPosition+1)%21 ))
            else:
                self.moveMonster()
        elif direction == "left":
            if self.board[self.xPosition][self.yPosition-1] != 2:
                self.move((self.xPosition,self.yPosition-1))
            else:
                self.moveMonster()
        else:
            raise ValueError

    def move(self,destination):
        self.board[self.xPosition][self.yPosition] = 0
        self.board[destination[0]][destination[1]] = 5
        self.xPosition = destination[0]
        self.yPosition = destination[1]
