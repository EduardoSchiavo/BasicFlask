from  flask import Flask, redirect, url_for

from flask import render_template, request

app =Flask('__main__')

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form['nm']
        return redirect(url_for("user", username=username))
    else:
        return render_template("login.html")
    
@app.route("/<username>")
def user(username):
    # return "<h1>{0}</h1>".format(username)
    return render_template("username.html", name=username)


if __name__=='__main__':
    app.run(debug=True)
