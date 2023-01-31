import os
from sqlalchemy import Column, String, Integer, create_engine, Date, Float
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import date
#from config import database_setup

#----------------------------------------------------------------------------#
# Database Setup 
#----------------------------------------------------------------------------#

# Use Production Database.
# If run locally, key does not exist, so use locally set database instead.
#database_path = os.environ.get('DATABASE_URL', "postgres://{}:{}@{}/{}".format(database_setup["user_name"], database_setup["password"], database_setup["port"], database_setup["database_name_test"]))
database_path = os.environ['DATABASE_URL']
if database_path.startswith("postgres://"):
  database_path = database_path.replace("postgres://", "postgresql://", 1)
db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    '''binds a flask application and a SQLAlchemy service'''
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

def db_fresh_db():
    '''creates the fresh db and deletes existing if any
    preparing a clean database
    '''
    db.drop_all()
    db.create_all()
    db_init_records()

def db_init_records():
    '''Intializing the database with the records.'''

    actor = (Actors(
        name = 'Shahrukh Khan',
        gender = 'Male',
        age = 56
        ))

    movie = (Movies(
        title = 'Pathaan',
        release_date = date.today()
        ))

    performance = Performance.insert().values(
        MovieId = movie.id,
        ActorId = actor.id,
        actorFees = 50000.00
    )

    actor.insert()
    movie.insert()
    db.session.execute(performance) 
    db.session.commit()

#----------------------------------------------------------------------------#
# Performance Junction Object N:N 
#----------------------------------------------------------------------------#

# Without creating a new Table, we create a association table
Performance = db.Table('Performance', db.Model.metadata,
    db.Column('MovieId', db.Integer, db.ForeignKey('movies.id')),
    db.Column('ActorId', db.Integer, db.ForeignKey('actors.id')),
    db.Column('actorFees', db.Float)
)

#----------------------------------------------------------------------------#
# Actors Model 
#----------------------------------------------------------------------------#

class Actors(db.Model):  
  __tablename__ = 'actors'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  gender = Column(String)
  age = Column(Integer)

  def __init__(self, name, gender, age):
    self.name = name
    self.gender = gender
    self.age = age

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'name' : self.name,
      'gender': self.gender,
      'age': self.age
    }

#----------------------------------------------------------------------------#
# Movies Model 
#----------------------------------------------------------------------------#

class Movies(db.Model):  
  __tablename__ = 'movies'

  id = Column(Integer, primary_key=True)
  title = Column(String)
  release_date = Column(Date)
  actors = db.relationship('Actors', secondary=Performance, backref=db.backref('performances', lazy='joined'))

  def __init__(self, title, release_date) :
    self.title = title
    self.release_date = release_date

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'title' : self.title,
      'release_date': self.release_date
    }
