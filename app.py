from flask import Flask
from flask_cors import CORS
from models import db
import routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(routes.bp)

if __name__ == "__main__":
    app.run(debug=True)
