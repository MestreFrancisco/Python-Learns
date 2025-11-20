## Post 

post es un endpoint que en vez de traer informacion lo que hace es enviarla

```python
@app.post("/users")
async def create_user(user: User):
    u_list.append(user)
    return {"message": "Usuario creado", "user": user}
```

