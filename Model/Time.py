from sqlalchemy import Column, Integer, String
from Model import Base

class Time(Base):
    __talename__ = 'time'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    pais = Column(String(100), nullable=False)
    data_fundacao = Column(String(20))
    nome_fundador = Column(String(100))
    descricao = Column(String(500))
    logo_url = Column(String(500))
