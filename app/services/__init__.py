"""
Registro central de servicios de negocio.
Aquí podrías inicializar servicios externos si es necesario.
"""

from .participante_service import ParticipanteService
from .evento_service import EventoService
# los demás se agregan aquí cuando los crees


def register_services(app):
    """
    Aquí podrías inyectar dependencias o registrar servicios.
    Por ahora solo dejamos el hook preparado.
    """
    pass
