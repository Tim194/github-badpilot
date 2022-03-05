import login
import random

_maxTitleLen = 20 #in char
_lang = [".py", ".txt"]


class Document:
    def __init__(self, title, lang, user):
        self.title = title
        self.lang = lang
        self.author = user.id
        self.allowedUsers = [user.id]
        self.id = random.randint(0,99999999999999)
        self.text = ""
        

def create(title, lang, user):
    if(not safeTitle(title)):
        return login.Error("Title is to long or the title contains characters that are not allowed")

    if(not lang in _lang):
        return login.Error("We do not suport the language you choose. We apoligise for the inconvinience")

    docs = Document(title, lang, user)
    


    


#Returns true if safe and false if not safe
def safeTitle(title):
    if('"' in title):
        return False
    
    if("'" in title):
        return False

    if("<" in title):
        return False

    if(">" in title):
        return False

    if(len(title) > _maxTitleLen):
        return False

    return True

