from pylons import config

db = config['pylons.app_globals'].db

class Users():
    def __init__(self):
        self.users = []
        for user in db.users.find():
            self.users.append({'_id':str(user['_id']),
                               'name':str(user['name'])})
