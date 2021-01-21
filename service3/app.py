from flask import Flask, request, Response
import random

app = Flask(__name__)

@app.route("/getluck", methods=["GET"])
def getluck():
    #simulate a dice roll
    luck = random.randint(1,6)
    luck2 = random.randint(1,6)
    if luck == luck2:
        lucky = True
    elif luck != luck2:
        lucky = False
    return  Response(str(lucky), mimetype='text/plain')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')