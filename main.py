import errno
from flask import Flask, render_template, request,redirect
import login
app = Flask(__name__)

#Website index
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup", methods=["POST", "GET"])
def signup():
    if(request.method == "POST"):
        email = request.form['email']
        password = request.form["password"]

        data = login.create(email,password)

        if(data):

            return redirect("/")
        return render_template("signup.html", error=data.text)
    else:
        return render_template("signup.html")

if(__name__ == "__main__"):
    app.run(debug=True)
