# Сервер Redis

from tkinter import DISABLED

import redis
from random import randint

with redis.Redis() as server_redis:
    server_redis.lpush("queue", randint(1, 99))
