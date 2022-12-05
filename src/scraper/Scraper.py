from datetime import date
import requests
import re
import yaml

with open("./src/config/scraper_config.yml", "r") as stream:
    try:
        params = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)


class Scraper:

    def __init__(self) -> None:
        self.get_url_inicial = lambda fecha : params['url']['initial_url'].format(fecha)
        self.get_url = lambda fecha, edicion : params['url']['edition_url'].format(fecha, edicion)

    def get_edition(self, scrape_date):
        url_inicial = self.get_url_inicial(scrape_date.strftime("%d-%m-%Y"))
        response = requests.get(url_inicial, timeout=30)
        total_doc = response.text
        patron_edicion = r'{}'.format(params['patrones']['edicion'])
        try:
            grupo_numero = re.search(patron_edicion, total_doc).group('numero')
            numero = int(grupo_numero.replace('.', ''))
            return numero
        except AttributeError:
            return None

    def scrape(self, scrape_date: date) -> str:
        edicion = self.get_edition(scrape_date)
        if edicion == None:
            return None
        url = self.get_url(
            scrape_date.strftime("%d-%m-%Y"),
            edicion
        )
        
        response = requests.get(url, timeout=30)
        
        return response.text


if __name__ == "__main__" : pass