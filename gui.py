#    Project: The infamous Pacman
#    Name      : Samar Rahmouni
#    AndrewID  : srahmoun
#    File      : Front-end Graphical User Interface for the infamous PacMan game

from tkinter import *
from engine import Monster

class GameFrame:
    # Initialize our first Frame
    def __init__(self,root,pacman):
        # Loading the engine
        self.engine = pacman
        self.enemies = [Monster(pacman.board, 9, 7), Monster(pacman.board, 10, 7)]
        self.enemy = self.enemies[0]
        # Initialize frame
        self.root = root
        self.playFrame = Frame(self.root,width=415,height=415)
        # Initialize canvas
        self.canvas = Canvas(self.playFrame, width=415, height=415)
        # Loading sprites
        self.empty = PhotoImage(file="empty.gif")
        self.pacman = PhotoImage(file="pacmansprite.gif")
        self.wall = PhotoImage(file="wall.gif")
        self.circle = PhotoImage(file="circle.gif")
        self.goal = PhotoImage(file="goal.gif")
        self.monster = PhotoImage(file="monster.gif")
        self.sprites = {0: self.empty,
                        1: self.pacman,
                        2: self.wall,
                        3: self.circle,
                        4: self.goal,
                        5: self.monster}
        # Setting up Events
        self.root.bind("<Key>", self.playGame)
        self.timerDelay = 300
        self.monsterMoves()
        # Setup the board
        self.playFrame.pack()
        self.canvas.pack(expand=YES, fill=BOTH)
        self.setupBoard()

    # We will setup the board by associating every board number to the sprite
    def setupBoard(self):
        board = self.engine.board
        for i in range(21):
            for j in range(21):
                self.canvas.create_image(j*21, i*21, image=self.sprites[board[i][j]])

    # We start playing the game by translating the input    
    def playGame(self, event):
        if self.engine.alive:
            self.translateInput(event)
            self.setupBoard()

    def translateInput(self, keyPressed):
        if keyPressed.keysym in "wads":
            self.engine.board[self.enemy.xPosition][self.enemy.yPosition] = 0
            self.canvas.create_image(self.engine.xPosition * 21, self.engine.yPosition * 21, image=self.sprites[0])
        # Moving up
        if keyPressed.keysym == "w":
            self.engine.movePacman("up",self.enemy.xPosition,self.enemy.yPosition)
        # Moving left
        elif keyPressed.keysym == "a":
            self.engine.movePacman("left",self.enemy.xPosition,self.enemy.yPosition)
        # Moving right
        elif keyPressed.keysym == "d":
            self.engine.movePacman("right",self.enemy.xPosition,self.enemy.yPosition)
        # Moving down
        elif keyPressed.keysym == "s":
            self.engine.movePacman("down",self.enemy.xPosition,self.enemy.yPosition)

        if keyPressed.keysym in "wasd":
            self.canvas.create_image(self.engine.xPosition * 21, self.engine.yPosition * 21, image=self.sprites[1])
        

    def monsterMoves(self):
        for i in range(len(self.enemies)):
            self.enemy = self.enemies[i]
            if self.engine.alive:
                self.canvas.create_image(self.enemy.xPosition * 21, self.enemy.yPosition * 21, image=self.sprites[0])
                self.engine.board[self.enemy.xPosition][self.enemy.yPosition] = 0
                self.enemy.moveMonster()
                self.canvas.create_image(self.enemy.xPosition * 21, self.enemy.yPosition * 21, image=self.sprites[5])
                #self.setupBoard()
                self.canvas.after(self.timerDelay, self.monsterMoves)

