import unittest
from unittest import mock
from src.ingestor.DataIngestor import DataIngestor

class DataIngestionIntegrationTest(unittest.TestCase):
  
  

  def test_should_scrape_and_parse_single_publication_page(self):

    dataIngestor = DataIngestor()

