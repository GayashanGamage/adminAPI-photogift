from upstash_redis import Redis

class CachService:

    def __init__(self, redis_url, redis_token):
        # print(redis_url, redis_token)
        self.redis = Redis(redis_url, redis_token)

    def get_cache(self):
        return self.redis
