#module Enviroment

from os import system

class Enviroment:

    def __init__():
        self.reset()

    def reset( self ):
        self.player_coords = [ 0, 0 ]
        self.target_coords = [ 4, 4 ]
        self.player_score  = 0 
        self.done          = False

    def render( self ):
        system( "clear" )
        for y in range(5):
            for x in range(5):
                if [ x, y ] == self.player_coords:
                    print("P", end = " " )
                elif [ x, y ] == self.target_coords:
                    print("T", end = " " )
                else:
                    print(" ", end = " " )
            print()
        print( "-"*10 )
        print( f"score = {self.player_score}" )
