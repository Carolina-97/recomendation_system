from fastapi import FastAPI, HTTPException
import requests
import asyncio
import redis

app = FastAPI()
redis_conn = redis.Redis(host='localhost', port=6379, db=0)

local_cache = {}
@app.get("/recommend/")
async def recommend(viewerid: int):
    cache_key = f"viewer:{viewerid}"
    if cache_key in local_cache:
        return local_cache[cache_key]

    cached_value = redis_conn.get(cache_key)

    if cached_value:
        return {"result": cached_value.decode()}

    recommendations = await runcascade(viewerid)
    local_cache[cache_key] = recommendations
    redis_conn.setex(cache_key, 60, str(recommendations))
    return recommendations

async def runcascade(viewerid: int):
    model_names = [f"Model{i}" for i in range(5)]
    tasks = [asyncio.create_task(call_generator_service(model, viewerid)) for model in model_names]
    results = await asyncio.gather(*tasks)
    return results

async def call_generator_service(model_name: str, viewerid: int):
    response = requests.post("http://localhost:8001/generate/", json={"model_name": model_name, "viewerid": viewerid})
    return response.json()
