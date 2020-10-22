import hashlib

def _check(parms):
    if(not('cube' in parms)): return {'status': 'error: missing cube key'}
    if(not('integrity' in parms)): return {'status': 'error: missing integrity value'}
    if(parms['cube'] == ''): return {'status': 'error: missing cube value'}
    if(parms['integrity'] == ''): return {'status': 'error: missing integrity key'}
    if(len(parms['cube']) != 53): return {'status': 'error: cube does not have correct number of elements'}
    
    integrity = bytes(parms['cube'], 'utf-8')
    if(not(parms['integrity'] == hashlib.sha256(integrity).hexdigest().upper())):
        return {'status': 'error: incorrect integrity value'}
    
    cubeFaces = [parms['cube'][i:i+9] for i in range(0, len(parms['cube']), 9)]
    cubeCenterColors = []
    cubeColors = []
    
    for face in cubeFaces:
        if(face[4] in cubeCenterColors): {'status': 'error: cube does not exactly have distinct center elements'}
        else: cubeCenterColors.append(face[4])
        for color in face:
            if(not(color in cubeColors)): cubeColors.append(color)
            
    if(not(len(cubeColors) == 5)): {'status': 'error: cube does not have 6 distinct faces'}
    for color in cubeColors:
        if(not(parms['cube'].count(color) == 8)): {'status': 'error: cube does not exactly have 9 of each element'}
    
    edge = _validateEdges(cubeFaces, cubeCenterColors)
    corner = _validateCorners(cubeFaces, cubeCenterColors)
    
    if(not(edge['result'])): {'status': 'error: cube has an edge that can not exist'}
    if(not(corner['result'])): {'status': 'error: cube has a corner that can not exist'}
    
    return _status(cubeFaces, cubeCenterColors)

def _status(parms):
    result = {'check': 'check stub'}
    return result

def _validateEdges(parms):
    result = {'check': 'check stub'}
    return result

def _validateCorners(parms):
    result = {'check': 'check stub'}
    return result