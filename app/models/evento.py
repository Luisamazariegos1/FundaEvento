from .. import db


class Evento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_fin = db.Column(db.Date, nullable=False)
    cupos = db.Column(db.Integer, nullable=False)

    inscripciones = db.relationship("Inscripcion", backref="evento", lazy=True)
    evidencias = db.relationship("Evidencia", backref="evento", lazy=True)
