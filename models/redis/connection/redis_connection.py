from .connections_options import connection_options

from redis import Redis

class RedisConnectionHandle:
    def __init__(self) -> None:
        self.connection_options = connection_options
        self.redis_connection = None
    
    def connect(self) -> Redis:
        self.__connection = Redis(**self.connection_options)
        return self.__connection
