from app import app
from flask_openapi3 import Tag
from Schemas import *

time_tag = Tag(name="Time", description="Adição, edição, visualização e remoção de um novo time")

@app.get('/times', tags=[time_tag], responses={"200", "404"})
def get_times():
    """Buscar equipes de jiujitsu
    """
    session = Session()

@app.get('/time', tags=[time_tag])
def get_time(query: TimeBuscaSchema):
    pass

@app.post('/time', tags[time_tag])
def add_time(form: TimeSchema):
    pass

@app.put('/time', tags[time_tag])
def update_time(form: TimeUpdateSchema):
    pass

@app.delete('/time', tags=[time_tag])
def delete_time(query: TimeBuscaSchema):
    pass