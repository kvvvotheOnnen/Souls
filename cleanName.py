import re
def cleanName(texto_fila):
    sin_numeros = re.sub(r'\d+', '', texto_fila)
    return sin_numeros

def claneNameTrim(texto):
    t = texto.split('\n', 1)[0]
    return t