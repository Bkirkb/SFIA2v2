from flask import Flask, request, Response
import requests

app = Flask(__name__)

luckyyear=["2022", "2023","2026","2030"]
unluckyyear=["2021","2024","2027"]

@app.route('/getfortune', methods=["POST"])
def getfortune():
    output=request.json
    year=output["year"]
    luckybool=output["luck"]
    if luckybool == "True" and year in luckyyear:
        fortunemsg = "You've rolled a double in the game and in life, you are truly lucky."
    elif luckybool == "True" and year not in luckyyear and year not in unluckyyear:
        fortunemsg = "The double dice predicts a neutral fate"
    elif luckybool == "False" and year in luckyyear:
        fortunemsg = "Your luck is not with the dice rolls, but your future is bright"
    elif luckybool == "True" and year in unluckyyear:
        fortunemsg = "Though you may be skilled with the dice, you should avoid danger in your chosen year"
    elif luckybool == "False" and year in unluckyyear:
        fortunemsg = "Bad things may be coming, avoid outside at all costs."
    else:
        fortunemsg = "Your past, present and future are unknown"
    return Response(str(fortunemsg), mimetype='text/plain')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')