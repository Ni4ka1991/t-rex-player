#agent module


#one hot encoding
UP    = [1, 0, 0, 0]
RIGHT = [0, 1, 0, 0]
DOWN  = [0, 0, 1, 0]
LEFT  = [0, 0, 0, 1]

ACTION = [
    UP,
    RIGHT,
    DOWN,
    LEFT
]

class Agent():
    def __init__( self ):
        pass


    def selectAction( self ):
       return DOWN 


