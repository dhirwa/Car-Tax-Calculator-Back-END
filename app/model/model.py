from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/cars'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db=SQLAlchemy(app)
migrate= Migrate(app, db)


manager=Manager(app)
manager.add_command('db', MigrateCommand)

class Cars(db.Model):
    cr_id=db.Column(db.Integer,primary_key= True)
    cr_brand=db.Column(db.String(50))
    cr_mark=db.Column(db.String(50))
    cr_engine=db.Column(db.String(50))
    cr_drive=db.Column(db.String(50))
    cr_year=db.Column(db.Integer)
    cr_newprice=db.Column(db.Integer)
    cr_body=db.Column(db.String(50))
    cr_category=db.Column(db.String(10))




if __name__ == '__main__':
    manager.run()
