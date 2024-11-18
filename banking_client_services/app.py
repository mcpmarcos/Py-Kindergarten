from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def readRoot():
    return {"message": "Hello World"}
