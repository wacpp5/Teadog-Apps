from flask import Flask
from dog_dollars.routes import dog_dollars_bp
from upsell.routes import upsell_bp
from boxrate.routes import boxrate_bp

app = Flask(__name__)

app.register_blueprint(dog_dollars_bp, url_prefix="/dog-dollars")
app.register_blueprint(upsell_bp, url_prefix="/upsell")
app.register_blueprint(boxrate_bp, url_prefix="/boxrate")

@app.route("/")
def index():
    return {"status": "Teadog Unified App is running"}

if __name__ == "__main__":
    app.run(debug=True)
