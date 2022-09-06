<<<<<<< HEAD
from flask import Flask, jsonify, request
=======
from flask import Flask, render_template, request


>>>>>>> c28aa6b9062d88b416d69d9d433d0cf35e65d22f


app = Flask(__name__)




<<<<<<< HEAD
@app.route("/", methods=['GET'])
def home():
    return jsonify({"data":"This is my Loan Application Project"})
=======
@app.route("/")
def hello():
    return render_template("index.html")
>>>>>>> c28aa6b9062d88b416d69d9d433d0cf35e65d22f

@app.route("/apply", methods= ['POST'])
def apply():
    if request.method == "POST":
<<<<<<< HEAD
	data = request.get_json()
    	return data
    else:
	return jsonify({"error":"This method is not allowed"}), 400
=======
        name = request.form["fullName"]
    return name
>>>>>>> c28aa6b9062d88b416d69d9d433d0cf35e65d22f

if __name__ == "__main__":
    app.run(debug=True)