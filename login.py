import json
import hashlib
import random

MIN_PASSWORD_LEN = 5
SALT = str("4RNZddeqqlzS7h96M7vyevj6d3tLOLSALTPBzX3ZjgsTmROOkeWLFRwdt1QHNA7qKE")

class Error:
    def __init__(self, error):
        self.text = error

    def __bool__(self):
        return False

class User:
    def __init__(self):
        self.email = None
        self.documentIds = None
        self.password = None
        self.id = None

    def toJson(self):
        data = {
            "email": self.email,
            "password": self.password,
            "documents": self.documentIds,
            "id": self.id
        }

        return data

    def loadJson(self, data):
        self.documentIds = data["documents"]
        self.email = data["email"]
        self.password = data["password"]
        self.id = data["id"]

    def save(self):
        with open("users/" + str(self.id) + ".json", 'w') as outfile:
            json.dump(self.toJson(), outfile)

    def load(self, path):

        with open(path) as json_file:
            self.loadJson(json.load(json_file))



def create(email, password):

    if(not passwordCheck(password)):
        return Error("Password dont meet our requerments for a secure password")

    if(not emailCheck(email)):
        return Error("Email dont meet our requerments for a email")

    password = hash512(password)

    user = User()
    user.email = email
    user.password = password
    user.id = random.randint(0,9999999999999)

    user.save()







def hash512(password):
    return hashlib.sha512( SALT ).hexdigest()


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
    