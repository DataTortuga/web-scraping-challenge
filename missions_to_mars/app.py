from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)


@app.route("/")
def index():
    mars_nws = mongo.db.mars_nws.find_one()
    return render_template("index.html", mars_nws=mars_nws)


@app.route("/scrape")
def scraper():

    mars_nws = mongo.db.mars_nws
    mars_f_img = mongo.db.mars_f_img
    mars_tb = mongo.db.mars_tb
    mars_hem = mongo.db.mars_hem

    mars_data = scrape_mars.scrape()
    mars_nws.update({}, mars_data[0], upsert=True)
    mars_f_img.update({}, mars_data[1], upsert=True)
    mars_tb.update({}, mars_data[2], upsert=True)
    mars_hem.update({}, mars_data[3], upsert=True)
    
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
