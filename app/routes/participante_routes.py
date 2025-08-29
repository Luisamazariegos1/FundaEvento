from .. import db
# app/routes/participante_routes.py
from flask import Blueprint, request, jsonify
from .. import db
from ..models.participante import Participante

participante_bp = Blueprint("participante_bp", __name__)


@participante_bp.get("/participantes")
def listar_participantes():
    items = Participante.query.order_by(Participante.creado_en.desc()).all()
    return jsonify([
        {
            "id": p.id,
            "nombre": p.nombre,
            "email": p.email,
            "telefono": p.telefono,
            "creado_en": p.creado_en.isoformat() if p.creado_en else None
        } for p in items
    ]), 200


@participante_bp.post("/participantes")
def crear_participante():
    data = request.get_json(force=True)
    p = Participante(
        nombre=data.get("nombre"),
        email=data.get("email"),
        telefono=data.get("telefono"),
    )
    db.session.add(p)
    db.session.commit()
    return jsonify({"id": p.id}), 201
