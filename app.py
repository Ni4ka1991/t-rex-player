#!/usr/bin/env python3



from enviroment import Enviroment

env = Enviroment()

env.render()
env.distance( env.player_coords, env.target_coords )

env.player_coords = [ 3, 3 ]
env.distance( env.player_coords, env.target_coords )
