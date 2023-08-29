import asyncio
import aioredis

async def main():
    redis = aioredis.from_url(
        redis://127.0.0.1, port=6379, db=0, encoding="utf-8", decode_responses=True
    )
    async with redis.client() as conn:
        await conn.set("my-key", "value")
        conn.set("my-key", "value")
        val = await
        conn.get("my-key")
        print(val)


    async def redis_pool():
        # Redis client bound to pool of connections (auto-reconnecting).
        redis = aioredis.from_url(
            "redis://localhost", encoding="utf-8", decode_responses=True
        )
        await redis.set("my-key", "value")
        val = await redis.get("my-key")
        print(val)