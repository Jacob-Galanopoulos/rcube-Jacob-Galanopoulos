import hashlib

def _check(parms):
    if(not('cube' in parms)): return {'status': 'error: missing cube key'}
    if(parms['cube'] == ''): return {'status': 'error: missing cube value'}
    if(len(parms['cube']) != 54): return {'status': 'error: cube does not have correct number of elements'}
    
    cubeFaces = [parms['cube'][i:i+9] for i in range(0, len(parms['cube']), 9)]
    cubeCenterColors = []
    cubeColors = []
    
    for face in cubeFaces:
        if(face[4] in cubeCenterColors): return {'status': 'error: cube does not exactly have distinct center elements'}
        else: cubeCenterColors.append(face[4])
        for color in face:
            if(not(color in cubeColors)): cubeColors.append(color)
            
    if(not(len(cubeColors) == 6)): return {'status': 'error: cube does not have 6 distinct faces'}
    for color in cubeColors:
        if(not(parms['cube'].count(color) == 9)): return {'status': 'error: cube does not exactly have 9 of each element'}
    
    #edge = _validateEdges(cubeFaces, cubeCenterColors)
    #corner = _validateCorners(cubeFaces, cubeCenterColors)
    
    #if(not(edge['result'])): {'status': 'error: cube has an edge that can not exist'}
    #if(not(corner['result'])): {'status': 'error: cube has a corner that can not exist'}
    
    if(not('integrity' in parms)): return {'status': 'error: missing integrity value'}
    if(parms['integrity'] == ''): return {'status': 'error: missing integrity key'}
    integrity = bytes(parms['cube'], 'utf-8')
    if(not(parms['integrity'] == hashlib.sha256(integrity).hexdigest().upper())): return {'status': 'error: incorrect integrity value'}
    
    return _status(cubeFaces, cubeCenterColors)

def _status(cubeFaces = [], cubeCenterColors = []):
    if(len(cubeFaces) == 0): return {'error': 'missing cube faces'}
    if(len(cubeCenterColors) == 0): return {'error': 'missing cube center colors'}
    
    isFull = True
    isCross = True
    isSpot = True
    currentFace = 0
    for face in cubeFaces:
        spot = face[:4] + face[4+1:]
        if(not(face[0]*9 == face)): isFull = False
        if(not(cubeCenterColors[currentFace] == face[1]) or 
            not(cubeCenterColors[currentFace] == face[3]) or 
            not(cubeCenterColors[currentFace] == face[5]) or 
            not(cubeCenterColors[currentFace] == face[7])):
            isCross = False
        if(not(spot == face[0]*8)):
            spot = False
        currentFace += 1
            
    if isFull:
        return {'status': 'full'}
    elif isCross:
        return {'status': 'crosses'}
    elif isSpot:
        return {'status': 'spots'}
    else:
        return {'status': 'unknown'}
            

def _validateEdges(cubeFaces = [], cubeCenterColors = []):
    result = {'check': 'check stub'}
    return result

def _validateCorners(cubeFaces = [], cubeCenterColors = []):
    result = {'check': 'check stub'}
    return result