from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id:int
    name:str
    surname:str
    age:int
    

u_list = [
    User(id=1, name="Fran", surname="Mestre", age=22),
    User(id=2, name="Franco", surname="Mendez", age=26),
    User(id=3, name="Juliana", surname="Serrano", age=22),
]

@app.get("/")
async def root():
    return {"message":"Hola Wacho"}

@app.get("/users")
async def get_users(id: int | None = None):
    if id is None:
        return u_list
    return search_by_user(id)

@app.get("/users/{id}")
async def get_user_by_path(id: int):
    return search_by_user(id)

@app.post("/users")
async def create_user(user: User):
    u_list.append(user)
    return {"message": "Usuario creado", "user": user}

def search_by_user(id:int):
    result = next((u for u in u_list if u.id == id), None)
    return result if result else {"error": "Usuario no encontrado"}


# Filtrando usuarios cuyo nombre empieza con "fr"
filtered_users = filter(lambda u: u.name.lower().startswith("fr"), u_list)

# Convertimos el filtro en una lista para ver los resultados
filtered_users_list = list(filtered_users)

# Mostramos los resultados
for user in filtered_users_list:
    print(user.name)
