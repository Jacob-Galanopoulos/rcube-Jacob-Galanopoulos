import hashlib

def _create(parms):
    defaultReturn = {'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 
                          'integrity': '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289', 
                          'status':'ok'}
    if(not("faces" in parms)):
        return defaultReturn
    else:
        faces = parms["faces"]
    
    if(not(len(faces) == 6)):
        error = {'status': 'error: Incorrect length of faces - must be exactly 6 faces'}
        return error
    else:
        output = ''
        for char in faces:
            if (faces.count(char) > 1):
                error = {'status': 'error: No duplicate faces are allowed'}
                return error
            else:
                i = 0
                while i < 9:
                    output = output.join(char)
                    i += 1
        
        integrity = hashlib.sha256(faces).hexdigest().upper()
        correctReturn = {'cube': output, 'integrity': integrity, 'status': 'ok'}
        return correctReturn