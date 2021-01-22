<<<<<<< HEAD
from flask import Flask,request, Response, jsonify
=======
from flask import Flask, jsonify
>>>>>>> development
import random

app = Flask(__name__)

@app.route("/getday", methods=["GET"])
def getday():
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        month = random.choice(months)
        if month == "February":
            day = random.randint(1,28)
        elif month == "April" or month == "June" or month == "September" or month == "November":
            day = random.randint(1,30)
        else:
            day = random.randint(1,31)
        date={"day" : day, "month" : month}
        return jsonify(date)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')