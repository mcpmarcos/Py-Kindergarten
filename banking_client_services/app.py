from http import HTTPStatus

from fastapi import FastAPI

from banking_client_services.Schemas import (
    UserDB,
    UserList,
    UserPublic,
    UserSchema,
)

app = FastAPI()

database = []


@app.get("/", status_code=HTTPStatus.OK)
def readRoot():
    return {"message": "Hello World"}
 

@app.post("/user/", status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(
      id=len(database) + 1, 
      **user.model_dump())
    database.append(user_with_id)
    return user_with_id

@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users():
    return {'users': database}


 # read
 # update
 # delete
