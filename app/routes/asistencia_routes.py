from flask import Blueprint

asistencia_bp = Blueprint("asistencias", __name__)


@asistencia_bp.get("/")
def listar():
    return "Asistencias - en construcción"
