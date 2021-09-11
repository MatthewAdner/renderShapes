from shapes import *



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
            tzlist.append(shape[face][2])
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


# print(process(cube,(120,150,225)))