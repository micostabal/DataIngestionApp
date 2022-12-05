from src.scraper.Scraper import Scraper
from datetime import date
import requests
import unittest
from unittest import TestCase, mock

def next_number(numero):
  return numero+1

class ScraperTest(TestCase):
  
  scraper = Scraper()
  mock_edition_number = 42969
  mock_date = date(2021, 6, 3)
  
  def test_scraper_should_do_sth(self):
    pass
  
  def test_can_mock_stuff(self):
    mock_function = mock.create_autospec(next_number, return_value=45)
    
    siguiente = mock_function(99)
    
    self.assertEqual(siguiente, 45)
  
  def test_should_get_edition_number(self):

    with open("./test/stubs/scraper/initialResponseF1.html", "r") as file:
      mock_function = mock.create_autospec(
        requests.get,
        return_value=file.read()
      )
    
    edition_number = ScraperTest.scraper.get_edition(ScraperTest.mock_date)
    
    self.assertEqual(edition_number, ScraperTest.mock_edition_number)
  
  def test_should_scrape(self):
    
    with open("./test/stubs/scraper/pageResponseF1.html", "r") as file:
      scraped_text = file.read()
    
    mock_function = mock.create_autospec(
      Scraper.get_edition,
      return_value=ScraperTest.mock_edition_number
    )
    
    with mock.patch('requests.get') as patched_post:
        patched_post.return_value.text = scraped_text

        fullHtmlText = ScraperTest.scraper.scrape(ScraperTest.mock_date)
        self.assertEqual(scraped_text, fullHtmlText)
    

if __name__ == "__main__":
  unittest.main()