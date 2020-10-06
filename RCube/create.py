import hashlib

def _create(parms):
    if(not('faces' in parms) or parms['faces'] == ''):
        faces = 'gybwro'
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
                output = output + (9 * char)
        
        outputBytes = bytes(output, 'utf-8')
        integrity = hashlib.sha256(outputBytes).hexdigest().upper()
        correctReturn = {'cube': output, 'integrity': integrity, 'status': 'ok'}
        return correctReturn