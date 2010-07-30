import pymongo
import re

def build_graph(graph):
    connection = pymongo.Connection('localhost', 27017)
    
    db_name = re.sub(r'[^\w]*', '', graph.name.lower())
    print 'Building graph: {0}'.format(db_name)
    try:
        connection.drop_database(db_name)
    except Exception as e:
        pass
    coll = connection[db_name]
    
    #insert the group
    groupid = coll.group.insert({'name':graph.name}, safe=True)
    
    #insert the users
    users = {}
    for user in graph.users:
        user['_id'] = coll.users.insert({'name':user['name'],
                                         'groupid':groupid},
                                         safe=True)
        users[user['name']] = user
    
    #insert the connections
    for connectiontype in graph.connections:
        connectiontypeid = coll.connectiontypes.insert({'name':connectiontype['name'],
                                                        'display_type':connectiontype['display_type']},
                                                        safe=True)
        for connection in connectiontype['data']:
            user1id = users[connection['user1']]['_id']
            user2id = users[connection['user2']]['_id']
            coll.connections.insert({'connectiontypeid': connectiontypeid,
                                     'groupid':groupid,
                                     'user1id':user1id,
                                     'user2id':user2id,
                                     'weights':[{'weight':connection['weight']}]},
                                     safe=True)
    