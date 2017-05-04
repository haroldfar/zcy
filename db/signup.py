import mongo
from time import gmtime, strftime

_db = mongo.get_client()['Sports']


def sign_up(sports, event_id, user_id, user_name):
	_db[sports+"_signup"].insert_one({'event_id': event_id, 'user_id':user_id, 'user_name': user_name, 'signup_time': strftime("%Y-%m-%d %H:%M:%S", gmtime())})

def add_event(sports, added_by, time, place, maximum_persons):
	_db[sports+"_event"].insert_one({'event_id': get_iterator(), 'added_by': added_by, 'time':time, 'place': place, 'add_time': strftime("%Y-%m-%d %H:%M:%S", gmtime())})

def get_iterator():
	current = _db["iterator"].find_one()
	if not current:
		_db["iterator"].insert_one({"next_no": 3000000})
		return 3000000
	else:
		_db["iterator"].update_one({"next_no":current['next_no']}, {"$set": {"next_no": current['next_no'] + 1}})
		return current['next_no'] + 1

# print get_iterator()
add_event('badminton', 'czha', '4 May, Thursday', 'Pasir Ris Sports Hall', 10)
# sign_up('badminton', '000023', 'czha', 'Chiyuan Zhang')
