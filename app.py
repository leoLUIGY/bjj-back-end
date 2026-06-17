from flask_openapi3 import OpenAPI, Info
from flask_cors import CORS

info = Info(title="Bjj API", version="1.0.0")

app = OpenAPI(__name__, info=info)

CORS(app)

from Routes.Time_Rotas import *