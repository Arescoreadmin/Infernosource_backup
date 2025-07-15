import redis
import os

redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")

try:
    redis_client = redis.Redis.from_url(redis_url)
    redis_client.ping()
    print("✅ Redis connected")
except redis.exceptions.ConnectionError:
    print("❌ Redis connection failed")
