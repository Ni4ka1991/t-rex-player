#module Enviroment

from os import system
import math

class Enviroment:

    def __init__( self ):
        self.reset()

    def reset( self ):
        self.player_coords = [ 0, 0 ]
        self.target_coords = [ 4, 4 ]
        self.player_score  = 0 
        self.done          = False

    def render( self ):
        system( "clear" )
        print( "_"*11 )
        for y in range(5):
            print( "|", end = '' )
            for x in range(5):
                if [ x, y ] == self.player_coords:
                    print("P", end = "|" )
                elif [ x, y ] == self.target_coords:
                    print("T", end = "|" )
                else:
                    print(" ", end = "|" )
            print()
            print( "_" * 11 )
        print( f"score = {self.player_score}" )


    def distance( self, point1, point2 ):
        dist = math.sqrt(( point1[0] - point2[0])**2 + ( point1[1] - point2[1])**2 ) 
        print( f"distance:", dist )
        return dist
#        return math.sqrt(( point1[0] - point2[0])**2 + ( point1[1] - point2[1])**2 ) 


    def step( self, action = None ):
        self.player_coords[0] += 1
