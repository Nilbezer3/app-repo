from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping():
    return {"ok": True}


@app.get("/health")
def health():
    return {"status": "ok"}
