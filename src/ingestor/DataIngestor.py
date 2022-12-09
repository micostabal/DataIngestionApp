from datetime import date
from scraper import DateParser
from typing import List
from client.DataClient import DataClient
from scraper import Scraper

class DataIngestor:
  
  def __init__(self, clients: List[DataClient]):
    self.dateParser=DateParser()
    self.scraper = Scraper()
    self.clients = clients
    
  
  def ingestDate(self, date: date):
    raw_html_date_doc = self.scraper.scrape(date)
    if raw_html_date_doc is None:
        return False

    for new_publication in self.dateParser.parse(
      date,
      raw_html_date_doc
    ):
      for client in self.clients:
        client.store_publication(new_publication)
    
    return True

