from shapes import *

# a funtion to find the center of a 
def centFinder(polyCoords):
    centCoord = []
    posList=[]
    for c in range(3):
        posList = []
        for p in polyCoords:
            posList.append(p[c])
        centCoord.append(sum(posList)/len(posList))
    return(centCoord)
            
'''
poly = [[15,0,0],[112,0,19],[100.2,100,0],[0,100,296.15]]
print(centFinder(poly))
'''

def distFinder(coord1,coord2):
    dist = ((coord2[0]-coord1[0])**2 + (coord2[1]-coord1[1])**2 + (coord2[2]-coord1[2])**2)**(1/2)
    return(dist)

'''
cent1 = centFinder(cube[0])
cent2 = centFinder(cube[1])
dist = distFinder(cent1,cent2)
print(dist)
'''

def resize(faceList,x,y,z):
    resized = []
    for face in faceList:
        newFace = []
        for point in face:
            newFace.append([point[0]*x,point[1]*y,point[2]*z])
        resized.append(newFace)
    return(resized)

def translate(faceList,x,y,z):
    moved = []
    for face in faceList:
        newFace = []
        for point in face:
            newFace.append([point[0]+x,point[1]+y,point[2]+z])
        moved.append(newFace)
    return(moved)
            
def newShape(source,xSize,ySize,zSize,xMove,yMove,zMove):
    temp = source
    temp = resize(temp,xSize,ySize,zSize)
    temp = translate(temp,xMove,yMove,zMove)
    faceList = temp
    return(faceList)

























'''
# finds the center of each face and adds a color
def process(shape, color):
    for face in range(len(shape)):
        tx=0
        ty=0
        tz=0
        txlist=[]
        tylist=[]
        tzlist=[]
        for c in range(len(shape[face])):
            txlist.append(shape[face][c][0])
            tylist.append(shape[face][c][1])
            tzlist.append(shape[face][c][2])
        tx = sum(txlist)/len(txlist)
        ty = sum(tylist)/len(tylist)
        tz = sum(tzlist)/len(tzlist)
        shape[face].append((tx,ty,tz))
        shape[face].append(color)
    return shape

def shapeProcess(shape, color):
    for face in range(len(shape)):
        tx=0
        ty=0
        tz=0
        txlist=[]
        tylist=[]
        tzlist=[]
        for c in range(len(shape[face])):
            txlist.append(shape[face][0])
            tylist.append(shape[face][1])
            tzlist.append(shape[face][c][2])
        tx = sum(txlist)/len(txlist)
        ty = sum(tylist)/len(tylist)
        tz = sum(tzlist)/len(tzlist)
        shape[face].append((tx,ty,tz))
        shape[face].append(color)
    return shape





# will do some processing in the future, ignoring the last 2 items of each of the the faces
def processAgain(shape):
    for face in range(len(shape)):
        tx=0
        ty=0
        tz=0
        txlist=[]
        tylist=[]
        tzlist=[]
        for c in range(len(shape[face])-2):
            txlist.append(shape[face][c][0])
            tylist.append(shape[face][c][1])
            tzlist.append(shape[face][c][2])
        tx = sum(txlist)/len(txlist)
        ty = sum(tylist)/len(tylist)
        tz = sum(tzlist)/len(tzlist)
        shape[face].append((tx,ty,tz))
        #shape[face].append(color)
    return shape


# print(process(cube,(120,150,225)))'''