from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():

    mars_data = mongo.db.collection.find_one()

    return render_template("index.html", data=mars_data)


@app.route("/scrape")
def scrape():

    mars_dic = scrape_mars.scrape()
    print(mars_dic)

    mongo.db.collection.update({},mars_dic, upsert=True)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
