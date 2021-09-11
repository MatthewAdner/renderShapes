from shapes import *
from shapeProcessing import *
from math import sqrt
#light
lightSource=(600,-300,-200)
#view
camPos=(200,200,-200)

shapes = [cube]
#TODO
# function to find average of coordinates in each face
# make list of faces
# go through the list of faces and find the angle of reflection from the light source to the camera
#   all the color values of the shapes by (angle/45) maybe try 90 if it doesn't look right
# sort the list
# find 2d coorinates to be drawn
# draw polygons

#TODO later
#   made a function to rotate the coordinates around the center of all the coordinatges in a shape

# find the angle of reflection of the light source from a face. 
def angleFinder():
    angle = 'an angle'
    return angle



# list of faces that needs to be renderd
faceList = []

# puts faces in faceList
for shape in shapes:
    for face in shape:
        faceList.append(shapeProcess(face, (0, 173, 239)))

# function to find the distance between two points
def distFinder(cam, point):
    sqrt((cam[0]**2-point[0]**2)+(cam[1]**2-point[1]**2)+(cam[2]**2-point[2]**2))
print(shapes[0][0])
# a list of distances 
distList = []

# adds the distances to the list
for face in faceList:
    distList.append(distFinder(camPos,face[-2]))

# rarange faceList by distList 
print(distList[0:5])


def flatCoordFinder(coord):
    # field of view (FOV) will be 90 degrees
    # camera will be located at 200,200,-200
    fCoord='2d coordinate'
    return fCoord

