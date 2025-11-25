# POST Y PUT

## Indice 

+ [Informacion Adicional](post-put-informacion-adicional.md)
+ [Post](#post)

## Post 

__post__ es un endpoint que en vez de traer informacion lo que hace es enviarla , con post podemos crear nuevos datos en lugar de traerlos.

```python
@app.post("/users")
async def create_user(user: User):
    u_list.append(user)
    return {"message": "Usuario creado", "user": user}
```

---

