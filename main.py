from flask import Flask, render_template, request, jsonify
from replit import db
import random

app = Flask(
	__name__,
	template_folder='templates',
	static_folder='static'
)

@app.route('/')
def home_page():
    return render_template("index.html")
 
@app.route('/path/<longa>/<lata>/<longb>/<latb>')
def coord(longa,lata,longb,latb):
    return render_template("path.html", longa=longa, lata=lata, longb=longb, latb=latb)

if __name__ == "__main__":
	app.run(
		host='0.0.0.0',
		port=random.randint(2000, 9000)
	)