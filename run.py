from models.redis.connection.redis_connection import RedisConnectionHandle
from models.redis.redis_repository import RedisRepository

from configs.start_form import start_form

from datetime import datetime


data_atual = datetime.now()
data_formatada = data_atual.strftime("%Y-%m-%d")

redis_conn = RedisConnectionHandle().connect()
redis_repository = RedisRepository(redis_conn)
hash_item = redis_conn.hgetall(data_formatada)

print(hash_item)

redis_repository.insert_hash(data_formatada, 'banana', 3.12)

python_dict = { }

for key, value in hash_item.items():
    python_dict[key.decode('utf-8')]  = value.decode('utf-8')

start_form.load_info(python_dict)

value = start_form.get_info('banana')
print(value)