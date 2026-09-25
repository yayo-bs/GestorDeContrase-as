"""Funciones para generar contrasenas seguras."""

import secrets
import string


def generar_contrasena(
    longitud: int = 12,
    mayusculas: bool = True,
    minusculas: bool = True,
    numeros: bool = True,
    simbolos: bool = False,
) -> str:
    """Genera una contrasena usando las categorias seleccionadas."""
    grupos = []
    if mayusculas:
        grupos.append(string.ascii_uppercase)
    if minusculas:
        grupos.append(string.ascii_lowercase)
    if numeros:
        grupos.append(string.digits)
    if simbolos:
        grupos.append(string.punctuation)

    if not grupos:
        raise ValueError("Debes seleccionar al menos una categoria")
    if longitud < len(grupos):
        raise ValueError("La longitud debe permitir todas las categorias")

    caracteres = "".join(grupos)
    resultado = [secrets.choice(grupo) for grupo in grupos]
    resultado.extend(
        secrets.choice(caracteres) for _ in range(longitud - len(resultado))
    )
    secrets.SystemRandom().shuffle(resultado)
    return "".join(resultado)
