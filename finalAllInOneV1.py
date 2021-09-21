from cmu_graphics import *
from random import randint

# shapes (this is from shapes.py)
cube=[
[[0,0,0],[100,0,0],[100,100,0],[0,100,0]],
[[0,0,0],[0,0,100],[100,0,100],[100,0,0]],
[[100,0,0],[100,0,100],[100,100,100],[100,100,0]],
[[0,100,0],[0,100,100],[100,100,100],[100,100,0]],
[[0,0,0],[0,0,100],[0,100,100],[0,100,0]],
[[0,0,100],[100,0,100],[100,100,100],[0,100,100]]
]

diamond4=[
[[0,0,0],[-100,-100,100],[100,-100,100]],
[[0,0,0],[100,-100,100],[100,-100,-100]],
[[0,0,0],[100,-100,-100],[-100,-100,-100]],
[[0,0,0],[-100,-100,-100],[-100,-100,100]],
[[0,-200,0],[-100,-100,100],[100,-100,100]],
[[0,-200,0],[100,-100,100],[100,-100,-100]],
[[0,-200,0],[100,-100,-100],[-100,-100,-100]],
[[0,-200,0],[-100,-100,-100],[-100,-100,100]],
]

squishedDiamond4=[
[[200,0,0],[-100,-100,100],[100,-100,100]],
[[200,0,0],[100,-100,100],[100,-100,-100]],
[[200,0,0],[100,-100,-100],[-100,-100,-100]],
[[200,0,0],[-100,-100,-100],[-100,-100,100]],
[[200,-200,0],[-100,-100,100],[100,-100,100]],
[[200,-200,0],[100,-100,100],[100,-100,-100]],
[[200,-200,0],[100,-100,-100],[-100,-100,-100]],
[[200,-200,0],[-100,-100,-100],[-100,-100,100]],
]


verySquishedDiamond4=[
[[200,0,0],[-100,-100,100],[-50,-100,100]],
[[200,0,0],[-50,-100,100],[-50,-100,-100]],
[[200,0,0],[-50,-100,-100],[-100,-100,-100]],
[[200,0,0],[-100,-100,-100],[-100,-100,100]],
[[200,-200,0],[-100,-100,100],[-50,-100,100]],
[[200,-200,0],[-50,-100,100],[-50,-100,-100]],
[[200,-200,0],[-50,-100,-100],[-100,-100,-100]],
[[200,-200,0],[-100,-100,-100],[-100,-100,100]],
]



# shape processing functions (from shapeProcessing.py)

# finds the center of a polygon
def centFinder(polyCoords):
    centCoord = []
    posList=[]
    for c in range(3):
        posList = []
        for p in polyCoords:
            posList.append(p[c])
        centCoord.append(sum(posList)/len(posList))
    return(centCoord)

# finds the distance between 2 points
def distFinder(coord1,coord2):
    dist = ((coord2[0]-coord1[0])**2 + (coord2[1]-coord1[1])**2 + (coord2[2]-coord1[2])**2)**(1/2)
    return(dist)

# resizes a shape relative to (0,0,0)
def resize(faceList,x,y,z):
    resized = []
    for face in faceList:
        newFace = []
        for point in face:
            newFace.append([point[0]*x,point[1]*y,point[2]*z])
        resized.append(newFace)
    return(resized)

# translates a shape in the 3d space
def translate(faceList,x,y,z):
    moved = []
    for face in faceList:
        newFace = []
        for point in face:
            newFace.append([point[0]+x,point[1]+y,point[2]+z])
        moved.append(newFace)
    return(moved)

# creates a new shape from a given base shape
def newShape(source,xSize,ySize,zSize,xMove,yMove,zMove):
    temp = source
    temp = resize(temp,xSize,ySize,zSize)
    temp = translate(temp,xMove,yMove,zMove)
    faceList = temp
    return(faceList)


# code that runs all the functions and makes shapes and renders stuff (from render.py)

# light
lightSource=[600,-300,-200]
# view
camPos=[250,250,-600]

screen = [[0,0,0], [400,0,0], [400,400,0], [0,400,0]]

shapes = [cube]
finalList = []
colorList = []

# list of faces that need to be renderd
faceList = []

# list of distances
distList = []

finalList.append(newShape(cube, 0.2,2,8,100,300,0))
finalList.append(newShape(cube, 2,1,.4,0,180,100))
finalList.append(newShape(diamond4,0.7,1.2,0.7,300,300,200))
finalList.append(newShape(verySquishedDiamond4,0.7,1.2,0.2,100,100,400))

for c in range(30):
    colorList.append([randint(0,255),randint(0,255),randint(0,255)])


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