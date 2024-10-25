from bs4 import BeautifulSoup

def priceProcess():
    
    with open('pagina_steamdb.txt', 'r', encoding='utf-8') as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    price_div = soup.find('div', class_='single-price-line')
    if price_div:
        price_span = price_div.find('span')
        if price_span:
            precio_juego = price_span.text
            return precio_juego
        else:
            print('No se encontró el <span> con el precio.')
    else:
        print('No se encontró el div con la clase "single-price-line".')