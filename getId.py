import re
def getId(txt):
    id_juego = re.findall(r'\d+', txt)[0]
    return id_juego