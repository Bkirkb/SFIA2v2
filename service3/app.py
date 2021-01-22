from flask import Flask, Response
import random

app = Flask(__name__)

@app.route("/getluck", methods=["GET"])
def getluck():
    luck = random.randint(1,100)
    return  Response(str(luck), mimetype='text/plain')



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')