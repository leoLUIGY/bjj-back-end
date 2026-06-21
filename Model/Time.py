from sqlalchemy import Column, Integer, String
from Model.Base import Base

class Time(Base):
    __tablename__ = 'time'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    pais = Column(String(100), nullable=False)
    data_fundacao = Column(String(20))
    nome_fundador = Column(String(100))
    descricao = Column(String(500))
    logo_url = Column(String(500))

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "pais": self.pais,
            "data_fundacao": self.data_fundacao,
            "nome_fundador": self.nome_fundador,
            "descricao": self.descricao,
            "logo_url": self.logo_url
        }