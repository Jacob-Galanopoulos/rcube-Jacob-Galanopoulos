import hashlib
import RCube.check as check
directions = ['f', 'F', 'b', 'B', 'r', 'R', 'l', 'L', 't', 'T', 'u', 'U']

def _rotate(parms):
    if(not('cube' in parms)): return {'status': 'error: missing cube key'}
    if(parms['cube'] == ''): return {'status': 'error: missing cube value'}
    if(not('side' in parms)): return {'status': 'error: missing side key'}
    if(not(parms['side'] in directions)):
        return {'status': 'error: invalid side value'}
    
    validCube = check._check(parms)
    cubeFaces = [parms['cube'][i:i+9] for i in range(0, len(parms['cube']), 9)]
    
    if ('error' in validCube): return validCube
    elif (parms['side'] == 'f' or parms['side'] == 'F'):
        rotatedCube = _rotateFront(cubeFaces, parms['side'])
    elif (parms['side'] == 'b' or parms['side'] == 'B'):
        rotatedCube = _rotateBack(cubeFaces, parms['side'])
    elif (parms['side'] == 'l' or parms['side'] == 'L'):
        rotatedCube = _rotateLeft(cubeFaces, parms['side'])
    elif (parms['side'] == 'r' or parms['side'] == 'R'):
        rotatedCube = _rotateRight(cubeFaces, parms['side'])
    elif (parms['side'] == 't' or parms['side'] == 'T'):
        rotatedCube = _rotateTop(cubeFaces, parms['side'])
    elif (parms['side'] == 'u' or parms['side'] == 'U'):
        rotatedCube = _rotateBottom(cubeFaces, parms['side'])
    
    outputBytes = bytes(rotatedCube, 'utf-8')
    integrity = hashlib.sha256(outputBytes).hexdigest().upper()
    return {'status': 'rotated', 'cube': rotatedCube, 'integrity': integrity}

def _rotateFront(cubeFaces = [], rotateDirection = ''):
    if(len(cubeFaces) == 0): return {'error': 'missing input'}
    if(rotateDirection == ''): return {'error': 'missing input'}
    
    rotatedCube = ''
    #take contents of cubeFaces and make into lists so we can manipulate the characters
    for face in range(0, 6):
        cubeFaces[face] = list(cubeFaces[face])
        
    top = [cubeFaces[4][6], cubeFaces[4][7], cubeFaces[4][8]]
    bottom = [cubeFaces[5][0], cubeFaces[5][1], cubeFaces[5][2]]
    left = [cubeFaces[3][2], cubeFaces[3][5], cubeFaces[3][8]]
    right = [cubeFaces[1][0], cubeFaces[1][3], cubeFaces[1][6]]

    #Should technically work since rotateDirection is only a char
    if rotateDirection.islower():
        #rotate right
        index = 0 
        for face in top:
            cubeFaces[1][index] = face
            if index == 6: break
            index += 3 #to get indices 0,3,6
        for face in left:
            cubeFaces[4][index] = face
            index += 1 #To get the indices 6,7,8
        index = 0 
        for face in right:
            cubeFaces[5][index] = face
            if index == 2: break
            index += 1 #To get indices 0,1,2
        for face in bottom:
            cubeFaces[3][index] = face
            index += 3 #To get the indices 2,5,8
    else:
        #rotate left
        index = 0 
        for face in bottom:
            cubeFaces[1][index] = face
            if index == 6: break
            index += 3 #to get indices 0,3,6
        for face in right:
            cubeFaces[4][index] = face
            index += 1 #To get the indices 6,7,8
        index = 0 
        for face in left:
            cubeFaces[5][index] = face
            if index == 2: break
            index += 1 #To get indices 0,1,2
        for face in top:
            cubeFaces[3][index] = face
            index += 3 #To get the indices 2,5,8
            
    cubeFaces[0] = _rotateCenter(cubeFaces[0], rotateDirection)
    for face in cubeFaces:
        rotatedCube += ''.join(face)    
    return {'rotatedCube': rotatedCube}

def _rotateBack(cubeFaces = [], rotateDirection = ''):
    if(len(cubeFaces) == 0): return {'error': 'missing input'}
    if(rotateDirection == ''): return {'error': 'missing input'}
    
    rotatedCube = ''
    for face in range(0, 6):
        cubeFaces[face] = list(cubeFaces[face])
    
    center = 2
    top = [cubeFaces[4][0], cubeFaces[4][1], cubeFaces[4][2]]
    bottom = [cubeFaces[5][6], cubeFaces[5][7], cubeFaces[5][8]]
    left = [cubeFaces[1][2], cubeFaces[1][5], cubeFaces[1][8]]
    right = [cubeFaces[3][0], cubeFaces[3][3], cubeFaces[3][6]]
    
    if rotateDirection.islower():
        #rotate right
        index = 0 
        for face in top:
            cubeFaces[3][index] = face
            if index == 6: break
            index += 3 #to get indices 0,3,6
        index = 6
        for face in right:
            cubeFaces[5][index] = face
            index += 1 #to get indices 6,7,8
        index = 2
        for face in bottom:
            cubeFaces[1][index] = face
            index += 3 #to get indices 2,5,8
        index = 0
        for face in left:
            cubeFaces[4][index] = face
            index += 1 #to get indices 0,1,2
    else:
        #rotate left
        index = 0 
        for face in bottom:
            cubeFaces[3][index] = face
            if index == 6: break
            index += 3 #to get indices 0,3,6
        index = 6
        for face in left:
            cubeFaces[5][index] = face
            index += 1 #to get indices 6,7,8
        index = 2
        for face in top:
            cubeFaces[1][index] = face
            index += 3 #to get indices 2,5,8
        index = 0
        for face in right:
            cubeFaces[4][index] = face
            index += 1 #to get indices 0,1,2
            
    cubeFaces[center] = _rotateCenter(cubeFaces[center], rotateDirection)
    for face in cubeFaces:
        rotatedCube += ''.join(face)    
    return {'rotatedCube': rotatedCube}

def _rotateLeft(cubeFaces = [], rotateDirection = ''):
    if(len(cubeFaces) == 0): return {'error': 'missing input'}
    if(rotateDirection == ''): return {'error': 'missing input'}
    
    rotatedCube = ''
    #take contents of cubeFaces and make into lists so we can manipulate the characters
    for face in range(0, 6):
        cubeFaces[face] = list(cubeFaces[face])
        
    top = [cubeFaces[4][0], cubeFaces[4][3], cubeFaces[4][6]]
    bottom = [cubeFaces[5][0], cubeFaces[5][3], cubeFaces[5][6]]
    left = [cubeFaces[2][2], cubeFaces[2][5], cubeFaces[2][8]]
    right = [cubeFaces[0][0], cubeFaces[0][3], cubeFaces[0][6]]

    #Should technically work since rotateDirection is only a char
    if rotateDirection.islower():
        #rotate right
        index = 0 
        for face in top:
            cubeFaces[0][index] = face
            index += 3 #to get indices 0,3,6
        index = 0 
        for face in right:
            cubeFaces[5][index] = face
            index += 3 #To get the indices 0,3,6
        index = 2
        for face in bottom:
            cubeFaces[2][index] = face
            index += 3 #To get the indices 2,5,8
        index = 0 
        for face in left:
            cubeFaces[4][index] = face
            index += 3 #To get the indices 0,3,6
    else:
        #rotate left
        index = 0 
        for face in bottom:
            cubeFaces[0][index] = face
            index += 3 #to get indices 0,3,6
        index = 0 
        for face in left:
            cubeFaces[5][index] = face
            index += 3 #To get the indices 0,3,6
        index = 2
        for face in top:
            cubeFaces[2][index] = face
            index += 3 #To get the indices 2,5,8
        index = 0 
        for face in right:
            cubeFaces[4][index] = face
            index += 3 #To get the indices 0,3,6
            
    cubeFaces[3] = _rotateCenter(cubeFaces[3], rotateDirection)
    for face in cubeFaces:
        rotatedCube += ''.join(face)    
    return {'rotatedCube': rotatedCube}

def _rotateRight(cubeFaces = [], rotateDirection = ''):
    if(len(cubeFaces) == 0): return {'error': 'missing input'}
    if(rotateDirection == ''): return {'error': 'missing input'}
    
    rotatedCube = ''
    #take contents of cubeFaces and make into lists so we can manipulate the characters
    for face in range(0, 6):
        cubeFaces[face] = list(cubeFaces[face])
        
    top = [cubeFaces[4][2], cubeFaces[4][5], cubeFaces[4][8]]
    bottom = [cubeFaces[5][2], cubeFaces[5][5], cubeFaces[5][8]]
    left = [cubeFaces[0][2], cubeFaces[0][5], cubeFaces[0][8]]
    right = [cubeFaces[2][0], cubeFaces[2][3], cubeFaces[2][6]]

    #Should technically work since rotateDirection is only a char
    if rotateDirection.islower():
        #rotate right
        index = 0 
        for face in top:
            cubeFaces[2][index] = face
            index += 3 #to get indices 0,3,6
        index = 2
        for face in right:
            cubeFaces[5][index] = face
            index += 3 #To get the indices 2,5,8
        index = 2
        for face in bottom:
            cubeFaces[0][index] = face
            index += 3 #To get the indices 2,5,8
        index = 2
        for face in left:
            cubeFaces[4][index] = face
            index += 3 #To get the indices 2,5,8
    else:
        #rotate left
        index = 0 
        for face in bottom:
            cubeFaces[2][index] = face
            index += 3 #to get indices 0,3,6
        index = 2
        for face in left:
            cubeFaces[5][index] = face
            index += 3 #To get the indices 2,5,8
        index = 2
        for face in top:
            cubeFaces[0][index] = face
            index += 3 #To get the indices 2,5,8
        index = 2
        for face in right:
            cubeFaces[4][index] = face
            index += 3 #To get the indices 2,5,8
            
    cubeFaces[1] = _rotateCenter(cubeFaces[1], rotateDirection)
    for face in cubeFaces:
        rotatedCube += ''.join(face)    
    return {'rotatedCube': rotatedCube}

def _rotateTop(cubeFaces = [], rotateDirection = ''):
    if(len(cubeFaces) == 0): return {'error': 'missing input'}
    if(rotateDirection == ''): return {'error': 'missing input'}
    
    rotatedCube = ''
    #take contents of cubeFaces and make into lists so we can manipulate the characters
    for face in range(0, 6):
        cubeFaces[face] = list(cubeFaces[face])
        
    top = [cubeFaces[2][0], cubeFaces[2][1], cubeFaces[2][2]]
    bottom = [cubeFaces[0][0], cubeFaces[0][1], cubeFaces[0][2]]
    left = [cubeFaces[3][0], cubeFaces[3][1], cubeFaces[3][2]]
    right = [cubeFaces[1][0], cubeFaces[1][1], cubeFaces[1][2]]

    #Should technically work since rotateDirection is only a char
    if rotateDirection.islower():
        #rotate right
        index = 0 
        for face in top:
            cubeFaces[1][index] = face
            index += 1 #to get indices 0,1,2
        index = 0 
        for face in right:
            cubeFaces[0][index] = face
            index += 1 #to get indices 0,1,2
        index = 0 
        for face in bottom:
            cubeFaces[3][index] = face
            index += 1 #to get indices 0,1,2
        index = 0 
        for face in left:
            cubeFaces[2][index] = face
            index += 1 #to get indices 0,1,2
    else:
        #rotate left
        index = 0 
        for face in bottom:
            cubeFaces[1][index] = face
            index += 1 #to get indices 0,1,2
        index = 0 
        for face in left:
            cubeFaces[0][index] = face
            index += 1 #to get indices 0,1,2
        index = 0 
        for face in top:
            cubeFaces[3][index] = face
            index += 1 #to get indices 0,1,2
        index = 0 
        for face in right:
            cubeFaces[2][index] = face
            index += 1 #to get indices 0,1,2
            
    cubeFaces[4] = _rotateCenter(cubeFaces[4], rotateDirection)
    for face in cubeFaces:
        rotatedCube += ''.join(face)    
    return {'rotatedCube': rotatedCube}

def _rotateBottom(cubeFaces = [], rotateDirection = ''):
    if(len(cubeFaces) == 0): return {'error': 'missing input'}
    if(rotateDirection == ''): return {'error': 'missing input'}
    
    rotatedCube = ''
    #take contents of cubeFaces and make into lists so we can manipulate the characters
    for face in range(0, 6):
        cubeFaces[face] = list(cubeFaces[face])
        
    top = [cubeFaces[0][6], cubeFaces[0][7], cubeFaces[0][8]]
    bottom = [cubeFaces[2][6], cubeFaces[2][7], cubeFaces[2][8]]
    left = [cubeFaces[3][6], cubeFaces[3][7], cubeFaces[3][8]]
    right = [cubeFaces[1][6], cubeFaces[1][7], cubeFaces[1][8]]

    #Should technically work since rotateDirection is only a char
    if rotateDirection.islower():
        #rotate right
        index = 6 
        for face in top:
            cubeFaces[1][index] = face
            index += 1 #to get indices 6,7,8
        index = 6  
        for face in right:
            cubeFaces[2][index] = face
            index += 1 #to get indices 6,7,8
        index = 6  
        for face in bottom:
            cubeFaces[3][index] = face
            index += 1 #to get indices 6,7,8
        index = 6  
        for face in left:
            cubeFaces[0][index] = face
            index += 1 #to get indices 6,7,8
    else:
        #rotate left
        index = 6 
        for face in bottom:
            cubeFaces[1][index] = face
            index += 1 #to get indices 6,7,8
        index = 6 
        for face in left:
            cubeFaces[2][index] = face
            index += 1 #to get indices 6,7,8
        index = 6 
        for face in top:
            cubeFaces[3][index] = face
            index += 1 #to get indices 6,7,8
        index = 6 
        for face in right:
            cubeFaces[0][index] = face
            index += 1 #to get indices 6,7,8
            
    cubeFaces[5] = _rotateCenter(cubeFaces[5], rotateDirection)
    for face in cubeFaces:
        rotatedCube += ''.join(face)    
    return {'rotatedCube': rotatedCube}

#Ever come to the realization that everything does the same thing?
#Why not make a function to do all that in one place
def _rotateCenter(wholeFace = [], direction = ''):
    if(len(wholeFace) == 0): return {'error': 'missing input'}
    if(direction == ''): return {'error': 'missing input'}
    
    segmentedCenter = list()
    holder = list()
    for face in wholeFace:
        holder.append(face)
        if (len(holder) == 3):
            segmentedCenter.append(holder)
            holder = list()
            
    if direction.islower():
        rotatedCenter = list(zip(*segmentedCenter[::-1]))
    else:
        rotatedCenter = list(zip(*segmentedCenter))[::-1]
        
    condensedCenter = []    
    for side in rotatedCenter:
            for face in side:
                condensedCenter.append(face)
    return condensedCenter