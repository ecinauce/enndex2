from dbmongo import doMongo
from pymongo import MongoClient
from bson.json_util import dumps
from class_user import User

class MongoUserFactory(object):
  @staticmethod
  def createUser(p_username, p_password, p_email):
    invokeDb = doMongo()
    db = invokeDb.client
    
    thisDb = db.ennchandb
    userTable = thisDb.user
    result = userTable.insert({"username":p_username,"password":p_password,"email":p_email})
    
    return dumps(result)
  
  @staticmethod
  def createUserFromId(p_id):
    invokeDb = doMongo()
    db = invokeDb.client
    
    userTable = db.user
    rawUserInstance = userTable.find_one({"_id":p_id})
    result = (dumps(rawUserInstance),)
    
    outUser = User()
    outUser.setId(result['_id'])
    outUser.setName(result['username'])
    outUser.setEmail(result['email'])
    
    return outUser
    
  @staticmethod
  def createUserFromName(p_username):
    invokeDb = doMongo()
    db = invokeDb.client
    
    userTable = db.user
    rawUserInstance = userTable.find_one({"username":p_username})
    result = (dumps(rawUserInstance),)
    
    outUser = User()
    outUser.setId(result['_id'])
    outUser.setName(result['username'])
    outUser.setEmail(result['email'])
    
    return outUser