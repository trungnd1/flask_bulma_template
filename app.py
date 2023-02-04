from flask import Flask, render_template
import os

# Initialize the Flask application=======================================================================
app = Flask(__name__)
app.config.from_object('config.DevConfig')
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = app.config['INSECURE_TRANSPORT']
app.secret_key = app.config['SECRET_KEY']      # os.urandom(24) #os.environ.get("SECRET_KEY") or os.urandom(24)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()