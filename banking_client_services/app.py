from fastapi import FastAPI 
from http import HTTPStatus
from banking_client_services.Schemas import UserSchema

app = FastAPI()


@app.get("/", status_code=HTTPStatus.CREATED)
def readRoot():
    return {"message": "Hello World"}
 

@app.post("/user/", response_Model=UserSchema)
def create_user(user: UserSchema):
    return user
 
 
 # read
 # update
 # delete
