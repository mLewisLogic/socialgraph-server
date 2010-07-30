from pylons import config

db = config['pylons.app_globals'].db

def get_weight(weight_dict): return weight_dict['weight']

class Connections():
    def __init__(self, name=None):
        self.connections = []
        
        # Get the specific connectiontype
        if name:
            conntype = db.connectiontypes.find_one({'name':name})
            if conntype:
                conntypeid = conntype['_id']
            else:
                return
            connections = db.connections.find({'connectiontypeid':conntypeid})
        else:
            connections = db.connections.find()
        
        # Rip through connections in the DB
        for connection in db.connections.find():
            weights = connection['weights']
            weight = sum(map(get_weight,weights)) / len(weights)
            if weight > 0.3:
                self.connections.append({'id1': str(connection['user1id']),
                                         'id2': str(connection['user2id']),
                                         'weight': weight})
