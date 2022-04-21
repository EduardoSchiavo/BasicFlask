from  flask import Flask, redirect, url_for
from flask import render_template, request

#instantiate flask app
app =Flask('__main__')

#route to the homepage, using the index.html template
@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

#route to the form that lets you enter your name. 
#not a real login by any means!!
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form['nm']
        return redirect(url_for("user", username=username))
    else:
        return render_template("login.html")

#route displaying welcome message
@app.route("/<username>")
def user(username):
    return render_template("username.html", name=username)


#run the app
if __name__=='__main__':
    app.run(debug=True) #debug True let's the app automatically updated if changes are saved while it's running
