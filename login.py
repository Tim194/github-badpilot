import hashlib

MIN_PASSWORD_LEN = 5
SALT = "4RNZddeq!qlzS7h96M7vyevj6d3tPBzX3ZjgsTmROOkeWLFRwdt1QHNA7qKE"

class Error:
    def __init__(self, error):
        self.text = error

    def __bool__(self):
        return False


def create(email, password):

    if(not passwordCheck(password)):
        return Error("Password dont meet our requerments for a secure password")

    if(not emailCheck(email)):
        return Error("Email dont meet our requerments for a email")

    password = hash512(password)




def hash512(password):
    return hashlib.sha512( SALT + password ).hexdigest()


def passwordCheck(password):
    if(len(password) < MIN_PASSWORD_LEN and type(password) == type("")): #If password is to chort
        return False
    
    else:
        return True

def emailCheck(email):
    if("@" in email and type(email) == type("") and not "'" in email and not '"' in email):
        email = email.split("@")
        domain = email[1]
        name = email[0]

        if(len(name) > 0 and "." in domain):
            return True
    
    return False
    