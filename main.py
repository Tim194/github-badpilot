from flask import Flask, render_template, request
app = Flask(__name__)

#Website index
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup", methods=["POST", "GET"])
def signup():
    if(request.method == "POST"):
        return render_template("signup.html")
    else:
        return render_template("signup.html")

if(__name__ == "__main__"):
    app.run(debug=True)
