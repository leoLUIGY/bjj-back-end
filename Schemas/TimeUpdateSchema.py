from pydantic import BaseModel

class TimeUpdateSchema(BaseModel):
    id: int

    nome: str
    pais: str
    data_fundacao: str
    nome_fundador: str
    descricao: str 
    logo_url: str | None = None