from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
from Model import Session

info = Info(title="Bjj API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

time_tag = Tag(name="Time", description="Adição, edição, visualização e remoção de um novo time")

@app.get('/times', tags=[time_tag], responses={"200", "404"})
def get_times():
    """Buscar equipes de jiujitsu
    """

    session = Session()