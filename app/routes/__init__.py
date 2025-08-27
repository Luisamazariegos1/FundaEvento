from .usuarios import usuarios_bp
from .eventos import eventos_bp
from .grupos import grupos_bp
from .participantes import participantes_bp
from .inscripciones import inscripciones_bp
from .asistencias import asistencias_bp
from .evidencias import evidencias_bp
from .evaluaciones import evaluaciones_bp
from .notificaciones import notificaciones_bp
from .reportes import reportes_bp
from .auth import auth_bp
from .main import main


def register_routes(app):
    app.register_blueprint(main)
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(eventos_bp)
    app.register_blueprint(grupos_bp)
    app.register_blueprint(participantes_bp)
    app.register_blueprint(inscripciones_bp)
    app.register_blueprint(asistencias_bp)
    app.register_blueprint(evidencias_bp)
    app.register_blueprint(evaluaciones_bp)
    app.register_blueprint(notificaciones_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(reportes_bp)
