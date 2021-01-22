from application import app, db
from application.models import Fortune2
from flask import render_template
import requests
from sqlalchemy import desc

@app.route('/')
@app.route('/index')
def index():
    #target is name of container and port to be published
    year_response = requests.get("http://fortune-swarm_service2:5000/getyearmon")
    luck_response = requests.get("http://fortune-swarm_service3:5000/getluck")
    fortune_response_post = requests.post("http://fortune-swarm_service4:5000/getfortune", json={"year" : year_response.json()["year"] , "luck" : luck_response.text})
    
    luck = str(luck_response.text)
    fortunemsg = fortune_response_post.text
    month = str(year_response.json()["month"])
    year = str(year_response.json()["year"])
    specdate = str(month + " " + year)
    new_fortune = Fortune2(yearmon=specdate, fortune=fortunemsg, luck=luck)
    db.session.add(new_fortune)
    db.session.commit()
    last5 = Fortune2.query.order_by(desc("id")).limit(6).all()
    return render_template("index.html", yearmon=specdate, luck=luck, fortune=fortunemsg, last5=last5)