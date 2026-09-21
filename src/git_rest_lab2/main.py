from fastapi import FastAPI

app = FastAPI(
    title="Git REST Lab 2",
    version="1.0.0",
)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Git REST Lab 2 service is running"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/hello/{name}")
def hello_user(name: str) -> dict[str, str]:
    return {"message": f"Hello, {name}!"}

@app.get("/about")
def about_service() -> dict[str, str]:
    return {
        "service": "Git REST Lab 2",
        "framework": "FastAPI",
    }
@app.get("/version")
def service_version() -> dict[str, str]:
    return {"version": "1.0.0"}