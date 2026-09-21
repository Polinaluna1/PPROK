from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Git REST Lab 2 service is running"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}