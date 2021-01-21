from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/getyearmon", methods=["GET"])
def getyearmon():
        years = ["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030", "2031", "2032", "2033"]
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        year = random.choice(years)
        month = random.choice(months)
        date={"year" : year, "month" : month}
        return jsonify(date)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')