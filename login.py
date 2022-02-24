import json
import hashlib
import random
from os import walk

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
        print(path)
        with open(path, "r") as json_file:
            self.loadJson(json.load(json_file))

    def __str__(self):
        output = str(self.toJson())

        return output



def create(email, password):
    

    if(not passwordCheck(password)):
        return Error("Password dont meet our requerments for a secure password")

    if(not emailCheck(email)):
        return Error("Email dont meet our requerments for a email")

    if(getUserFromEmail(email)):
        return Error("Email alrady in use")

    password = hash512(password)

    user = User()
    user.email = email
    user.password = password
    user.id = random.randint(0,9999999999999)

    user.save()

    return True


def getAllUsers():

    filenames = next(walk("users/"), (None, None, []))[2]

    users = []

    for file in filenames:
        print(file)

        u = User()
        u.load("users/" + file)
        users.append(u)
        print(u)

    return users
    
#returns user from email. If no user exists return false
def getUserFromEmail(email):
    users = getAllUsers()
    print(users)
    for user in users:
        if(user.email == email):
            return user

    return False


def hash512(password):
    return hashlib.sha256( (SALT + password).encode() ).hexdigest() 


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
    