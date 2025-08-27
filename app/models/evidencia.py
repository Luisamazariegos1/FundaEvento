from .. import db


class Evidencia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    evento_id = db.Column(db.Integer, db.ForeignKey(
        "evento.id"), nullable=False)
    nombre_archivo = db.Column(db.String(100), nullable=False)
    ruta_archivo = db.Column(db.String(200), nullable=False)
