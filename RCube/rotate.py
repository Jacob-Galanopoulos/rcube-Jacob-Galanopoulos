import hashlib
import RCube.check as check
from test.test_set import cube
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
    elif (parms['side'] == 'f' or parms['side'] == 'F' or parms['side'] == 'b' or 
          parms['side'] == 'B'):
        rotatedCube = _execFrontAndBack(cubeFaces, parms['side'])
    elif (parms['side'] == 'r' or parms['side'] == 'R' or parms['side'] == 'l' or 
          parms['side'] == 'L'):
        rotatedCube = _execLeftAndRight(cubeFaces, parms['side'])
    else:
        rotatedCube = _execTopAndBottom(cubeFaces, parms['side'])
    
    outputBytes = bytes(rotatedCube, 'utf-8')
    integrity = hashlib.sha256(outputBytes).hexdigest().upper()
    return {'status': 'rotated', 'cube': rotatedCube, 'integrity': integrity}

def _execFrontAndBack(cubeFaces = [], rotateDirection = ''):
    rotatedCube = ''
    center = cubeFaces[0]
    top = cubeFaces[4][6:8]
    bottom = cubeFaces[5][0:2]
    if (rotateDirection == 'f' or rotateDirection == 'F'):
        left = cubeFaces[3][2] + cubeFaces[3][5] + cubeFaces[3][8]
        right = cubeFaces[1][0] + cubeFaces[1][3] + cubeFaces[1][6]
        if (rotateDirection == 'f'):
            cubeFaces[4][6:8] = left
            cubeFaces[5][0:2] = right
            cubeFaces[1][0] = top[0]
            cubeFaces[1][3] = top[1]
            cubeFaces[1][6] = top[2]
            cubeFaces[3][8] = bottom[2]
            cubeFaces[3][5] = bottom[1]
            cubeFaces[3][2] = bottom[0]
            #center
            cubeFaces[0][0] = center[6]
            cubeFaces[0][1] = center[3]
            cubeFaces[0][2] = center[0]
            cubeFaces[0][3] = center[7]
            cubeFaces[0][4] = center[4]
            cubeFaces[0][5] = center[1]
            cubeFaces[0][6] = center[8]
            cubeFaces[0][7] = center[5]
            cubeFaces[0][8] = center[2]
        else:
            cubeFaces[4][6:8] = right
            cubeFaces[5][0:2] = left
            cubeFaces[1][0] = bottom[2]
            cubeFaces[1][3] = bottom[1]
            cubeFaces[1][6] = bottom[0]
            cubeFaces[3][2] = top[2]
            cubeFaces[3][5] = top[1]
            cubeFaces[3][8] = top[0]
            #center
            cubeFaces[0][0] = center[2]
            cubeFaces[0][1] = center[5]
            cubeFaces[0][2] = center[8]
            cubeFaces[0][3] = center[1]
            cubeFaces[0][4] = center[4]
            cubeFaces[0][5] = center[7]
            cubeFaces[0][6] = center[0]
            cubeFaces[0][7] = center[3]
            cubeFaces[0][8] = center[6]
    else:
        center = cubeFaces[2]
        left = cubeFaces[1][2] + cubeFaces[1][5] + cubeFaces[1][8]
        right = cubeFaces[3][0] + cubeFaces[3][3] + cubeFaces[3][6]
        #if (rotateDirection == 'B'):
            #Do the rotation here
        #else:
            #Do the rotation here
    for c in cubeFaces:
        rotatedCube += c        
    return rotatedCube

def _execLeftAndRight(cubeFaces = [], rotateDirection = ''):
    result = {'rotate': 'rotate stub'}
    return result

def _execTopAndBottom(cubeFaces = [], rotateDirection = ''):
    result = {'rotate': 'rotate stub'}
    return result