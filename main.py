from fastapi import FastAPI
from routes import products,jira

app = FastAPI()

app.include_router(products.router)
app.include_router(jira.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Dummy Product API"}