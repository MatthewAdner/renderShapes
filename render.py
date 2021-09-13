from shapes import *
from shapeProcessing import *
from cmu_graphics import *
# light
lightSource=[600,-300,-200]
# view
camPos=[200,200,-400]

screen = [[0,0,0], [400,0,0], [400,400,0], [0,400,0]]

shapes = [cube]


# list of faces that needs to be renderd
faceList = []

# list of distances
distList = []

# puts faces in faceList
for shape in shapes:
    for face in shape:
        faceList.append(face)

# adds the center point to the end of each coordinate
for face in range(len(faceList)):
    faceList[face].append(centFinder(faceList[face]))

# adds the distance from the point to the camera of each face to distList    
for face in range(len(faceList)):
    distList.append(distFinder(faceList[face][-1], camPos))

# zipps distList and faceList together so facelist and can be sorted with distList
zipped = list(zip(distList, faceList))

# sorts the zipped lists. Since distList comes first in the tuples, that is what it is sorted by
zipped.sort()

# unzips the lists and puts them into their former lists homes, this time in order
distList, faceList = zip(*zipped)
for face in range(len(faceList)):
    faceList[face].pop()

# now that the faces have been ordered, we know which order to draw them in
# now we must draw them. This will be done by doing projections
# we have a screen rectangle, effectively a plane.
# we will draw line between each point of a given face and the camera
#   we will see where this line intersects with the screen plane
#   we will use this point as our 2D coordinates.
#   these points will have their third value (the z coordinate) dropped and will be put into a new list
#   this will then be put into the notation of CS1's graphics library and outputted as a text file

# DONE
# for the projection work, we will write an equation for each line
# We will then find where the line's z coordinate intersects with the z value held by the screen plane

# calculates the values of the x and y coordinates given the z coordinate of the screen and the values of the points at the end of the lines
def projector(point1,point2,zVal):
    x = (((zVal-point1[2])/(point2[2]-point1[2]))*(point2[0]-point1[0])+point1[0])
    y = (((zVal-point1[2])/(point2[2]-point1[2]))*(point2[1]-point1[1])+point1[1])
    return([x,y])

renderFaces = []


for face in faceList:
    face2d = []
    for point in face:
        face2d.append(projector(point, camPos, 0))
    renderFaces.append(face2d)


# did you know that you can pass the values from a list into a function by writing the list as *listName instead of listName COOL right?

print(renderFaces)
renderPoly = []
for face in renderFaces:
    temp = []
    for point in face:
        for num in point:
            temp.append(num)
    renderPoly.append(temp)

# final rendering of cube
for poly in renderPoly:
    Polygon(*poly,fill=None,border='purple')
#Polygon(*renderPoly[1],fill=None,border='purple')

#print('\n\n\n', renderPoly)

'''
final = []
for face in renderFaces:
    temp = []
    for point in face:
        temp.append(point)
    #Rect(temp,fill=None)
print(renderFaces)
r = [200.251531,150.201321,300.123,115,223.123413,315.12312]
#Polygon(r[0],r[1],r[2],r[3],r[4],r[5],r[6],fill=None,border='black')
#Polygon(200.251531,150.201321,300.123,115,223.123413,315.12312,fill=None,border='black')
#Polygon(*r,fill=None,border='black')
#Polygon(0,0,100,0,100,100)
'''












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



def flatCoordFinder(coord):
    # field of view (FOV) will be 90 degrees
    # camera will be located at 200,200,-200
    fCoord='2d coordinate'
    return fCoord

