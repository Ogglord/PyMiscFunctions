### Class to handle most calls to cache/zip/settings/mail/cache variables etc..
import tempfile
### our modules
from .fucache import Cache as c
from .fuzip import Zip as z


class Session():
    def __init__(self, config, sessionid):
        self.config = config
        self.sessionid=sessionid
        self.cache = c(self.config)
        self.zip = z(self.config)
        # test connection
        self.cache.ping()


    def set(self, key, value):
        self.cache.hset(self.sessionid,key, value)

    def get(self, key, default):
        return self.cache.hget(self.sessionid,key, default)

    def __getitem__(self,key):
        return self.get(key,None)

    def __setitem__(self,key,value):
        self.set(key,value)

    def getall(self):
        return self.cache.redis_con.hgetall(self.sessionid)

    ### takes a list of name+byte array and converts to a zip file in temp folder
    def zipfiles(self,files):
        return self.zip.zipfiles(files)








 