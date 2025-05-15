from fastapi import FastAPI
from routes import products

app = FastAPI()

app.include_router(products.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Dummy Product API"}