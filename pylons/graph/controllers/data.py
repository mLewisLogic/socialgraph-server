import json
import igraph
import logging
import os
import tempfile

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from graph.lib.base import BaseController, render

from graph.model.Connections import Connections
from graph.model.Users import Users

log = logging.getLogger(__name__)

class DataController(BaseController):
    def all(self, id=None):
        connections = Connections(id)
        users = Users()
        data = {'connections': connections.connections,
                'users': users.users}
        return json.dumps(data)
    
    def all_igraph(self):
        connections = Connections()
        users = Users()
        newgraph = igraph.Graph.DictList(users.users,
                                         connections.connections,
                                         False,
                                         '_id',
                                         ('id1', 'id2'))
        (h,f) = tempfile.mkstemp(text=True)
        os.close(h)
        newgraph.write_graphml(f)
        graphfile = open(f)
        dataobj = graphfile.read()
        graphfile.close()
        return dataobj
    
    def connections(self, id=None):
        connections = Connections(id)
        return json.dumps(connections.connections)
    
    def users(self):
        users = Users()
        return json.dumps(users.users)
    
