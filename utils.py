
def normalize(s:str)->str:
    """Elimina las tildes de una cadena y devuelve esa cadena normalizada

    Args:
        s (str): El string a normalizar

    Returns:
        str: El string normalizado
    """
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s



















