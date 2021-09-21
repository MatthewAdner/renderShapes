from typing import final
from shapes import *
from shapeProcessing import *
from cmu_graphics import *
from random import randint

# FUTURE IDEAS FOR THIS
#   shading
#   rotatable objects


# light
lightSource=[600,-300,-200]
# view
camPos=[250,250,-600]

screen = [[0,0,0], [400,0,0], [400,400,0], [0,400,0]]

shapes = [cube]
finalList = []
colorList = []

# list of faces that needs to be renderd
faceList = []

# list of distances
distList = []

# puts faces in faceList
'''for shape in shapes:
    for face in shape:
        faceList.append(face)

faceList = resize(faceList, .2,2.2,1.75)
faceList = translate(faceList, 100,100,0)'''
'''faceList = newShape(cube, 0.2,2,8,100,300,0)
faceList2 = newShape(cube, 2,1,.4,0,180,100)
finalList.append(faceList)
finalList.append(faceList2)'''

finalList.append(newShape(cube, 0.2,2,8,100,300,0))
finalList.append(newShape(cube, 2,1,.4,0,180,100))
finalList.append(newShape(diamond4,0.7,1.2,0.7,300,300,200))
finalList.append(newShape(verySquishedDiamond4,0.7,1.2,0.2,100,100,400))
#finalList.append()

for c in range(30):
    colorList.append([randint(0,255),randint(0,255),randint(0,255)])

'''
print(faceList,'\n\n\n\n')
print(temp)
'''


# adds the center point to the end of each coordinate
for faceList in range(len(finalList)):
    for face in range(len(finalList[faceList])):
        finalList[faceList][face].append(centFinder(finalList[faceList][face]))
print(finalList,'\n\n') # this one's ballin!

# adds the distance from the point to the camera of each face to distList    
for faceList in range(len(finalList)):
    for face in range(len(finalList[faceList])):
        distList.append(distFinder(finalList[faceList][face][-1], camPos))
print(len(finalList[0]),len(finalList[1])) # ballin
print(len(distList))
# zipps distList and faceList together so facelist and can be sorted with distList
superFinalList = []
for e in finalList:
    for a in e:
        superFinalList.append(a)

zipped = zip(distList, superFinalList)
lZipped = list(zipped)

# sorts the zipped lists. Since distList comes first in the tuples, that is what it is sorted by
lZipped.sort()

# unzips the lists and puts them into their former lists homes, this time in order
distList, faceList = zip(*lZipped)
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
renderFaces.reverse()

# did you know that you can pass the values from a list into a function by writing the list as *listName instead of listName COOL right?

#print(renderFaces)
renderPoly = []
for face in renderFaces:
    temp = []
    for point in face:
        for num in point:
            temp.append(num)
    renderPoly.append(temp)
k = 0

# render background
Rect(0,0,400,400,fill=gradient(rgb(200,240,255),rgb(160,210,235),start='center'))


# final rendering of cube
for poly in renderPoly:
    Polygon(*poly,fill=rgb(*(colorList[k%len(colorList)])),border='black',opacity=70, borderWidth = .5)
    k += 1
    #rgb(*(colorList[k%len(colorList)]))
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


