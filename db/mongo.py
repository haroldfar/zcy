from pymongo import MongoClient
client = MongoClient()

def get_client():
	if client:
		return client
	else:
		return MongoClient()