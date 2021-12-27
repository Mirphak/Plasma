# -*- coding: utf-8 -*-
'''
Module: Soccer.py
Age: Cleft with Jalak paged in
Date: December, 2012
Author: Stone (01141040)
E-mail: stone@stone-shard.com
This is a stripped version of the Cleft/Jalak Soccer Field.
'''
'''
Date: December, 2012
I dumped the matrix data for the columns into a dictionary.
Then made a simple warp to set up the field using that dictionary.
I'll try to add more when I have time. This should be sufficient to get you started.
'''

from Plasma import *


# This is a dictionary of column names and matrix data.
columnMap = {
    'columnPhys_00' : ((0.0, 0.0, 1.0, 47.0),
                       (0.0, 1.0, 0.0, 827.0),
                       (-1.0, 0.0, 0.0, 0.0),
                       (0.0, 0.0, 0.0, 1.0)),
    'columnPhys_01' : ((0.0, 0.0, 1.0, 112.6),
                       (0.0, 1.0, 0.0, 858.0),
                       (-1.0, 0.0, 0.0, 0.0),
                       (0.0, 0.0, 0.0, 1.0)),
    'columnPhys_02' : ((0.0, 0.0, 1.0, 41.4),
                       (0.0, 1.0, 0.0, 858.0),
                       (-1.0, 0.0, 0.0, 0.0),
                       (0.0, 0.0, 0.0, 1.0)),
    'columnPhys_03' : ((0.0, 0.0, 1.0, 107.0),
                       (0.0, 1.0, 0.0, 975.0),
                       (-1.0, 0.0, 0.0, -3.0),
                       (0.0, 0.0, 0.0, 1.0)),
    'columnPhys_04' : ((0.0, 0.0, 1.0, 47.0),
                       (0.0, 1.0, 0.0, 975.0),
                       (-1.0, 0.0, 0.0, -3.0),
                       (0.0, 0.0, 0.0, 1.0)),
    'columnPhys_05' : ((0.0, 0.0, 1.0, 107.0),
                       (0.0, 1.0, 0.0, 1122.0),
                       (-1.0, 0.0, 0.0, 0.0),
                       (0.0, 0.0, 0.0, 1.0)),
    'columnPhys_06' : ((0.0, 0.0, 1.0, 47.0),
                       (0.0, 1.0, 0.0, 1122.0),
                       (-1.0, 0.0, 0.0, 0.0),
                       (0.0, 0.0, 0.0, 1.0)),
    'columnPhys_07' : ((0.0, 0.0, 1.0, 112.6),
                       (0.0, 1.0, 0.0, 1092.0),
                       (-1.0, 0.0, 0.0, 0.0),
                       (0.0, 0.0, 0.0, 1.0)),
    'columnPhys_08' : ((0.0, 0.0, 1.0, 41.4),
                       (0.0, 1.0, 0.0, 1092.0),
                       (-1.0, 0.0, 0.0, 0.0),
                       (0.0, 0.0, 0.0, 1.0)),
    'columnPhys_09' : ((0.0, 0.0, 1.0, 107.0),
                       (0.0, 1.0, 0.0, 827.0),
                       (-1.0, 0.0, 0.0, 0.0),
                       (0.0, 0.0, 0.0, 1.0)),
    'columnPhys_10' : ((0.991790008545, 0.127877247334, 0.0, 140.0),
                       (0.0, 0.0, 1.0, 975.0),
                       (0.127877247334, -0.991790008545, 0.0, 0.0),
                       (0.0, 0.0, 0.0, 1.0)),
    'columnPhys_11' : ((0.991790008545, 0.127877247334, 0.0, 140.0),
                       (0.0, 0.0, 1.0, 1035.0),
                       (0.127877247334, -0.991790008545, 0.0, 0.0),
                       (0.0, 0.0, 0.0, 1.0)),
    'columnPhys_12' : ((1.0, 0.0, 0.0, 0.0),
                       (0.0, 1.0, 0.0, 0.0),
                       (0.0, 0.0, 1.0, -29.6),
                       (0.0, 0.0, 0.0, 1.0)),
    'columnPhys_13' : ((0.991790008545, 0.127877247334, 0.0, 140.0),
                       (0.0, 0.0, 1.0, 1095.0),
                       (0.127877247334, -0.991790008545, 0.0, 0.0),
                       (0.0, 0.0, 0.0, 1.0)),
    'columnPhys_14' : ((0.707106781006, 0.707106781006, 0.0, 17.0),
                       (-0.707106781006, 0.707106781006, 0.0, 861.0),
                       (0.0, 0.0, 1.0, 22.6),
                       (0.0, 0.0, 0.0, 1.0)),
    'columnPhys_15' : ((0.992420482635, -0.122888338566, 0.0, 14.0),
                       (0.0, 0.0, 1.0, 1095.0),
                       (-0.122888338566, -0.992420482635, 0.0, 0.0),
                       (0.0, 0.0, 0.0, 1.0)),
    'columnPhys_16' : ((0.707106781006, 0.707106781006, 0.0, 137.0),
                       (-0.707106781006, 0.707106781006, 0.0, 861.0),
                       (0.0, 0.0, 1.0, 22.6),
                       (0.0, 0.0, 0.0, 1.0)),
    'columnPhys_17' : ((0.707106781006, 0.707106781006, 0.0, 17.0),
                       (-0.707106781006, 0.707106781006, 0.0, 1089.0),
                       (0.0, 0.0, 1.0, 22.6),
                       (0.0, 0.0, 0.0, 1.0)),
    'columnPhys_18' : ((0.991790008545, 0.127877247334, 0.0, 140.0),
                       (0.0, 0.0, 1.0, 855.0),
                       (0.127877247334, -0.991790008545, 0.0, 0.0),
                       (0.0, 0.0, 0.0, 1.0)),
    'columnPhys_19' : ((0.991790008545, 0.127877247334, 0.0, 140.0),
                       (0.0, 0.0, 1.0, 915.0),
                       (0.127877247334, -0.991790008545, 0.0, 0.0),
                       (0.0, 0.0, 0.0, 1.0)),
    'columnPhys_20' : ((0.707106781006, 0.707106781006, 0.0, 137.0),
                       (-0.707106781006, 0.707106781006, 0.0, 1089.0),
                       (0.0, 0.0, 1.0, 22.6),
                       (0.0, 0.0, 0.0, 1.0)),
    'columnPhys_21' : ((0.992420482635, -0.122888338566, 0.0, 14.0),
                       (0.0, 0.0, 1.0, 855.0),
                       (-0.122888338566, -0.992420482635, 0.0, 0.0),
                       (0.0, 0.0, 0.0, 1.0)),
    'columnPhys_22' : ((0.992420482635, -0.122888338566, 0.0, 14.0),
                       (0.0, 0.0, 1.0, 915.0),
                       (-0.122888338566, -0.992420482635, 0.0, 0.0),
                       (0.0, 0.0, 0.0, 1.0)),
    'columnPhys_23' : ((0.992420482635, -0.122888338566, 0.0, 14.0),
                       (0.0, 0.0, 1.0, 975.0),
                       (-0.122888338566, -0.992420482635, 0.0, 0.0),
                       (0.0, 0.0, 0.0, 1.0)),
    'columnPhys_24' : ((0.992420482635, -0.122888338566, 0.0, 14.0),
                       (0.0, 0.0, 1.0, 1035.0),
                       (-0.122888338566, -0.992420482635, 0.0, 0.0),
                       (0.0, 0.0, 0.0, 1.0)),}
 

# Soccer.Field()
def Field():
    ''' Set up the field by warping the columns to the matrix data in the columnMap. '''
    for column in columnMap: # Go through the column names in the dictionary.
        object = PtFindSceneobject(column, 'Jalak') # Find a sceneobject from its name and age.
        matrix = ptMatrix44() # Create an empty matrix.
        matrix.setData(columnMap[column]) # Set the matrix to the data in the dictionary entry.
        object.netForce(1) # Force object messages to the network.
        object.physics.warp(matrix) # Warps the sceneobject to the matrix.


# Soccer.Ball()
def Ball():
    ''' Warp the ball to the center of the field. '''
    object = PtFindSceneobject('Sphere1', 'Jalak') # Find a sceneobject from its name and age.
    object.netForce(1) # Force object messages to the network.
    object.physics.warp(ptPoint3(77, 975, 1.75)) # Warp the sceneobject to the specified location.
    
