import os
import sys
from flask import Flask, request, Response, abort, jsonify

try:
     from flask_cors import CORS, cross_origin
except ImportError:
     import os
     parentdir= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
     os.sys.path.insert(0,parentdir)
     from flask_cors import CORS, cross_origin

from flask_sqlalchemy import SQLAlchemy
from auth import AuthError, requires_auth
from models import db_drop_and_create_all, setup_db, Actors, Movies, Performance
from config import pagination_service

ROWS  = pagination_service['example']

app = Flask(__name__)
cors=CORS(app, resources={r"/*": {"origins": "*"}})
#CORS(app, support_credentials=True)

@app.route("/login")
@cross_origin(supports_credentials=True)
def login():
  return jsonify({'success': 'ok'})

def create_app(test_config=None):
  '''create and configure the app'''
  
  app = Flask(__name__)
  setup_db(app)
  # db_drop_and_create_all() # uncomment this if you want to start a new database

  CORS(app)
  # CORS Headers 
  @app.after_request
  def after_request(response):
      #response.headers.add('Access-Control-Allow-Origin', '*')
      response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
      response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
      #response.headers.add('Access-Control-Expose-Headers', 'Content-Type,Content-Length,Authorization,X-Pagination')
      
      if request.method.lower()=='options':
        return Response()
      return response

  #----------------------------------------------------------------------------#
  # User Functions start here
  #----------------------------------------------------------------------------#

  def get_error_message(error, message):
      '''This function returns the error message in case anything goes wrong

      '''
      try:
          # Return error message 
          return error.description['message']
      except:
          # else default text
          return message

  def paginate_results(request, results):
    '''Paginates and formats database queries. Parameters are HTTP object requesr and database selection   
    Returns: list of objects
    Returns:
      * <list> list of objects

    '''
    # Get page from request. default is set to 1 
    page = request.args.get('page', 1, type=int)
    start =  (page - 1) * ROWS
    end = start + ROWS
    result_objects  = [object_name.format() for object_name in results]
    return result_objects [start:end]

  #----------------------------------------------------------------------------#
  #  API Code start from here 

  #----------------------------------------------------------------------------#
  # Endpoint /actors GET/POST/DELETE/PATCH
  #----------------------------------------------------------------------------#
  @app.route('/actors', methods=['GET'])
  @requires_auth('read:actors')
  def get_actors(payload):
    result_actors = Actors.query.all()
    allactors = paginate_results(request, result_actors)

    if len(allactors) == 0:
      abort(404, {'message': 'error, no actor found'})

    return jsonify({
      'success': True,
      'actors': allactors
    })

  @app.route('/actors', methods=['POST'])
  @requires_auth('create:actors')
  def insert_actors(payload):
    """Inserts a new Actor
    """
    # Get request json
    response = request.get_json()

    if not response:
          abort(400, {'message': 'Not a valid JSON'})
    name = response.get('name', None)
    age = response.get('age', None)
    gender = response.get('gender', 'Other')
    if not name:
      abort(422, {'message': 'name is blank'})

    if not age:
      abort(422, {'message': 'age is blank.'})

    # Create new instance of Actor & insert it.
    AddNewActor = (Actors(
          name = name, 
          age = age,
          gender = gender
          ))
    AddNewActor.insert()

    return jsonify({
      'success': True,
      'created': AddNewActor.id
    })

  @app.route('/actors/<actor_id>', methods=['PATCH'])
  @requires_auth('edit:actors')
  def edit_actors(payload, actorId):
    """Edit an existing Actor record

    """
    # Get request json
    response = request.get_json()

    # Abort if no actor_id or body has been provided
    if not actorId:
      abort(400, {'message': 'Actor id is blank'})

    if not response:
      abort(400, {'message': 'Invalid JSON body.'})
    TempActor = Actors.query.filter(Actors.id == actorId).one_or_none()

    # Abort 404 if no actor with this id exists
    if not TempActor:
      abort(404, {'message': 'Actor with id {} invalid'.format(actorId)})
    # no update will happen
    name = response.get('name', TempActor.name)
    age = response.get('age', TempActor.age)
    gender = response.get('gender', TempActor.gender)

    # Set new field values
    TempActor.name = name
    TempActor.age = age
    TempActor.gender = gender

    # Delete actor with new values
    TempActor.update()

    # Return success, updated actor id and updated actor as formatted list
    return jsonify({
      'success': True,
      'updated': TempActor.id,
      'actor' : [TempActor.format()]
    })

  @app.route('/actors/<actor_id>', methods=['DELETE'])
  @requires_auth('delete:actors')
  def delete_actors(payload, actorId):
    """Delete an existing Actor

    """
    # Abort if no actor_id has been provided
    if not actorId:
      abort(400, {'message': 'please append an actor id to the request url.'})
  
    # Find actor which should be deleted by id
    TempActor_tobe_deleted = Actors.query.filter(Actors.id == actorId).one_or_none()

    # If no actor with given id could found, abort 404
    if not TempActor_tobe_deleted:
        abort(404, {'message': 'Actor with id {} not found in database.'.format(actorId)})
    
    # Delete actor from database
    TempActor_tobe_deleted.delete()
    
    # Return success and id from deleted actor
    return jsonify({
      'success': True,
      'deleted': actorId
    })

  #----------------------------------------------------------------------------#
  # Endpoint /movies GET/POST/DELETE/PATCH
  #----------------------------------------------------------------------------#
  @app.route('/movies', methods=['GET'])
  @requires_auth('read:movies')
  def get_movies(payload):
    """Returns paginated movies object

    """
    result_movies = Movies.query.all()
    AllMovies = paginate_results(request, result_movies)

    if len(AllMovies) == 0:
      abort(404, {'message': 'no movies in the database.'})

    return jsonify({
      'success': True,
      'movies': AllMovies
    })

  @app.route('/movies', methods=['POST'])
  @requires_auth('create:movies')
  def insert_movies(payload):
    """Inserts a new movie

    """
    # Get request json
    response = request.get_json()

    if not response:
          abort(400, {'message': 'No json request found'})

    # Extract title and release_date value from request body
    title = response.get('title', None)
    release_date = response.get('release_date', None)

    # abort if one of these are missing with appropiate error message
    if not title:
      abort(422, {'message': 'no title provided.'})

    if not release_date:
      abort(422, {'message': 'no "release_date" provided.'})

    # Create new instance of movie & insert it.
    Add_Movie = (Movies(
          title = title, 
          release_date = release_date
          ))
    Add_Movie.insert()

    return jsonify({
      'success': True,
      'created': Add_Movie.id
    })

  @app.route('/movies/<movie_id>', methods=['PATCH'])
  @requires_auth('edit:movies')
  def edit_movies(payload, movie_id):
    """Edit an existing Movie

    """
    # Get request json
    responsebody = request.get_json()

    # Abort if no movie_id or body has been provided
    if not movie_id:
      abort(400, {'message': 'Movie id is blank'})

    if not responsebody:
      abort(400, {'message': 'invalid json'})

    # Find movie which should be updated by id
    TempMovie_tobe_Updated = Movies.query.filter(Movies.id == movie_id).one_or_none()

    # Abort 404 if no movie with this id exists
    if not TempMovie_tobe_Updated:
      abort(404, {'message': 'Movie with id {} not found in oyr database.'.format(movie_id)})

    # Extract title and age value from request body
    # If not given, set existing field values, so no update will happen
    title = responsebody.get('title', TempMovie_tobe_Updated.title)
    release_date = responsebody.get('release_date', TempMovie_tobe_Updated.release_date)

    # Set new field values
    TempMovie_tobe_Updated.title = title
    TempMovie_tobe_Updated.release_date = release_date

    # Delete movie with new values
    TempMovie_tobe_Updated.update()

    # Return success, updated movie id and updated movie as formatted list
    return jsonify({
      'success': True,
      'edited': TempMovie_tobe_Updated.id,
      'movie' : [TempMovie_tobe_Updated.format()]
    })

  @app.route('/movies/<movie_id>', methods=['DELETE'])
  @requires_auth('delete:movies')
  def delete_movies(payload, movie_id):
    """Delete an existing Movie


    """
    # Abort if no movie_id has been provided
    if not movie_id:
      abort(400, {'message': 'Movie id is blank'})
  
    # Find movie which should be deleted by id
    movie_to_delete = Movies.query.filter(Movies.id == movie_id).one_or_none()
    if not movie_to_delete:
        abort(404, {'message': 'Movie with id {} not found in our database.'.format(movie_id)})
  
    movie_to_delete.delete()
    
    # Return success and id from deleted movie
    return jsonify({
      'success': True,
      'deleted': movie_id
    })

  #----------------------------------------------------------------------------#
  # Error Handlers
  #----------------------------------------------------------------------------#

  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
                      "success": False, 
                      "error": 422,
                      "message": get_error_message(error,"unprocessable")
                      }), 422

  @app.errorhandler(400)
  def bad_request(error):
      return jsonify({
                      "success": False, 
                      "error": 400,
                      "message": get_error_message(error, "bad request")
                      }), 400

  @app.errorhandler(404)
  def ressource_not_found(error):
      return jsonify({
                      "success": False, 
                      "error": 404,
                      "message": get_error_message(error, "resource not found")
                      }), 404

  @app.errorhandler(AuthError)
  def authentification_failed(AuthError): 
      return jsonify({
                      "success": False, 
                      "error": AuthError.status_code,
                      "message": AuthError.error['description']
                      }), AuthError.status_code


  # After every endpoint has been created, return app
  return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)