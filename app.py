#!/usr/bin/env python3
from enviroment import Enviroment
from time import sleep

env = Enviroment()

for s in range( 20 ):
    env.render()
    env.distance( env.player_coords, env.target_coords )
    env.step()
    sleep(.5)
