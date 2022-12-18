from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, username, password):
        if username and password:    
            self.client = MongoClient('mongodb://%s:%s@localhost:54221/AAC' % ("myAACuser", "password"))
            self.database = self.client ['AAC']
            
    #method to implement C in CRUD        
    def create(self, data):
        if data:
            #variable to store data in
            insertData = self.database.animals.insert_one(data) # data should be dictionary
            #if insert was successful return true
            return True if insertData.acknowledged else False
        
        else: 
            raise Exception ("Nothing to save, because data parameter is empty.")
        
            
    #method to implement R in CRUD
    def read(self, search):
        if search:
            searchResult = self.database.animals.find(search, {"_id":False})
            return searchResult
        else:
            searchResult = self.database.animals.find({}, {"_id":False})
            return searchResult
        
            
    #method to implement U in CRUD
    def update(self, query, newValue):
        if not query:
            raise Exception("No search criteria.")
        elif not newValue:
            raise Exception("No update value.")
        else:
            updateData = self.dataBase.animals.update_many(query, {"$set": newValue})
            self.recordsUpdated = updateData.modified_count
            self.recordsMatched = updateData.matched_count
            
            return True if updateData.modified_count > 0 else False
            
    #method to implement D in CRUD
    def delete(self, data):
        if not data:
            raise Exception("Record not found.")
        else:
            deleteValid = self.dataBase.animals.delete_many(data)
            self.recordsDeleted = deleteValid.deleted_count
            
            return True if deleteValid.deleted_count > 0 else False
            
            

                                      