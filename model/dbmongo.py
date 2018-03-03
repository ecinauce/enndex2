from pymongo import MongoClient

class doMongo(object):
  def __init__(self):
    #Deployment DB
    #self.client = MongoClient('mongodb://userUIA:8YhwyYPaUmfH4Khx@mongodb/ennchandb')
    #Development DB
    self.client = MongoClient('mongodb://mongodb:08v1qNwxaSgCKvge@cluster0-shard-00-00-bkv3m.mongodb.net:27017,cluster0-shard-00-01-bkv3m.mongodb.net:27017,cluster0-shard-00-02-bkv3m.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin')
    
  def client(self):
    return self.client