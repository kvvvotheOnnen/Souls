
def hrefNameProcessor(href):
    # Extraer la parte después de 'steam-'
    contenido = href.split('steam-')[1]
    
    # Si hay un segundo 'steam-' o final del segmento de la URL, cortar allí
    if '-steam' in contenido:
        contenido = contenido.split('-steam')[0]
    
    # Reemplazar guiones por espacios para un nombre más legible
    contenido_limpio = contenido.replace('-', ' ')
    return contenido_limpio
