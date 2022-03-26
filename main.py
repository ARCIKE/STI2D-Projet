from flask import Flask, render_template, request
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


@app.route('/')
def home_page():
    return render_template("index.html")
  
@app.route('/path/<longa>/<lata>/<longb>/<latb>')
def coord(longa,lata,longb,latb):
    return render_template("path.html", longa=longa, lata=lata, longb=longb, latb=latb)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
	)

