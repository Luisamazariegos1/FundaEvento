from flask import Flask, jsonify, render_template
from flask_migrate import Migrate
from .config import Config
from .models import db

migrate = Migrate()


def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Importar modelos (asegura que existen)
    with app.app_context():
        from . import models

    # Home simple
    @app.get("/")
    def index():
        return jsonify({
            "app": "Fundaevento API",
            "status": "ok",
            "endpoints": [
                "/health",
                "/api/participantes"
            ]
        })

    @app.get("/health")
    def health():
        return "ok", 200

    @app.errorhandler(404)
    def not_found(e):
        return render_template("errors/404.html"), 404

    return app
