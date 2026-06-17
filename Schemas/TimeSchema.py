from pydantic import BaseModel

class TimeSchema(BaseModel):
    nome: str
    pais: str
    data_fundacao: str
    nome_fundador: str
    descricao: str
    logo_url: str