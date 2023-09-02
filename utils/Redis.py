import redis

from utils.file import read_config

config = read_config("redis.yaml")
PORT = config['redis']['port']
HOST = config['redis']['cluster-ip']
PASSWORD = config['redis']['password']
DB = config['redis']['database']
print(PORT,HOST,PASSWORD,DB)
redis_pool = redis.ConnectionPool(
    host=HOST,
    port=PORT,
    password=PASSWORD,
    db=DB,
    decode_responses=True)

redis_conn = redis.Redis(connection_pool=redis_pool)