from flask import Flask, request, Response
import requests

app = Flask(__name__)

lucky=[1,3,7,9,10,15,21,25,31]
unlucky=[2,6,8,11,13,17,23,30]

@app.route('/getfortune', methods=["POST"])
def getfortune():

    output = request.json
    day = output["day"]
    luck = output["luck"]

    if int(day) in unlucky:
        luck -= 20
    elif int(day) in lucky:
        luck += 10
    if luck < 55:
        fortunemsg="You are truly unlucky, the system predicts a bad event shall besiege your life soon, be careful!"
    elif luck > 55 and luck < 70:
        fortunemsg="You are lucky nor unlucky, perhaps a dark future awaits, perhaps not"
    elif luck > 80 and luck < 105:
        fortunemsg="You are a lucky individual, the gods have favoured your path and await good results"
    else:
        fortunemsg="You are the luckiest individual on earth, Your past, present and future has been blessed by higher powers the system predicts a lottery win in the near future"

    return Response(str(fortunemsg), mimetype='text/plain')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')