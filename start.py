from coords import *

'''Read map in and check if block is barrel'''
def check_barrel(x, y, MAP):

    with open('map_'+str(MAP)+'.txt') as file:

        rows = file.readlines()
        
        block = int(rows[y].strip()[x])
        
        return bool(block)           

'''Generate initializer data fro blocks'''
def gen_blocks(MAP):

    for i in range(13):
    
        for j in range(13):

            ends = (i in (0, 12)) or (j in (0, 12))
            
            even = (i % 2 == 0) and (j % 2 == 0)

            if ends or even:

                x, y = coords_pixels((i, j))
                
                yield (x, y, 'ROCK')

            elif check_barrel(i, j, MAP):

                x, y = coords_pixels((i, j))

                yield (x, y, 'BARR')

            else:

                x, y = coords_pixels((i, j))
                
                yield (x, y, 'WALK')

'''Generate initializer data for blocks'''
def gen_players(num_players):

    start_coords = [(1, 1), (11, 11), (1, 11), (11, 1)]

    for ID in range(num_players):

        i = start_coords[ID][0]
        j = start_coords[ID][1]

        x, y = coords_pixels((i, j))

        yield (x, y, ID)

'''Generate rails for movement to be checked against'''
def gen_rail():

    for i in range(1, 12):

        if i % 2 != 0:

            yield i
