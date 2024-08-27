import uvicorn
from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
async def beginning():
    data = '"Главная страница"'
    return Response(content=data,media_type="text/plain")

@app.get("/user/admin")
async def personality():
    data = '"Вы вошли как администратор"'
    return Response(content=data, media_type="text/plain")

@app.get("/user/{user_id}")
async def your_number(user_id: int):
    data = '"Вы вошли как пользователь №' f'{user_id}"'
    return Response(content=data, media_type="text/plain")

@app.get("/user/{username}/{age}")
async def user_information(username: str, age: int):
    data = '"Информация о пользователе. Имя:'f'{username}' ', Возраст:'f'{age}".'
    return Response(content=data, media_type="text/plain")