# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, USER, PASS): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = 'aacuser' 
        PASS = 'password' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        # If something got passed in, try to insert it
        if data is not None:
             try:
                 if ( self.database.animals.insert_one(data) ) != 0 :
                     # If insertion succeeds, return true
                     return True
                 else:
                     # If insertion fails, return false
                     return False
            # If the input exists but is invalid, display an error message and return false
             except Exception as e:
                  print({e.__class__.__name__})
                  return False
        else:
            # If there is no input, display an error message
            raise Exception("Nothing to save, because data parameter is empty")
        return False 

    # Create method to implement the R in CRUD.
    def read(self,query=None):
        # Make sure a query got passed in
        if query is not None:
            # If the query isn't empty, try to search for it
            try:
                result = list(self.database.animals.find(query,{'_id':False}))
            # If the query exists, but is invalid, catch the exception, display an error message,
            # and return an empty list
            except Exception as e:
                print({e.__class__.__name__})
                result = list()
        else:
            # If the query is empty, return an empty list
            result = list()
        return result
    
    # Update method to implement the U in CRUD
    def update(self, query: dict, update_data: dict) -> int:
        
        # Check if both required arguments are dictionaries
        if query is None or update_data is None or not isinstance(query, dict) or not isinstance(update_data, dict):
            print("Error: Query and update_data must be non-None dictionaries.")
            return 0
        
        # Use update_many to change all matching documents
        try:
            # Use update_many for flexibility, as the requirement allows changing "document(s)"
            update_result = self.collection.update_many(query, update_data)
            
            # Return the number of documents modified
            return update_result.modified_count
            
        except Exception as e:
            print(f"Update Error: {e.__class__.__name__} - {e}")
            return 0
        
    def delete(self, query: dict) -> int:
       
        # Check if the required argument is a dictionary
        if query is None or not isinstance(query, dict):
            print("Error: Query must be a non-None dictionary.")
            return 0
        
        # Use delete_many to remove all matching documents
        try:
            # Use delete_many for flexibility, as the requirement allows removing "document(s)"
            delete_result = self.collection.delete_many(query)
            
            # Return the number of documents deleted
            return delete_result.deleted_count
            
        except Exception as e:
            print(f"Delete Error: {e.__class__.__name__} - {e}")
            return 0
   