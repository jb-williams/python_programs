from fastapi import FastAPI
import redis

app = FastAPI()

r = redis.Redis(host="redis", port=6379)

import debugpy
debugpy.listed(("0.0.0.0", 5678))
#debugpy.wait_for_client()

@app.get("/")
def read_root():
    return {"Hellow": "World"}

@app.get("/hits")
def read_root():
    r.incr("hits")
    return {"Number of hits": r.get("hits")}