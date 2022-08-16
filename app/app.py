from flask import Flask, render_template, request




app = Flask(__name__)




@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/apply", methods= ['POST'])
def apply():
    if request.method == "POST":
        name = request.form["fullName"]
    return name

if __name__ == "__main__":
    app.run(debug=True)