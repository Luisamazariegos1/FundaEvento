from .. import db


class Participante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    contacto = db.Column(db.String(100), nullable=False)
    rol = db.Column(db.String(20), default="niño")  # niño, encargado, admin

    inscripciones = db.relationship(
        "Inscripcion", backref="participante", lazy=True)
