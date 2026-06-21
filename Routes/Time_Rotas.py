from app import app
from sqlalchemy.exc import IntegrityError
from flask_openapi3 import Tag
from Schemas.TimeBuscaSchema import TimeBuscaSchema
from Schemas.TimeSchema import TimeSchema
from Schemas.TimeUpdateSchema import TimeUpdateSchema
from Model import *

home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
time_tag = Tag(name="Time", description="Adição, edição, visualização e remoção de um novo time")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.get('/times', tags=[time_tag])
def get_times():
    """Buscar equipes de jiujitsu
    """
    session = Session()
    try:
        times = session.query(Time).all()

        if not times:
            return {"Times":[]} , 200
        else:
            return [time.to_dict() for time in times]
    finally:
        session.close()

@app.get('/time', tags=[time_tag])
def get_time(query: TimeBuscaSchema):
    """Buscar um time especifico
    """
    time_id = query.id
    session = Session()
    try:
        time = session.query(Time).filter(Time.id == time_id).first()
        if not time:
            error_msg = "Time não encontrado na base :/"
            return {"mesage": error_msg}, 404
        else:
            return time.to_dict()
    finally:
        session.close()

@app.post('/time', tags=[time_tag])
def add_time(form: TimeSchema):
    """ Adicionar um novo time
    """
    time = Time(
        nome = form.nome,
        pais = form.pais,
        data_fundacao = form.data_fundacao,
        nome_fundador = form.nome_fundador,
        descricao = form.descricao,
        logo_url = form.logo_url
    )
    session = Session()
    try:
       
        session.add(time)
        session.commit()
        return time.to_dict(), 200
    except IntegrityError as e:        
        error_msg = "Time de mesmo nome já salvo na base :/"
        return {"mesage": error_msg}, 409

    except Exception as e:
        error_msg = "Não foi possível salvar novo time:/"
        return {"mesage": error_msg}, 400
    finally:
        session.close()

@app.put('/time', tags=[time_tag])
def update_time(form: TimeUpdateSchema):
    """Editar informações de um time
    """
    time_id = form.id
    session = Session()
    try:
        time = session.query(Time).filter(Time.id == time_id).first()
        if not time:
            error_msg = "Time não encontrado na base :/"
            return {"mesage": error_msg}, 404
        else:
            
            time.nome = form.nome
            time.pais = form.pais
            time.data_fundacao = form.data_fundacao
            time.nome_fundador = form.nome_fundador
            time.descricao = form.descricao
            time.logo_url = form.logo_url

        
            session.commit()
            return time.to_dict(), 200
    except IntegrityError as e:        
        error_msg = "Time de mesmo nome já salvo na base :/"
        return {"mesage": error_msg}, 409

    except Exception as e:
        error_msg = "Não foi possível salvar novo time:/"
        return {"mesage": error_msg}, 400
    finally:
        session.close()

@app.delete('/time', tags=[time_tag])
def delete_time(query: TimeBuscaSchema):
    """Deletar um time a partir do id informado
    """
    time_id = query.id
    session = Session()
    try:
        count = session.query(Time).filter(Time.id == time_id).delete()
        session.commit()

        if count:
            return {"mesage": "time removido", "id": time_id}
        else:
            error_msg = "time não encontrado na base :/"
            return {"mesage": error_msg}, 404
    finally:
        session.close()