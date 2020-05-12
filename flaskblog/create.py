from flask import Flask
import os
from models import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
    
