try:
    import redis
    from redis.connection import ConnectionError
    
except ImportError:
    pass


class CacheRedis():    
    def __init__(self, config):
        self.redis_con = redis.StrictRedis(host=config.REDIS_HOST, port=config.REDIS_PORT, password=config.REDIS_PWD, db=config.REDIS_DB,
            charset="utf-8", decode_responses=True)            
        
    def ping(self):    
        try:            
            ping = self.redis_con.ping()
        except NameError:
            return {'error': 'cannot import redis library'}
        except ConnectionError as e:
            return {'error': str(e)}

        print( {
                'ping': ping,
                'version': self.redis_con.info().get('redis_version')
            })

    def hset(self, session, key, value):
        self.redis_con.hset(session,key, value)

    def hget(self, session, key, default):
        try:
            return self.redis_con.hget(session,key)
        except:
            return default    

    def set(self, key, value):
        self.redis_con.set(key,value)

    def get(self, key, default):
        try:
           res = self.redis_con.get(key)
        except:
            res = default
        return res


class CacheForTest:
    def __init__(self,config):        
        self.session_dict = {}
        self.session_dict["__shared__"] = {}
    
    def ping(self):
        pass

    def hset(self, session, key, value):        
        if self.session_dict.get(session) == None:
            self.session_dict[session] = {}
        
        self.session_dict[session][key] = value

    def hget(self, session, key, default):
        try:
            return self.session_dict[session][key]
        except:
            return default    

    def set(self, key, value):
        self.session_dict["__shared__"][key] = value

    def get(self, key, default):
        try:
           res = self.session_dict["__shared__"][key]
        except:
            res = default
        return res





