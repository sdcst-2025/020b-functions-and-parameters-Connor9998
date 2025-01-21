



def validateUser( username , password):
    if username == "correct" and password == "correct":
        return True
    else:
        return False

if validateUser('bob','12345') == True:
    print('you are valid, log in ')
else:
    print('invalid user')