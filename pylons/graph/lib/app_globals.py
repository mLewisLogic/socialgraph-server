"""The application's Globals object"""

from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options
from pylons import config
from pymongo.connection import Connection
from pymongo.errors import ConnectionFailure

class Globals(object):
    """Globals acts as a container for objects available throughout the
    life of the application

    """

    def __init__(self, config):
        """One instance of Globals is created during application
        initialization and is available during requests via the
        'app_globals' variable

        """
        self.cache = CacheManager(**parse_cache_config_options(config))

        """ MongoDB configuration """
        db_info = {'host': config['graph.database.host'],
                   'port': int(config['graph.database.port']),
                   'db': config['graph.database.db'],
                   'username': config['graph.database.username'],
                   'password': config['graph.database.password']}
        
        # Populate basic app globals
        try:
            conn = Connection(host=db_info['host'],
                              port=db_info['port'])
        except ConnectionFailure:
            raise Exception('Unable to connect to MongoDB')
        self.db = conn[db_info['db']]
        #auth = self.db.authenticate(db_info['username'], db_info['password'])
        #if not auth:
        #    raise Exception('Authentication to MongoDB failed')
        