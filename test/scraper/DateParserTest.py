from src.scraper.Scraper import Scraper
import unittest
from unittest import TestCase, mock

def next_number(numero):
  return numero+1

class ScraperTest(TestCase):
  
  def test_scraper_should_do_sth(self):
    pass
  
  def test_can_mock_stuff(self):
    mock_function = mock.create_autospec(next_number, return_value=45)
    
    siguiente = mock_function(99)
    
    self.assertEqual(siguiente, 45)
  
  def test_can_scrape(self):
    self.assertEqual(1, 2-1)


if __name__ == "__main__":
  unittest.main()