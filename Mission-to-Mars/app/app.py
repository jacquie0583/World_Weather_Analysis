# use Flask to render a template, redirecting to another url, and creating a URL
# use PyMongo to interact with our Mongo database
# use the scraping code, we will convert from Jupyter notebook to Python
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
# Python that our app will connect to Mongo using a URI
# URI is saying that the app can reach Mongo through our localhost server, using port 27017
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# define the route for the HTML page,function is what links our visual representation of our work, our web app, to the code that powers it.
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

# function sets up our scraping route,which will be the "button" of the web app, the one that will scrape updated data,tied to a button that runs the code when clicked.
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)

if __name__ == "__main__":
   app.run(debug=True)  