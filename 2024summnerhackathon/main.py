from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def 작명():
    return {}

