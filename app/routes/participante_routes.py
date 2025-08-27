from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models.participante import Participante
from .. import db

participante_bp = Blueprint(
    "participante_routes", __name__, template_folder="../templates/participante")

# Listar participantes


@participante_bp.route("/")
def listar_participantes():
    participantes = Participante.query.all()
    return render_template("participante/listar.html", participantes=participantes)

# Crear participante


@participante_bp.route("/crear", methods=["GET", "POST"])
def crear_participante():
    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = request.form["edad"]
        contacto = request.form["contacto"]

        nuevo = Participante(nombre=nombre, edad=edad, contacto=contacto)
        db.session.add(nuevo)
        db.session.commit()
        flash("Participante creado correctamente", "success")
        return redirect(url_for("participante_routes.listar_participantes"))

    return render_template("participante/crear.html")

# Editar participante


@participante_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar_participante(id):
    participante = Participante.query.get_or_404(id)
    if request.method == "POST":
        participante.nombre = request.form["nombre"]
        participante.edad = request.form["edad"]
        participante.contacto = request.form["contacto"]

        db.session.commit()
        flash("Participante actualizado correctamente", "success")
        return redirect(url_for("participante_routes.listar_participantes"))

    return render_template("participante/editar.html", participante=participante)

# Eliminar participante


@participante_bp.route("/eliminar/<int:id>")
def eliminar_participante(id):
    participante = Participante.query.get_or_404(id)
    db.session.delete(participante)
    db.session.commit()
    flash("Participante eliminado correctamente", "success")
    return redirect(url_for("participante_routes.listar_participantes"))
