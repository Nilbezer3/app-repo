from fastapi import FastAPI

app = FastAPI()




@app.get("/health")
def health():
    return {"status": "ok"}
from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping():
    """Basic health check endpoint"""
    return {"status": "ok"}

@app.get("/greet/{name}")
def greet(name: str):
    """Returns a friendly greeting"""
    return {"message": f"Hello, {name}! Welcome to our API."}

@app.post("/sum")
def sum_numbers(a: int, b: int):
    """Adds two numbers and returns the result"""
    return {"result": a + b}
