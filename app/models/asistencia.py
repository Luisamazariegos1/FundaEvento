from .. import db
from datetime import datetime


class Asistencia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    participante_id = db.Column(db.Integer, db.ForeignKey(
        "participante.id"), nullable=False)
    evento_id = db.Column(db.Integer, db.ForeignKey(
        "evento.id"), nullable=False)
    fecha = db.Column(db.Date, default=datetime.utcnow)
    presente = db.Column(db.Boolean, default=False)
