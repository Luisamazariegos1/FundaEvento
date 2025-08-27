from app import create_app, db
from app.models import Rol

app = create_app()

with app.app_context():
    roles = [
        {"id": 1, "nombre": "Administrador"},
        {"id": 2, "nombre": "Moderador"},
        {"id": 3, "nombre": "Usuario"},
    ]

    for rol_data in roles:
        rol = Rol.query.filter_by(id=rol_data["id"]).first()
        if not rol:
            nuevo_rol = Rol(id=rol_data["id"], nombre=rol_data["nombre"])
            db.session.add(nuevo_rol)

    db.session.commit()
    print("✅ Roles cargados correctamente.")
