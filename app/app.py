from flask import Flask, jsonify, request


app = Flask(__name__)



@app.route("/", methods=['GET'])
def home():
    return jsonify({"data":"This is my Loan Application Project"})

@app.route("/apply", methods= ['POST'])
def apply():
    if request.method == "POST":
	data = request.get_json()
    	return data
    else:
	return jsonify({"error":"This method is not allowed"}), 400


if __name__ == "__main__":
    app.run(debug=True)