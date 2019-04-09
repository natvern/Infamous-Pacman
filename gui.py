#    Project: The infamous Pacman
#    Name      : Samar Rahmouni
#    AndrewID  : srahmoun
#    File      : Front-end Graphical User Interface for the infamous PacMan game

from tkinter import *

class GameFrame:
    # Initialize our first Frame
    def __init__(self,root,pacman,monster):
        # Loading the engine
        self.engine = pacman
        self.enemy = monster
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
        sprites = {0: self.empty,
                   1: self.pacman,
                   2: self.wall,
                   3: self.circle,
                   4: self.goal,
                   5: self.monster}
        board = self.engine.board
        for i in range(21):
            for j in range(21):
                self.canvas.create_image(j*21, i*21, image=sprites[board[i][j]])
        
    def playGame(self, event):
        if self.engine.alive:
            self.translateInput(event)
            self.setupBoard()

    def translateInput(self, keyPressed):
        if keyPressed.keysym == "w":
            self.engine.movePacman("up",self.enemy.xPosition,self.enemy.yPosition)
        elif keyPressed.keysym == "a":
            self.engine.movePacman("left",self.enemy.xPosition,self.enemy.yPosition)
        elif keyPressed.keysym == "d":
            self.engine.movePacman("right",self.enemy.xPosition,self.enemy.yPosition)
        elif keyPressed.keysym == "s":
            self.engine.movePacman("down",self.enemy.xPosition,self.enemy.yPosition)

    def monsterMoves(self):
        if self.engine.alive:
            self.enemy.moveMonster()
            self.setupBoard()
            self.canvas.after(self.timerDelay, self.monsterMoves)

