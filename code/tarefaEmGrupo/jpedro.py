from pydantic import BaseModel
class Usuario(BaseModel):
    nome: str
    idade: int
    email: str
usuario=Usuario(nome="joa",idade=54,email="ale@santos.com")
print(usuario.nome)
print(usuario.idade)
print(usuario.email)

from pydantic import BaseModel
class Usuario(BaseModel):
    nome: str
    idade: int
    sexo: str
usuario=Usuario(nome="joa",idade=54,sexo="indefinido")
print(usuario.nome)
print(usuario.idade)
print(usuario.sexo)
