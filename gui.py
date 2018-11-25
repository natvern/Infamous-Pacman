#    Project: The infamous Pacman
#    Name      : Samar Rahmouni
#    AndrewID  : srahmoun
#    File      : Front-end Graphical User Interface for the infamous PacMan game

import * from Tkinter

class GameFrame:
    # Initialize our first Frame
    def __init__(self,root,pacman):
        # Loading sprites
        self.empty = PhotoImage(file="empty.gif")
        self.pacman = PhotoImage(file="pacmansprite.gif")
        self.wall = PhotoImage(file="wall.gif")
        self.circle = PhotoImage(file="circle.gif")
        self.goal = PhotoImage(file="goal.gif")
        # Loading the engine
        self.engine = pacman
        # Initialize frame
        self.root = root
        self.playFrame = Frame(root,width=210,height=210)
        self.playFrame.pack()
        # Setup the board
        self.setupBoard()
        # Start game
        self.root.after(60,self.startGame)

    # We will setup the board by associating every board number to the sprite
    def setupBoard(self):
        sprites = {0: self.empty,
                   1: self.pacman,
                   2: self.wall,
                   3: self.circle,
                   4: self.goal}
        board = self.pacman.board
        for i in range(21):
            for j in range(21):
                sprites[board[i][j]].grid(row=i, column=j)

    def startGame(self):
        self.root.after(60,startGame)
