from fastapi import FastAPI

app = FastAPI(title="Smart Task Manager")

@app.get("/")
def root():
    return {"status": "ok", "message": "Smart Task Manager API running"}
