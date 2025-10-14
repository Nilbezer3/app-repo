from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/ping")
def ping():
    """Basic liveness probe"""
    return {"status": "ok"}

@app.get("/health")
def health():
    """Detailed health check"""
    return {"status": "ok"}

@app.get("/greet/{name}")
def greet(name: str):
    """Returns a friendly greeting"""
    return {"message": f"Hello, {name}! Welcome to our API."}

@app.post("/sum")
def sum_numbers(a: int, b: int):
    """Adds two numbers given as query params (?a=1&b=2)"""
    return {"result": a + b}

@app.get("/version")
def version():
    """Returns API version (static for demo)"""
    return {"version": "1.0.0"}

@app.get("/time")
def time():
    """Returns current server time"""
    return {"time": datetime.utcnow().isoformat() + "Z"}

@app.get("/echo")
def echo(msg: str = "hello"):
    """Echoes a message via query param (?msg=...)"""
    return {"echo": msg}
