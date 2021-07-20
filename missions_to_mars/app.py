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

@app.route("/hemi")
def hemi():
    mars_nws = mongo.db.mars_nws.find_one()
    return render_template("hemi.html", mars_nws=mars_nws)


@app.route("/scrape")
def scraper():


    mongo.db.mars_nws.drop()
    mars_nws = mongo.db.mars_nws


    mars_data = scrape_mars.scrape()
    mars_nws.insert_many(mars_data)
    
    
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)


