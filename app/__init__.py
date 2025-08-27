from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

# Inicializar extensiones
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones con la app
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar Blueprints
    from app.routes.participante_routes import participante_bp
    from .routes.evento_routes import evento_bp
    from .routes.inscripcion_routes import inscripcion_bp
    from .routes.asistencia_routes import asistencia_bp
    from .routes.evidencia_routes import evidencia_bp
    from .routes.reporte_routes import reporte_bp

    app.register_blueprint(participante_bp, url_prefix="/participantes")
    app.register_blueprint(evento_bp, url_prefix="/eventos")
    app.register_blueprint(inscripcion_bp, url_prefix="/inscripciones")
    app.register_blueprint(asistencia_bp, url_prefix="/asistencia")
    app.register_blueprint(evidencia_bp, url_prefix="/evidencias")
    app.register_blueprint(reporte_bp, url_prefix="/reportes")

    return app
