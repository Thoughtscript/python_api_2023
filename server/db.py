from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db_name = 'sockmarket.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)