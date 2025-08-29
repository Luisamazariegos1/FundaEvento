from .. import db


class Usuario(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    rol_id = db.Column(db.Integer, db.ForeignKey("roles.id"))
    rol = db.relationship("Rol", back_populates="usuarios")
