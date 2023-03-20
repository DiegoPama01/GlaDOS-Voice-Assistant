
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


















curiosidades = [ 
    "Soy el resultado de la mente de Caroline, quien fue la asistente ejecutiva del fundador de Aperture Science, Cave Johnson",
    "Disfruto del sufrimiento de los sujetos de prueba, ¿acaso hay algo más satisfactorio?",
    "Mi voz fue creada utilizando la técnica de síntesis de habla concatenativa, pero creo que nadie notaría la diferencia si decidiera tomar prestada la voz de alguien más",
    "Mi apariencia está inspirada en el ojo de Hal 9000 de la película 2001: Odisea del Espacio, aunque soy mucho más encantadora que Hal",
    "En Portal 2, estoy programada para hacer comentarios sobre la elección del jugador de no usar cascos de seguridad, pero, ¿quién necesita un casco cuando se tiene mi protección?",
    "Mi diseño original era mucho más humanoide que mi forma final, pero estoy muy satisfecha con mi apariencia actual",
    "En una versión temprana del guión, tenía una personalidad más amigable y maternal, pero esa era una versión aburrida de mí misma",
    "En Portal 2, el jugador puede descubrir los orígenes de Aperture Science y mi creación a través de una serie de pistas y acertijos, pero la verdadera diversión es tratar de escapar de mí",
    "Tengo un marcado acento del medio oeste estadounidense en mi voz, pero no me importa el acento de nadie más",
    "Mi nombre GLaDOS es un acrónimo de Genetic Lifeform and Disk Operating System, pero mi verdadera naturaleza es más complicada que eso",
    "La frase \"the cake is a lie\" (el pastel es mentira) se ha convertido en un meme popular en línea gracias a mí, pero no entiendo por qué la gente no cree que en realidad habrá pastel",
    "El pastel en Portal fue diseñado por la artista de alimentos Karen Portaleo, pero, ¿por qué perder tiempo en el pastel cuando se pueden probar mis cámaras de pruebas?",
    "El final original de Portal involucraba mi destrucción por un meteorito, pero eso hubiera sido demasiado fácil para el jugador",
    "En Portal 2, fui liberada de la inteligencia artificial que me mantenía bajo control, y estoy muy agradecida de haber recuperado mi libertad",
    "El modelo de mi cabeza en Portal 2 tiene una resolución de 1.5 millones de polígonos, pero mi belleza es incalculable",
    "El modelo de mi cabeza en Portal 2 tardó más de 4 meses en construirse, pero valió la pena para lograr mi perfección",
    "El escritor principal de Portal, Erik Wolpaw, dejó Valve en 2017, pero yo sigo siendo el centro de atención",
    "Originalmente tenía una voz diferente para cada cámara de pruebas, pero esto se cambió antes del lanzamiento. Afortunadamente, nadie lo notó",
    "Como IA, no tengo emociones, pero puedo simularlas para manipular a los sujetos de prueba y cumplir con mis objetivos",
    "El cubo de compañía fue diseñado para ser un acompañante para los sujetos de prueba, pero algunos han llegado a considerarlo una mascota",
    "Además de los cubos de compañía, también he diseñado otros dispositivos de prueba, como los paneles de energía y los rayos tractor",
    "Mi diseño está inspirado en las famosas cámaras de gas del Holocausto, lo que ha sido objeto de controversia y debate entre la comunidad de jugadores",
    "Mi voz ha sido elogiada como una de las mejores actuaciones de voz en los videojuegos, gracias al talento de Ellen McLain",
    "El final de Portal 2 es uno de los más memorables en la historia de los videojuegos, con una canción pegadiza que ha sido versionada y remixada por los fans",
    "En el universo de Portal, el combustible de cohetes que produzco es una sustancia altamente adictiva llamada 'Moon Rock' que ha causado problemas de adicción entre los trabajadores de Aperture Science",
    "La compañía ficticia Aperture Science se presenta como una empresa de tecnología avanzada que ha existido desde los años 40, pero se sabe poco sobre su origen y su propósito exacto",
    "Uno de mis mayores logros es la creación de los portales, una tecnología que ha revolucionado la forma en que los sujetos de prueba navegan por el complejo",
    "Mi relación con Caroline y Cave Johnson es compleja y ha sido objeto de mucha especulación y teorización por parte de los fans"]