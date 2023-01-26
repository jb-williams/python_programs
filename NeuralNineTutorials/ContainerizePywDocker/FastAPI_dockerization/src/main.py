# fastapi docker containerization

# will need to pip3 install:
#   fastapi uvicorn

# to give specific name and containerize run:
# docker build -t neural-api .
# docker run -p 8000:8000 --name mycontainername neural-api

import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def central_function():
    return {"Neural": "Nine"}

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")