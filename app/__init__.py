# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)

    # Cargar modelos para que Alembic los vea
    with app.app_context():
        from . import models  # app/models/__init__.py

    migrate.init_app(app, db)

    # 🔴 IMPORTANTE: registrar blueprints aquí (no arriba)
    from .routes.participante_routes import participante_bp
    app.register_blueprint(participante_bp, url_prefix="/api")

    # Ruta de diagnóstico
    @app.get("/__routes__")
    def _routes():
        return "\n".join(sorted(str(r) for r in app.url_map.iter_rules())), 200, {
            "Content-Type": "text/plain; charset=utf-8"
        }

    @app.get("/health")
    def health():
        return "ok", 200

    return app
