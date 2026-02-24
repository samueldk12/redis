""" Comandos Redis Básicos """
import redis
import json
import random
from uuid import uuid4

redis_connection = redis.Redis(host='localhost', port='6379', db=0)

print(redis_connection.get('9880336266292826').decode('utf-8'))


redis_connection.hset('h1', 'nome', 'Samuel')
redis_connection.hset('h1', 'idade', 26)
redis_connection.delete('chave_1')

nome = redis_connection.hget('h1','nome').decode('utf-8')
idade = redis_connection.hget('h1','idade').decode('utf-8')

print(redis_connection.exists('h1'))
print(redis_connection.exists('h2'))

print(nome, idade)
# for i in range(10_000_000):
#     num_random = f'{int(random.random() * 10_000_000_000)}{i}'
#     redis_connection.set(num_random, str(uuid4()))
