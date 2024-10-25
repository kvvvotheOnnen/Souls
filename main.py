from seleniumbase import SB
import re
from urlTransformer import juegoURL
from cleanName import cleanName, claneNameTrim
from priceProcess import priceProcess
from hrefNameProcessor import hrefNameProcessor
from getId import getId
from fechaYhora import fechaYhora

def scrap(juego):
    with SB(uc=True, headless=True) as sb:
        try:
            nombreJuego = juegoURL(juego)
            url = f"https://www.eneba.com/latam/store/all?text={nombreJuego}&enb_campaign=Main%20Search&enb_content=search%20dropdown%20-%20input&enb_medium=input&enb_source=https%3A%2F%2Fwww.eneba.com%2F&enb_term=Submit"
            sb.get(url)
            cards = sb.find_elements('.oSVLlh')
            price = sb.find_elements('css selector', '.L5ErLT')
            names = []
            prices = []
            plataforma = []
            fecha = []
            games = [] 
            for i in cards:
                name = i.get_attribute('href')
                if name and 'steam' in name:
                    hrefLimpio = hrefNameProcessor(name)
                    names.append(hrefLimpio)
                    plataforma.append('steamDB')
                    date = fechaYhora()
                    fecha.append(date)
            for i in price:        
                prices.append(i.text)
            for n, pr, pl, fe in zip(names, prices, plataforma, fecha):
                obj = {
                    "juego": n,
                    "precio": pr,
                    "plataforma": pl,
                    "fecha": fe
                }
                games.append(obj)          
            return games       
        except ValueError as err:
            print(err)
scrap('dark souls')

            

