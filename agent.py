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
        self.last_state = None   #short memory


    def selectAction( self ):
        return DOWN 

    
    def rememberState( self, state ):
        self.last_state = state
