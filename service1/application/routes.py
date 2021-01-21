from application import app, db
from application.models import Fortune
from flask import render_template
import requests
from sqlalchemy import desc

@app.route('/')
@app.route('/index')
def index():
    #target is name of container and port to be published
    day_response = requests.get("http://fortune_app-fortune-service2:5000/getday")
    luck_response = requests.get("http://fortune_app-fortune-service3:5000/getluck")
    fortune_response_post = requests.post("http://fortune_app-fortune-service4:5000/getfortune", json={"day" : day_response.json()["day"] , "luck" : int(luck_response.text)})
    
    fortunemsg = fortune_response_post.text

    day = str(day_response.json()["day"])
    month = str(day_response.json()["month"])
    specdate = str(day + " " + month)
    new_fortune = Fortune(day=specdate, fortune=fortunemsg)
    db.session.add(new_fortune)
    db.session.commit()
    last5 = Fortune.query.order_by(desc("id")).limit(6).all()
    return render_template("index.html", day=specdate, fortune=fortunemsg, last5=last5)