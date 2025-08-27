from .. import db
from datetime import datetime


class Inscripcion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    participante_id = db.Column(db.Integer, db.ForeignKey(
        "participante.id"), nullable=False)
    evento_id = db.Column(db.Integer, db.ForeignKey(
        "evento.id"), nullable=False)
    fecha_inscripcion = db.Column(db.DateTime, default=datetime.utcnow)
