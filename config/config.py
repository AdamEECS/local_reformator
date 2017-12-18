from pymongo import *

config_dict = dict()

# mongodb config
db_name = 'local_platform'
client = MongoClient("mongodb://localhost:27017")
db = client[db_name]
