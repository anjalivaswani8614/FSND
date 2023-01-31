import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, db_fresh_db, Actors, Movies, Performance, db_fresh_db
from config import bearer_tokens
from sqlalchemy import desc
from datetime import date

# Create dict with Authorization key and Bearer token as values. 
# Later used by test classes as Header

casting_assistant_auth_header = {
    'Authorization': bearer_tokens['casting_assistant']
}

casting_director_auth_header = {
    'Authorization': bearer_tokens['casting_director']
}

executive_producer_auth_header = {
    'Authorization': bearer_tokens['executive_producer']
}


#----------------------------------------------------------------------------#
# RBAC Tests I: Missing Authorization | Missing Authentificaton
#   Casting Assistant:
#   - tes

#----------------------------------------------------------------------------#

#----------------------------------------------------------------------------#
# Setup of Unittest
#----------------------------------------------------------------------------#

class Agency(unittest.TestCase):
    """This class represents the agency test case"""

    def setUp(self):
        """Define test variables and initialize app."""

        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.environ['DATABASE_URL']
        setup_db(self.app, self.database_path)
        db_fresh_db()
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

# Test driven development (TDD): Create testcases first, then add endpoints to pass tests

#----------------------------------------------------------------------------#
# Test cases to validate API  /actors POST
#----------------------------------------------------------------------------#

    def testcase_forerror_401_new_actor(self):
        """Testcase to verify Post API for create new actor without Authorization."""

        new_actor_json = {
            'name' : 'Ranveer Singh',
            'age' : 25
        } 

        response = self.client().post('/actors', json = new_actor_json)
        body = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertFalse(body['success'])
        self.assertEqual(body['message'], 'Authorization header missing')

    def testcase_forerror_422_create_new_actor(self):
        """Testcase to verify Post API for create new actor generating an error"""

        new_actor_json_without_name = {
            'age' : 35
        } 

        response = self.client().post('/actors', json = new_actor_json_without_name, headers = casting_director_auth_header)
        body = json.loads(response.data)

        self.assertEqual(response.status_code, 422)
        self.assertFalse(body['success'])
        self.assertEqual(body['message'], 'no name provided.')

    def testcase_tocheck_create_newactor(self):
        """Testcase to verify Post API for create new actor"""

        new_actor_json = {
            'name' : 'Salman Khan',
            'age' : 55
        } 

        response = self.client().post('/actors', json = new_actor_json, headers = casting_director_auth_header)
        body = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(body['success response'])
        self.assertEqual(body['record created'], 2)
    
    

#----------------------------------------------------------------------------#
# Tests for /actors GET GET all actors , checking without authorisation
#----------------------------------------------------------------------------#

    def testcase_forerror_404_get_actors_api(self):
        """Testcase to validate error while getting all the actors from the list"""
        response = self.client().get('/actors?page=5000', headers = casting_assistant_auth_header)
        body = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertFalse(body['data found'])
        self.assertEqual(body['message'] , 'no actors found in database.')
   
    def testcase_toget_all_actors_api(self):
        response = self.client().get('/actors?page=1', headers = casting_assistant_auth_header)
        body = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(body['success'])
        if(len(body['actors']) > 0):
            print("Actors list is greater than 0")
        self.assertTrue(len(body['actors']) > 0)

    def testcase_forerror_401_get_all_actors_api(self):
        response = self.client().get('/actors?page=1')
        body = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertFalse(body['success'])
        self.assertEqual(body['message'], 'Authorization header is missing')

    

#----------------------------------------------------------------------------#
# Test cases to verify the API /actors PATCH
#----------------------------------------------------------------------------#

    def testcase_tocheck_edit_actor(self):
        """Test case to check patch for only existing actors"""
        json_Actor_newage_edit = {
            'age' : 42
        } 
        response = self.client().patch('/actors/1', json = json_Actor_newage_edit, headers = casting_director_auth_header)
        jsondata = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(jsondata['Data updated'])
        self.assertTrue(len(jsondata['actor']) > 0)
        self.assertEqual(jsondata['updated'], 1)

        """Testcase to check patch request with non json body"""
    def testcase_tocheck_error_400_edit_actor_patchapi(self):
            response = self.client().patch('/actors/124720', headers = casting_director_auth_header)
            body = json.loads(response.data)

            self.assertEqual(response.status_code, 400)
            self.assertFalse(body['data request sucess'])
            self.assertEqual(body['message'] , 'request is invalid json body.')
    
    
    """Test case with invalid actor id """
    def test_case_tocheck_error_404_edit_actor_patchapi(self):
        
        json_Actor_newage_edit = {
            'age' : 62
        } 
        response = self.client().patch('/actors/124720', json = json_Actor_newage_edit, headers = casting_director_auth_header)
        body = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertFalse(body['success request , assert false'])
        self.assertEqual(body['message'] , 'Actor with id 124720 not found in database.')

#----------------------------------------------------------------------------#
# Test cases to verify the functionality API for /actors DELETE
#----------------------------------------------------------------------------#
        """Testcase to Delete existing actor without using  Authorization"""
    def testcase_tocheck_error_401_delete_actor_deleteapi(self):
       
        response = self.client().delete('/actors/1')
        responsebody = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertFalse(responsebody['success'])
        self.assertEqual(responsebody['message'], 'Authorization header is expected.')


        """Testcase to Delete an existing actor with some permissions missing in the request"""
    def testcase_tocheck_error_403_delete_actor(self):
        response = self.client().delete('/actors/1', headers = casting_assistant_auth_header)
        responsebody = json.loads(response.data)

        self.assertEqual(response.status_code, 403)
        self.assertFalse(responsebody['success'])
        self.assertEqual(responsebody['message'], 'Permission not found.')

        """Test case to check and validate delete actor functionality"""
    def testcase_tocheck_delete_actor(self):
        response = self.client().delete('/actors/1', headers = casting_director_auth_header)
        responsebody = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(responsebody['success'])
        self.assertEqual(responsebody['deleted'], '1')

        """Test case to check and validate delete non actor functionality"""
    def testcase_tocheck_error_404_delete_actor(self):
        response = self.client().delete('/actors/100355', headers = casting_director_auth_header)
        responsebody = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertFalse(responsebody['success'])
        self.assertEqual(responsebody['message'] , 'Actor with id 100355 not found in database.')

#----------------------------------------------------------------------------#
# Tests to verify the API  /movies POST
#----------------------------------------------------------------------------#

    def testcase_tocheck_error_422_create_new_movie(self):
        """Testcase to create a new movie without a name"""

        newmovie_withoutname_json = {
            'release_date' : date.today()
        } 

        response = self.client().post('/movies', json = newmovie_withoutname_json, headers = executive_producer_auth_header)
        responsebody = json.loads(response.data)

        self.assertEqual(response.status_code, 422)
        self.assertFalse(responsebody['success'])
        self.assertEqual(responsebody['message'], 'no title provided.')

        """Test case to verify POST API for  new movie.""" 
    def testcase_to_create_new_movie_postapi(self):
        newmovie_json = {
            'title' : 'Love you Zindagi',
            'release_date' : date.today()
        } 

        response = self.client().post('/movies', json = newmovie_json, headers = executive_producer_auth_header)
        responsebody = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(responsebody['success'])
        self.assertEqual(responsebody['created'], 2)

    
#----------------------------------------------------------------------------#
# Tests for /movies GET
#----------------------------------------------------------------------------#

        """Test case to check errior while getting all the movie names using a get request"""
    def testcase_tocheck_error_404_get_movies(self):
        response = self.client().get('/movies?page=1125125125', headers = casting_assistant_auth_header)
        responsebody = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertFalse(responsebody['success'])
        self.assertEqual(responsebody['message'] , 'no movies found in database.')

    def test_error_401_get_all_movies(self):
        """Test case to get all the movie names using a get request without Authorization."""
        response = self.client().get('/movies?page=1')
        responsebody = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertFalse(responsebody['success'])
        self.assertEqual(responsebody['message'], 'Authorization header is expected.')

    
    def testcase_get_all_movies_getapi(self):
        """Test case to get all the movie names using a get request"""
        response = self.client().get('/movies?page=1', headers = casting_assistant_auth_header)
        responsebody = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(responsebody['success'])
        self.assertTrue(len(responsebody['movies']) > 0)

#----------------------------------------------------------------------------#
# Tests for /movies PATCH
#----------------------------------------------------------------------------#

    def testcase_edit_movie_patchapi(self):
        """Test case to check the PATCH  request for existing movies"""
        patch_request_edit_movie = {
            'release_date' : date.today()
        } 
        response = self.client().patch('/movies/1', json = patch_request_edit_movie, headers = executive_producer_auth_header)
        responsebody = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(responsebody['success'])
        self.assertTrue(len(responsebody['movie']) > 0)


    def testcase_error_404_edit_movie_patchapi(self):
        """Test case to check the PATCH  request with non valid id"""
        json_invalid_movie_id = {
            'release_date' : date.today()
        } 
        response = self.client().patch('/movies/245678', json = json_invalid_movie_id, headers = executive_producer_auth_header)
        responsebody = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertFalse(responsebody['success'])
        self.assertEqual(responsebody['message'] , 'Movie with id 245678 not found in database.')

    def testcase_error_400_edit_movie_patxhapi(self):
        """Test case to check the PATCH  request with non valid id json body"""
        response = self.client().patch('/movies/1', headers = executive_producer_auth_header)
        responsebody = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertFalse(responsebody['success'])
        self.assertEqual(responsebody['message'] , 'request does not contain a valid JSON body.')

#----------------------------------------------------------------------------#
# Test cases to verify API /movies DELETE
#----------------------------------------------------------------------------#
        """Testcase to chcek the delete existing movie functionality"""
    def testcase_tocheck_delete_movie_api(self):
        response = self.client().delete('/movies/1', headers = executive_producer_auth_header)
        responsebody = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(responsebody['success'])
        self.assertEqual(responsebody['deleted'], '1')

        """Testcase to chcek the delete existing movie functionality""""
    def testcase_tocheck_error_404_delete_movie(self):
        response = self.client().delete('/movies/121345', headers = executive_producer_auth_header) 
        responsebody = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertFalse(responsebody['success'])
        self.assertEqual(responsebody['message'] , 'Movie with id 121345 not found in database.')

    
        """Testcase to validate and check delete functionality for  existing movie without Authorization"""
    def testcase_tocheck_error_401_delete_movie(self):
        response = self.client().delete('/movies/1')
        responsebody = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertFalse(responsebody['success'])
        self.assertEqual(responsebody['message'], 'Authorization header is expected.')

        """Test case to validate the DELETE functionality for existing movie with the wrong permissions"""
    def testcase_tocheck_error_403_delete_movie(self):
        response = self.client().delete('/movies/1', headers = casting_assistant_auth_header)
        responsebody = json.loads(response.data)
        self.assertEqual(response.status_code, 403)
        self.assertFalse(responsebody['success'])
        self.assertEqual(responsebody['message'], 'Permission not found.')

    
# Make the tests conveniently executable.
# From app directory, run 'python test_app.py' to start tests
if __name__ == "__main__":
    unittest.main()