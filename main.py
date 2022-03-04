from flask import Flask, render_template, request,redirect, session
import login
import random
app = Flask(__name__)
app.secret_key = "EGTRQwerqwg56hrt6u5w45qa34t8i56e4fLOLOLedfw"

#Website index
@app.route("/")
def index():
    u = getUser()
    if(u):
        return render_template("index.html", u=u)
    return render_template("index.html")

@app.route("/login", methods=["GET","POST"])
def loginPage():
    u = getUser()
    if(u):
        return redirect("/")


    if(request.method == "POST"):
        email = request.form['email']
        password = request.form["password"]

        data = login.login(email,password)

        if(data):
            u = data
            loginUser(u)
            return redirect("/docs")
        return render_template("login.html", error=data.text)
    return render_template("login.html")

@app.route("/signup", methods=["POST", "GET"])
def signup():
    u = getUser()
    if(u):
        return redirect("/")

    if(request.method == "POST"):
        email = request.form['email']
        password = request.form["password"]

        data = login.create(email,password)

        if(data):
            u = data
            loginUser(u)
            return redirect("/docs")
        return render_template("signup.html", error=data.text)
    else:
        return render_template("signup.html")

@app.route("/logout")
def logout():
    session["pId"] = None
    return redirect("/")

@app.route("/docs")
def documentList():
    u = getUser()
    if(not u):
        return redirect("/login")

    return render_template("docs.html")

@app.route("/docs/create", methods=("POST", "GET"))
def createDocs():
    u = getUser()
    if(not u):
        return redirect("/login")
    
    if(request.method == "POST"):
        pass

    return render_template("createDocs.html")

    

publicIds = []
activeUsers = []

# takes user class as input
def loginUser(u):
    publicId = random.randint(0,999999999999999)

    publicIds.append([publicId, u.id])


    switch = True
    for activeUser in activeUsers:
        if(activeUser.id == u.id):
            switch = False
    
    if(switch):
        activeUsers.append(u)

    session["pId"] = publicId

#if the user is loged in it returns the user class while if the user is not loged in the func returns false
def getUser():
    if("pId" in session):
        for pId in publicIds:

            if(pId[0] == session["pId"]):
                for u in activeUsers:
                    if(u.id == pId[1]):
                        return u
        return False                
    else:
        return False
    



if(__name__ == "__main__"):
    app.run(debug=True)
