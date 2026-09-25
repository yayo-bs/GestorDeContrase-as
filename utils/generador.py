"""Funciones para generar contrasenas seguras."""

import secrets
import string


def generar_contrasena(longitud: int = 12) -> str:
    """Genera una contrasena aleatoria con letras y digitos."""
    if longitud < 1:
        raise ValueError("La longitud debe ser mayor que cero")

    caracteres = string.ascii_letters + string.digits
    return "".join(secrets.choice(caracteres) for _ in range(longitud))
