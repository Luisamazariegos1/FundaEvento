from .. import db


class Reporte(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.Text, nullable=False)
    fecha_generacion = db.Column(db.DateTime, nullable=False)
