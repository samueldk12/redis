from models.redis.connection.redis_connection import RedisConnectionHandle
from models.redis.redis_repository import RedisRepository
from models.mysql.mysql_repository import MySqlRepository

redis_conn = RedisConnectionHandle().connect()
redis_repository = RedisRepository(redis_conn)
mysql_repository = MySqlRepository()

name = "Aroldo"

###################### Logica
value = redis_repository.get(name)
if value:
    print('Achei no Redis')
else:
    value_2 = mysql_repository.select_by_name(name)
    redis_repository.insert(name, value_2)